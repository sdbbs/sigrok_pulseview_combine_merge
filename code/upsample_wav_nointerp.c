/*

Build in MINGW64 shell of MSYS2 in Windows;

Install the libsndfile library in MSYS2/MINGW64 with (is at version mingw-w64-x86_64-libsndfile-1.0.30-1 as of Oct 2020):

    pacman -S mingw-w64-x86_64-libsndfile

compile with:

    gcc -Wall -g upsample_wav_nointerp.c -o upsample_wav_nointerp -lsndfile

call with:

    ./upsample_wav_nointerp.exe ../test.wav 48000
    ./upsample_wav_nointerp.exe ../test.wav 1000000000

*/

#include <stdint.h> // uint32_t etc
#include <stdio.h> //printf, perror
#include <stdbool.h> // bool
#include <limits.h>
#include <stdlib.h> // realpath (but not in MINGW64); strtoul (instead of atoi, SO:7021725)
#include <unistd.h> // access

#include <sndfile.h>
//~ #include <samplerate.h>

#if  defined(_MSC_VER) || defined(__MINGW32__) || defined(__MINGW64__) // SO:45124869
#ifndef PATH_MAX
#define PATH_MAX _MAX_PATH
#endif
#define realpath(N,R) _fullpath((R),(N),_MAX_PATH)
#endif

char in_abs_path[PATH_MAX+1] = {0};
uint32_t in_new_rate = 0;
uint32_t srate_factor = 0;

SNDFILE *infile, *outfile; //SO:10558275
SF_INFO sfinfo_in, sfinfo_out;

#define BUFFER_LEN 1024
//static float datain[BUFFER_LEN]; // nope - if we iterate via frames, we now need to adjust this size for number of channels, which we'll only have at runtime - so we must calloc!

void usage(void) {
  fprintf(stderr, "Usage: upsample_wav_interp path/to/file.wav new_sample_rate_integer\n");
  fflush(stderr);
  exit(EXIT_FAILURE);
  /* NOTREACHED */
}

bool parseCommandLine(int argc, char* argv[]) {
  //printf("argc is %d; argv[0] is: '%s'\n", argc, argv[0]);
  if (argc != 3) {
    fprintf(stderr, "Error: need exactly 2 command line arguments\n");
    fflush(stderr);
    return false;
  }
  char *inwav_path = argv[1];
  char *retptr = NULL;
  retptr = realpath(inwav_path, in_abs_path);
  if (!retptr) {
    perror("Error: ");
    fflush(stderr);
    return false;
  }
  if( access( retptr, F_OK ) == -1 ) {
    fprintf(stderr, "Error: requested file cannot be opened: %s\n", retptr);
    fflush(stderr);
    return false;
  }
  fprintf(stderr, "Got input file: %s\n", in_abs_path);
  fflush(stderr);
  char *end;
  in_new_rate = (uint32_t) strtoul(argv[2], &end, 10);
  if (in_new_rate == 0) {
    fprintf(stderr, "Error: possibly cannot parse argument - got input rate 0 (errno: %d)\n", errno);
    //perror("Error: "); // just prints "Error: : No error" here
    fflush(stderr);
    return false;
  }
  fprintf(stderr, "Got input new rate: %d\n", in_new_rate);
  fflush(stderr);
  return true;
}

int main(int argc, char* argv[]) {
  // argv[0] is this programs path
  if (!parseCommandLine(argc, argv)) {
    usage();
    //return 1;
  }

  infile = sf_open(in_abs_path, SFM_READ, &sfinfo_in);
  fprintf(stderr, "Opened input file: %s with sampling rate: %d and number of channels: %d\n", in_abs_path, sfinfo_in.samplerate, sfinfo_in.channels);
  fflush(stderr);

  srate_factor = in_new_rate/sfinfo_in.samplerate;
  fprintf(stderr, "Sample rate conversion factor: %d\n", srate_factor);
  fflush(stderr);

  fprintf(stderr, " *** Assuming FLOAT_LE sample format ***\n");
  fflush(stderr);

  size_t outfile_path_len = strlen(in_abs_path) + 4; // just add '_out'
  //char* out_abs_path = (char*) malloc(outfile_path_len * sizeof(char));
  char* out_abs_path = (char*) calloc(outfile_path_len, sizeof(char)); // zero it out
  char dot = '.'; // specifically has to be a char, as it is interpreted as int in strrchr
  char* last_dot = strrchr(in_abs_path, dot);
  strncpy(out_abs_path, in_abs_path, last_dot-in_abs_path);
  strcat(out_abs_path, "_out");
  strcat(out_abs_path, last_dot);
  fprintf(stderr, "Saving to output file: %s\n", out_abs_path);
  fflush(stderr);

  sfinfo_out.samplerate = in_new_rate;
  sfinfo_out.channels = sfinfo_in.channels;
  sfinfo_out.format = sfinfo_in.format; // "SF_ENDIAN_LITTLE | SF_FORMAT_RAW | SF_FORMAT_PCM_16 ;"
  // no need to set sfinfo_out.frames ; see:
  // https://github.com/libsndfile/libsndfile/blob/master/tests/headerless_test.c
  // "sfinfo.frames = 123456789 ; /* Wrong length. Library should correct this on sf_close. */"
  outfile = sf_open(out_abs_path, SFM_WRITE, &sfinfo_out);

  uint32_t readcount;
  //static float dataout[srate_factor*BUFFER_LEN]; // nope, need to malloc (error: storage size of 'dataout' isn't constant)
  //float* dataout = malloc(srate_factor*BUFFER_LEN * sizeof(float));
  float* datain = calloc(sfinfo_in.channels*BUFFER_LEN, sizeof(float)); // zero it out
  float* dataout = calloc(srate_factor*sfinfo_in.channels*BUFFER_LEN, sizeof(float)); // zero it out
  uint64_t total_samples_written = 0;

  // note: sf_read_float reads samples (items); for multichannel, it fails for BUFFER_LEN that is not a multiple of number of channels
  // so, use sf_readf_float instead; which reads frames, which "is just a block of samples, one for each channel"

  while ((readcount = sf_readf_float (infile, datain, BUFFER_LEN)))
  {
    // example with libsamplerate (SO:10558275):
    //src_simple (&src_data, SRC_SINC_BEST_QUALITY, 1);
    //sf_write_double (outfile, dataout, readcount) ;

    //fprintf(stderr, "readcount %d\n", readcount);
    //fflush(stderr);

    // // this was the loop for (mono) with sf_read_float:
    // for(int i=0; i<readcount; i++) {
    //   float inval = datain[i];
    //   //fprintf(stderr, "i %d inval %f\n", i, inval);
    //   for(int tc=0; tc<srate_factor; tc++) {
    //     int newind = i*srate_factor + tc;
    //     dataout[newind] = inval;
    //     //fprintf(stderr, "i %d inval %f tc %d readcount %d newind %d\n", i, inval, tc, readcount, newind);
    //     //fflush(stderr);
    //   }
    // }

    // the loop for multichannel with sf_readf_float; readcount is here number of *frames* read;
    // so here, we do not duplicate samples within a frame - we duplicate the frames!
    for(int ifr=0; ifr<readcount; ifr++) {
      for(int tc=0; tc<srate_factor; tc++) {
        for(int isamp=0; isamp<sfinfo_in.channels; isamp++) {
          int origind = ifr*sfinfo_in.channels + isamp;
          float inval = datain[origind];
          int newind = ifr*sfinfo_in.channels*srate_factor + tc*sfinfo_in.channels + isamp;
          //fprintf(stderr, "ifr %d tc %d isamp %d origind %d newind %d inval %f readcount %d\n", ifr, tc, isamp, origind, newind, inval, readcount); fflush(stderr);
          dataout[newind] = inval;
        }
      }
    }

    uint64_t frames_to_write = srate_factor*readcount;
    //sf_write_float(outfile, dataout, samples_to_write) ;
    sf_writef_float(outfile, dataout, frames_to_write) ;
    total_samples_written += frames_to_write*sfinfo_in.channels;//samples_to_write;
  };

  sf_close(infile);
  //sfinfo_out.frames = total_samples_written; // seems to have no effect, since sf_close should correct this; note that programs like `mediainfo` will likely report the duration wrong for huge sampling rates
  sf_close(outfile);

  free(datain);
  free(dataout);

  fprintf(stderr, "Wrote %llu samples. Program finished.\n", total_samples_written);
  fflush(stderr);

  return 0;
}
