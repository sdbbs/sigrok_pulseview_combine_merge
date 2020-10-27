#!/usr/bin/env python3

"""
Note: sigrok session expects all tracks to be declared sequentially, e.g.:
probe1=... probe2=... probe3=... probe4=... probe5=... probe6=... probe7=... probe8=... analog9=...
(see C:\Program Files (x86)\sigrok\PulseView\examples\ad5258_read_once_write_continuously_triangle.sr)
And, in that case, the analog data files are called analog-1-9-1, analog-1-9-2 ... etc.
Note also, that first the digital tracks get loaded, and then the analog tracks
get loaded one after the other (i.e. not in parallel)

Call with:

python3 code/merge_sr_sessions.py data/*_dg.sr data/*_an_1GHz.sr
"""

import sys, os
import shutil
import argparse
import tempfile
import zipfile
import configparser
import io
import itertools
import re
from contextlib import ExitStack # Python 3.3+

class InputSrFile(object):
  def __init__(self, *args, **kwargs):
    self.path = kwargs.get('path', "")
    self.archive = kwargs.get('archive', None)
    self.metadata = kwargs.get('metadata', None)
    self.version = kwargs.get('version', None)
    self.num_logic_ch = kwargs.get('num_logic_ch', 0)
    self.num_anlog_ch = kwargs.get('num_anlog_ch', 0)
    self.dg_fl_list = kwargs.get('dg_fl_list', []) # converted names
    self.an_fl_list = kwargs.get('dg_fl_list', []) # converted names
  def __str__(self):
    return "{}".format( self.__dict__ )

def atoi(text): # SO:5967500
  return int(text) if text.isdigit() else text
def natural_keys(text):
  '''
  alist.sort(key=natural_keys) sorts in human order
  http://nedbatchelder.com/blog/200712/human_sorting.html
  (See Toothy's implementation in the comments)
  '''
  return [ atoi(c) for c in re.split(r'(\d+)', text) ]

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
  an_sr_files = [] # list of sr files with analog captures
  dg_sr_files = [] # list of sr files with digital captures
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
      tfobj.num_logic_ch = tfobj.metadata.getint('device 1', 'total probes')
      out_total_probes += tfobj.num_logic_ch
      if tfobj not in dg_sr_files:
        dg_sr_files.append(tfobj)
    if 'total analog' in tfobj.metadata['device 1']:
      tfobj.num_anlog_ch = tfobj.metadata.getint('device 1', 'total analog')
      out_total_analog += tfobj.num_anlog_ch
      if tfobj not in an_sr_files:
        an_sr_files.append(tfobj)
    for (each_key, each_val) in tfobj.metadata.items('device 1'):
      print("  {}: {}".format(each_key, each_val))
      if each_key.startswith("probe"):
        out_probe_names.append( "{}_{}".format(each_val, itf) )
      elif each_key.startswith("analog"):
        out_analog_names.append( "{}_{}".format(each_val, itf) )
  print()
  print("Total digital tracks to export: {}".format(out_total_probes))
  print("Total  analog tracks to export: {}".format(out_total_analog))
  print()
  print("Output metadata:")
  out_metadata_config['device 1']['total analog'] = str( out_total_analog )
  out_metadata_config['device 1']['total probes'] = str( out_total_probes )
  num_dig_chans = 0
  for ipn, pname in enumerate(out_probe_names):
    tipn = ipn+1
    out_metadata_config['device 1']['probe{}'.format(tipn)] = pname
    num_dig_chans = tipn
  analog_indices = []
  for ian, aname in enumerate(out_analog_names):
    new_analog_idx = ian+1+num_dig_chans
    out_metadata_config['device 1']['analog{}'.format(new_analog_idx)] = aname
    analog_indices.append(new_analog_idx)
  out_config_string = io.StringIO()
  out_metadata_config.write(out_config_string)
  print(out_config_string.getvalue())
  print()
  outprocdir = os.path.join( os.path.abspath(args.outdir), args.outfilename )
  outsrfile = "{}.sr".format(outprocdir)
  print("Extracting data in folder: {}; output file will be: {}".format(outprocdir, outsrfile))
  if os.path.isdir( outprocdir ):
    shutil.rmtree( outprocdir ) # os.rmdir( outprocdir )
    print("Removed existing directory {}".format(outprocdir))
  os.mkdir( outprocdir )
  print("Created directory {}".format(outprocdir))
  print("")
  idx_dg = 2 # start from 2; we'll have to "pack" these into `logic-1-*` files in the end
  idx_an = 1
  pat_analog = re.compile(r'analog-1-(\d+)')
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
          tfobj.dg_fl_list.append(newfname)
        elif zipfname.startswith("analog-1-"):
          got_an = True
          #newfname = zipfname.replace("analog-1-1", "analog-1-{}".format(num_dig_chans + idx_an)) # works only for analog-1-1-30 input, but not analog-1-3-30; must use regex - see SO:64559976
          def numrepl(matchobj):
            prev_offset = 0
            if itf > 0:
              for ii in range(itf):
                prev_offset += input_sr_files[ii].num_anlog_ch
            return "analog-1-{}".format( analog_indices[ int(matchobj.group(1))-1 + prev_offset ] )
          newfname = pat_analog.sub( numrepl, zipfname )
          tfobj.an_fl_list.append(newfname)
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
  print("Merging digital data...")
  dg_fl_lists = []
  for tfobj in dg_sr_files:
    tfobj.dg_fl_list.sort(key=natural_keys)
    dg_fl_lists.append(tfobj.dg_fl_list)
  #num_dig_capts = idx_dg-1
  for ftuple in itertools.zip_longest(*dg_fl_lists):
    outstr = ""
    outdata = []
    outfname = ''
    # NOTE: this code assumes the first of the ftuple has the biggest ammount of files; if that is not the case, code is likely to crash!
    for itf, tfile in enumerate(ftuple):
      outstr += "{} {}; ".format(tfile, dg_sr_files[itf].num_logic_ch)
      if tfile is not None:
        tfpath = os.path.join( outprocdir, tfile )
        if not outfname:
          outfname = list(tfile)
          outfname[6] = '1'
          outfname = "".join(outfname)
        with open(tfpath, "rb") as f:
          if itf == 0:
            outdata = bytearray(f.read()) # don't bitshift these
          else:
            toutdata = bytearray(f.read())
            # assume these blocks are of same length:
            for itb, tbyte in enumerate(toutdata):
              outdata[itb] = outdata[itb] + (tbyte << dg_sr_files[itf-1].num_logic_ch)
    outstr += "{}".format(outfname)
    if outdata and outfname:
      tfpath = os.path.join( outprocdir, outfname )
      with open(tfpath, "wb") as f:
        f.write(outdata)
      for tfile in ftuple:
        if tfile is not None:
          os.remove( os.path.join( outprocdir, tfile ) )
    #print(outstr)
  # finally, output metadata
  mdpath = os.path.join( outprocdir, "metadata" )
  with open(mdpath, "w") as f:
    out_metadata_config.write(f)
  # and pack into zip
  print("Packing into sr zip (unfortunately, it also adds .zip extension at end)")
  shutil.make_archive(outsrfile, 'zip', outprocdir)



###### end of main()

####################################
# ENTRY POINT
if __name__ == '__main__':
  main(sys.argv[1:])
