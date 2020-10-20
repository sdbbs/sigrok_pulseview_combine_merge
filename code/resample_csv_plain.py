#!/usr/bin/env python3



import sys, os
import argparse
import csv


def parse_args(args):
  parser = argparse.ArgumentParser(description="""resample .csv file with uniform sampling timestamps (floating point seconds, without gaps); currently there is no interpolation, for upsampling values are simply repeated. The output filename is the same as the input filename, except with the new sampling period appended""")
  parser.add_argument('input_csv_file_path', action="store", help="relative or absolute path(s) to input .csv file (assumed first column are uniform sampling timestamps as floating point seconds)") # positional;
  parser.add_argument('--resample_period', default='0.000000001', help='The desired sampling period in the output .csv; if unspecified, the default is "%(default)s"')
  #parser.add_argument('--resample_period', default='0.000002', help='The desired sampling period in the output .csv; if unspecified, the default is "%(default)s"') # tester
  return parser.parse_args(args)


############## MAIN FUNCTION ######################

def main(inargs):
  args = parse_args(inargs)
  in_csv_abspath = os.path.abspath(args.input_csv_file_path)
  in_csv_basename = os.path.basename(in_csv_abspath)
  in_csv_absname, in_csv_ext = os.path.splitext(in_csv_abspath)
  resample_period = float(args.resample_period)

  out_csv_abspath = "{}_{}{}".format(in_csv_absname, args.resample_period, in_csv_ext)
  print("Loading input CSV file: {}, saving output file {}".format(in_csv_abspath, out_csv_abspath))
  print("\n\n")

  with open(in_csv_abspath, mode='r') as in_file, open(out_csv_abspath, mode='w') as out_file:
    csv_reader = csv.reader(in_file, delimiter=',')
    csv_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    line_count = 0
    last_row = None
    new_ts = 0.0
    for row in csv_reader:
      if line_count == 0:
        csv_writer.writerow(row)
        line_count += 1
        sys.stderr.write("\r{}: {}".format(line_count, row)); sys.stderr.flush()
        continue # skip the header
      if last_row is None: # entry point - first in row
        csv_writer.writerow(row)
        last_row = row
        line_count += 1
        sys.stderr.write("\r{}: {}".format(line_count, row)); sys.stderr.flush()
      else:
        # here we are at least on second row;
        # output the duplicate samples from last row
        this_ts = float(row[0])
        last_ts = float(last_row[0]) # should be already written
        tts = last_ts
        while tts < this_ts:
          tts += resample_period
          #if (tts >= this_ts): break # exit loop in this case, so we do not double values ; this can still do duplicates!
          if ("{:.09f}".format(tts) >= "{:.09f}".format(this_ts)): break
          t_row = ["{:.09f}".format(tts)] #[tts] # must format as float here, else it's all over the place with notations
          t_row.extend(last_row[1:]) # in-place
          csv_writer.writerow(t_row)
          line_count += 1
          sys.stderr.write("\r{}: {}".format(line_count, t_row)); sys.stderr.flush()
        # here we should be ready to output current row
        ft_row = ["{:.09f}".format(this_ts)]
        ft_row.extend(row[1:]) # in-place
        csv_writer.writerow(ft_row)
        last_row = row
        line_count += 1
        sys.stderr.write("\r{}: {}".format(line_count, ft_row)); sys.stderr.flush()


###### end of main()

####################################
# ENTRY POINT
if __name__ == '__main__':
  main(sys.argv[1:])
