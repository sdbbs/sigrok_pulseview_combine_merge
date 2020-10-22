#!/usr/bin/env python3

"""
Note: sigrok session expects all tracks to be declared sequentially, e.g.:
probe1=... probe2=... probe3=... probe4=... probe5=... probe6=... probe7=... probe8=... analog9=...
(see C:\Program Files (x86)\sigrok\PulseView\examples\ad5258_read_once_write_continuously_triangle.sr)
And, in that case, the analog data files are called analog-1-9-1, analog-1-9-2 ... etc.
Note also, that the analog tracks get loaded one after the other (i.e. not in parallel)

https://github.com/sigrokproject/libsigrok/blob/master/src/output/srzip.c :

* Allocate one samples buffer for all logic channels, and
* several samples buffers for the analog channels. Allocate
* buffers of CHUNK_SIZE size (in bytes), and determine the
* sample counts from the respective channel counts and data
* type widths.

https://github.com/sigrokproject/libsigrok/blob/master/src/input/vcd.c :

* Supported features:
* - $var with 'wire' and 'reg' types of scalar variables

(that is, analog captures in .vcd input are not supported, since

this works:
[device 1]
samplerate=1 GHz
total analog=2
analog1=CH1
analog2=CH2
unitsize=1

"""

import sys, os
import argparse
import tempfile
import zipfile
import configparser
import io

class InputSrFile(object):
  def __init__(self, *args, **kwargs):
    self.path = kwargs.get('path', "")
    self.archive = kwargs.get('archive', None)
    self.metadata = kwargs.get('metadata', None)
    self.version = kwargs.get('version', None)
  def __str__(self):
    return "{}".format( self.__dict__ )

def parse_args(args):
  parser = argparse.ArgumentParser(description="""merge multiple sikrok/PulseView .sr session files into a single one. Note that all individual .sr files must be at the same sampling rate. A folder (processing directory, which is deleted and re-created at each call of the script) will be created in the output directory, where data will be stored during processing; then this data gets packed into the output .sr file (also stored in the output directory)""")
  parser.add_argument('input_sr_file', nargs='+', action="store", help="relative or absolute paths to input .sr files") # positional;
  parser.add_argument('--outdir', default=tempfile.gettempdir(), help='Output directory, where the output .sr file (and related processing directory) will be saved; if unspecified, the default is "%(default)s"')
  parser.add_argument('--outfilename', default='mergedout', help='Basename of the processing directory and the output .sr file in the output directory; if unspecified, the default is "%(default)s"')
  return parser.parse_args(args)

############## MAIN FUNCTION ######################

def main(inargs):
  args = parse_args(inargs)
  input_sr_files = []
  out_samplerate = None
  for tfile in args.input_sr_file:
    fname, ext = os.path.splitext(tfile)
    if ext == '.sr':
      tfpath = os.path.abspath(tfile)
      tfobj = InputSrFile(path=tfpath)
      tfobj.archive = zipfile.ZipFile(tfpath, 'r')
      metadata_binstr = tfobj.archive.read('metadata')
      metadata_str = metadata_binstr.decode('utf-8')
      metadata_buf = io.StringIO(metadata_str)
      ini_config = configparser.ConfigParser()
      ini_config.read_file(metadata_buf)
      tfobj.metadata = ini_config
      if out_samplerate is None:
        out_samplerate = tfobj.metadata['device 1']['samplerate']
        print("Assumed output samplerate: {}".format(out_samplerate))
      else:
        this_samplerate = tfobj.metadata['device 1']['samplerate']
        if out_samplerate != this_samplerate:
          print("Error: got samplerate {}, different from the assumed output samplerate {}; exiting.".format(this_samplerate, out_samplerate))
          sys.exit(1)
      tfobj.version = tfobj.archive.read('version').decode('utf-8')
      if tfobj.version != '2':
        print("Error: got version {}, but only .sr version 2 format is supported. Exiting.".format(tfobj.version))
        sys.exit(1)
      input_sr_files.append( tfobj )
    else:
      print("Invalid file extension '{}' for {}; ignoring this file")
  numinputfiles = len(input_sr_files)
  out_metadata_config = None
  out_version = None
  out_total_probes = 0 # digital tracks
  out_total_analog = 0 # analog tracks
  out_probe_names = []
  out_analog_names = []
  print("Got .sr input files: ")
  for itf, tfobj in enumerate(input_sr_files):
    print("{:02d}/{:02d}: {}".format(itf+1, numinputfiles, tfobj.path))
    #print(tfobj.metadata['device 1']['samplerate'])  # metadata._sections ; metadata.__dict__
    if out_version is None:
      out_version = tfobj.version
    if out_metadata_config is None:
      # start out_metadata_config off as a copy of the first metadata
      config_string = io.StringIO() # SO:23416370
      tfobj.metadata.write(config_string)
      # We must reset the buffer to make it ready for reading.
      config_string.seek(0)
      out_metadata_config = configparser.ConfigParser()
      out_metadata_config.read_file(config_string)
    if 'total probes' in tfobj.metadata['device 1']:
      this_tot_probes = tfobj.metadata.getint('device 1', 'total probes')
      out_total_probes += this_tot_probes
    if 'total analog' in tfobj.metadata['device 1']:
      this_tot_analog = tfobj.metadata.getint('device 1', 'total analog')
      out_total_analog += this_tot_analog
    for (each_key, each_val) in tfobj.metadata.items('device 1'):
      print("  {}: {}".format(each_key, each_val))
  print()
  print("Total digital tracks to export: {}".format(out_total_probes))
  print("Total  analog tracks to export: {}".format(out_total_analog))
  outprocdir = os.path.join( os.path.abspath(args.outdir), args.outfilename )
  outsrfile = "{}.sr".format(outprocdir)
  print("Extracting data in folder: {}; output file will be: {}".format(outprocdir, outsrfile))
  if os.path.isdir( outprocdir ):
    os.rmdir( outprocdir )
    print("Removed existing directory {}".format(outprocdir))
  os.mkdir( outprocdir )
  print("Created directory {}".format(outprocdir))
  print("")
  idx_dg = 1
  idx_an = 1
  for itf, tfobj in enumerate(input_sr_files):
    print("Extracting {:02d}/{:02d}: {}".format(itf+1, numinputfiles, tfobj.path))
    got_dg = False
    got_an = False
    files_unpacked = 0
    with tfobj.archive as zip_arch:
      for zipfname in zip_arch.namelist():
        newfname = zipfname
        if zipfname.startswith("logic-"):
          got_dg = True
          newfname = zipfname.replace("logic-1", "logic-{}".format(idx_dg))
        elif zipfname.startswith("analog-1-"):
          got_an = True
          newfname = zipfname.replace("analog-1-1", "analog-1-{}".format(idx_an))
        #print("{} -> {}".format(zipfname, newfname))
        outfpath = os.path.join( outprocdir, newfname )
        with open(outfpath, "wb") as f:  # open the output path for writing
          f.write(zip_arch.read(zipfname))  # save the contents of the file in it
        files_unpacked += 1
    print("  ... unpacked {} files".format(files_unpacked))
    # end processing this .sr file; update idx_* accordingly
    if got_dg:
      idx_dg += 1
    if got_an:
      idx_an += 1

###### end of main()

####################################
# ENTRY POINT
if __name__ == '__main__':
  main(sys.argv[1:])
