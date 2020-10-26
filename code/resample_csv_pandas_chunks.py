#!/usr/bin/env python3

# NOTE: if using MSYS2 in Windows - pandas is only available in MINGW32/64! Alternatively, in Windows, try running the script under Anaconda Python
# NOTE: VERY memory-intensive script - is likely to cause your system to hang! And very likely to fail with:
# MemoryError: Unable to allocate 37.3 GiB for an array with shape (5011232001,) and data type int64


import sys, os
import argparse
import pandas as pd


def parse_args(args):
  parser = argparse.ArgumentParser(description="""resample .csv file with uniform sampling timestamps (floating point seconds, without gaps); currently there is no interpolation, for upsampling values are simply repeated. The output filename is the same as the input filename, except with the new sampling period appended""")
  parser.add_argument('input_csv_file_path', action="store", help="relative or absolute path(s) to input .csv file (assumed first column are uniform sampling timestamps as floating point seconds)") # positional;
  parser.add_argument('--resample_period', default='1ns', help='The desired sampling period in the output .csv; if unspecified, the default is "%(default)s"')
  return parser.parse_args(args)


############## MAIN FUNCTION ######################

def main(inargs):
  args = parse_args(inargs)
  in_csv_abspath = os.path.abspath(args.input_csv_file_path)
  in_csv_basename = os.path.basename(in_csv_abspath)
  in_csv_absname, in_csv_ext = os.path.splitext(in_csv_abspath)

  # see also: https://stackoverflow.com/questions/64423106/upsample-floating-point-second-series-in-csv-with-pandas

  print("Loading input CSV file: {}".format(in_csv_abspath))
  out_csv_filename = "{}_{}{}".format(in_csv_absname, args.resample_period, in_csv_ext)
  #df_data = pd.read_csv(in_csv_abspath)
  df_dtype = { "Time[s]": float, "Channel 0": float }
  reader = pd.read_csv(in_csv_abspath, dtype=df_dtype, chunksize=10000) # chunksize is ammount of rows
  write_header = True
  for i, tchunk in enumerate(reader):
    columsDataFrame=tchunk.columns
    tchunk.index = pd.to_timedelta(tchunk.iloc[:,0], unit='s')
    print("Resampling {}...".format(i+1))
    df_resampled = tchunk.resample(args.resample_period).pad()
    print("Re-calculate index ...")
    df_resampled.iloc[:,0] = df_resampled.index.total_seconds()
    df_resampled.to_csv(out_csv_filename, index=False, header=write_header, mode='a')
    write_header = False

###### end of main()

####################################
# ENTRY POINT
if __name__ == '__main__':
  main(sys.argv[1:])
