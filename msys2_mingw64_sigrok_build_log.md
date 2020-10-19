# Build log, Windows 10, MSYS2/MINGW64 build of sigrok (Oct 2020)

See:

* https://sigrok.org/wiki/Windows#Native_build_using_MSYS2
* https://sigrok.org/gitweb/?p=sigrok-util.git;a=blob;f=cross-compile/msys2/README

First attempt - in MSYS2 shell:

```
$ git clone git://sigrok.org/sigrok-util sigrok-util_git
...
$ cd sigrok-util_git/
$ ./cross-compile/msys2/sigrok-native-msys2 prepare
Building in an 'MSYS2 MSYS' shell will not work, aborting.
Please use the 'MSYS2 MinGW 64-bit' (or 32-bit) shell.
```

Note, at time of writing, commit 149202b4da310b2828447711db6adbe07e7d815a (from Mon Sep 28 23:12:01 2020) was checked out from `sigrok-util`.

Ok, then in MINGW64 shell:

```
$ cd sigrok-util_git
$ ./cross-compile/msys2/sigrok-native-msys2 prepare
:: Synchronizing package databases...
 mingw32 is up to date
 mingw64 is up to date
 msys is up to date
warning: autoconf-2.69-5 is up to date -- reinstalling
warning: automake-wrapper-11-1 is up to date -- reinstalling
warning: libtool-2.4.6-9 is up to date -- reinstalling
warning: make-4.3-1 is up to date -- reinstalling
warning: wget-1.20.3-1 is up to date -- reinstalling
warning: patch-2.7.6-1 is up to date -- reinstalling
:: There are 17 members in group mingw-w64-x86_64-toolchain:
:: Repository mingw64
   1) mingw-w64-x86_64-binutils  2) mingw-w64-x86_64-crt-git  3) mingw-w64-x86_64-gcc  4) mingw-w64-x86_64-gcc-ada  5) mingw-w64-x86_64-gcc-fortran
   6) mingw-w64-x86_64-gcc-libgfortran  7) mingw-w64-x86_64-gcc-libs  8) mingw-w64-x86_64-gcc-objc  9) mingw-w64-x86_64-gdb
   10) mingw-w64-x86_64-headers-git  11) mingw-w64-x86_64-libmangle-git  12) mingw-w64-x86_64-libwinpthread-git  13) mingw-w64-x86_64-make
   14) mingw-w64-x86_64-pkg-config  15) mingw-w64-x86_64-tools-git  16) mingw-w64-x86_64-winpthreads-git  17) mingw-w64-x86_64-winstorecompat-git

Enter a selection (default=all):

warning: mingw-w64-x86_64-binutils-2.35.1-2 is up to date -- reinstalling
warning: mingw-w64-x86_64-crt-git-8.0.0.6001.98dad1fe-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-gcc-10.2.0-4 is up to date -- reinstalling
warning: mingw-w64-x86_64-gcc-fortran-10.2.0-4 is up to date -- reinstalling
warning: mingw-w64-x86_64-gcc-libgfortran-10.2.0-4 is up to date -- reinstalling
warning: mingw-w64-x86_64-gcc-libs-10.2.0-4 is up to date -- reinstalling
warning: mingw-w64-x86_64-gdb-9.2-3 is up to date -- reinstalling
warning: mingw-w64-x86_64-headers-git-8.0.0.6001.98dad1fe-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-libmangle-git-8.0.0.6001.98dad1fe-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-libwinpthread-git-8.0.0.6001.98dad1fe-3 is up to date -- reinstalling
warning: mingw-w64-x86_64-make-4.3-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-pkg-config-0.29.2-2 is up to date -- reinstalling
warning: mingw-w64-x86_64-tools-git-8.0.0.6001.98dad1fe-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-winpthreads-git-8.0.0.6001.98dad1fe-3 is up to date -- reinstalling
warning: mingw-w64-x86_64-winstorecompat-git-8.0.0.6001.98dad1fe-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-glib2-2.66.1-2 is up to date -- reinstalling
warning: mingw-w64-x86_64-libusb-1.0.23-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-boost-1.74.0-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-python-3.8.6-3 is up to date -- reinstalling
warning: mingw-w64-x86_64-python-numpy-1.19.2-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-python-gobject-3.38.0-1 is up to date -- reinstalling
warning: mingw-w64-x86_64-python-setuptools-47.1.1-1 is up to date -- reinstalling
resolving dependencies...
looking for conflicting packages...

Packages (58) mingw-w64-x86_64-c-ares-1.16.1-1  mingw-w64-x86_64-confuse-3.2.2-1  mingw-w64-x86_64-curl-7.72.0-1  mingw-w64-x86_64-jansson-2.12-1
              mingw-w64-x86_64-jemalloc-5.2.1-1  mingw-w64-x86_64-jsoncpp-1.9.4-1  mingw-w64-x86_64-libarchive-3.4.3-1
              mingw-w64-x86_64-libmetalink-0.1.3-3  mingw-w64-x86_64-libpsl-0.21.1-1  mingw-w64-x86_64-libsigc++-2.10.4-1  mingw-w64-x86_64-libssh2-1.9.0-2
              mingw-w64-x86_64-libuv-1.40.0-1  mingw-w64-x86_64-lz4-1.9.2-1  mingw-w64-x86_64-nghttp2-1.41.0-1  mingw-w64-x86_64-rhash-1.3.9-1
              mingw-w64-x86_64-xapian-core-1~1.4.16-1  autoconf-2.69-5  autoconf-archive-2019.01.06-1  automake-wrapper-11-1  libtool-2.4.6-9  make-4.3-1
              mingw-w64-x86_64-binutils-2.35.1-2  mingw-w64-x86_64-boost-1.74.0-1  mingw-w64-x86_64-check-0.15.0-1  mingw-w64-x86_64-cmake-3.17.3-3
              mingw-w64-x86_64-crt-git-8.0.0.6001.98dad1fe-1  mingw-w64-x86_64-doxygen-1.8.18-1  mingw-w64-x86_64-gcc-10.2.0-4
              mingw-w64-x86_64-gcc-ada-10.2.0-4  mingw-w64-x86_64-gcc-fortran-10.2.0-4  mingw-w64-x86_64-gcc-libgfortran-10.2.0-4
              mingw-w64-x86_64-gcc-libs-10.2.0-4  mingw-w64-x86_64-gcc-objc-10.2.0-4  mingw-w64-x86_64-gdb-9.2-3  mingw-w64-x86_64-glib2-2.66.1-2
              mingw-w64-x86_64-glibmm-2.64.2-1  mingw-w64-x86_64-headers-git-8.0.0.6001.98dad1fe-1  mingw-w64-x86_64-hidapi-0.9.0-1
              mingw-w64-x86_64-libftdi-1.4-3  mingw-w64-x86_64-libmangle-git-8.0.0.6001.98dad1fe-1  mingw-w64-x86_64-libusb-1.0.23-1
              mingw-w64-x86_64-libwinpthread-git-8.0.0.6001.98dad1fe-3  mingw-w64-x86_64-libzip-1.7.3-1  mingw-w64-x86_64-make-4.3-1
              mingw-w64-x86_64-nsis-3.05-1  mingw-w64-x86_64-pkg-config-0.29.2-2  mingw-w64-x86_64-python-3.8.6-3  mingw-w64-x86_64-python-gobject-3.38.0-1
              mingw-w64-x86_64-python-numpy-1.19.2-1  mingw-w64-x86_64-python-setuptools-47.1.1-1  mingw-w64-x86_64-qt5-static-5.15.1-1
              mingw-w64-x86_64-swig-4.0.2-1  mingw-w64-x86_64-tools-git-8.0.0.6001.98dad1fe-1  mingw-w64-x86_64-winpthreads-git-8.0.0.6001.98dad1fe-3
              mingw-w64-x86_64-winstorecompat-git-8.0.0.6001.98dad1fe-1  patch-2.7.6-1  pkg-config-0.29.2-1  wget-1.20.3-1

Total Download Size:   1089.93 MiB
Total Installed Size:  7694.16 MiB
Net Upgrade Size:      6743.51 MiB

:: Proceed with installation? [Y/n]y
:: Retrieving packages...
 mingw-w64-x86_64-gcc-ada-10.2.0-4-any                             18.7 MiB  9.39 MiB/s 00:02 [######################################################] 100%
 mingw-w64-x86_64-gcc-objc-10.2.0-4-any                            11.3 MiB  6.59 MiB/s 00:02 [######################################################] 100%
 mingw-w64-x86_64-libsigc++-2.10.4-1-any                            3.2 MiB  12.0 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-glibmm-2.64.2-1-any                            1427.6 KiB  5.16 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-confuse-3.2.2-1-any                              84.7 KiB  3.94 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-libftdi-1.4-3-any                               139.3 KiB  3.32 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-check-0.15.0-1-any                              159.3 KiB   236 KiB/s 00:01 [######################################################] 100%
 mingw-w64-x86_64-libzip-1.7.3-1-any                              299.1 KiB   372 KiB/s 00:01 [######################################################] 100%
 mingw-w64-x86_64-xapian-core-1~1.4.16-1-any                        2.5 MiB  4.68 MiB/s 00:01 [######################################################] 100%
 mingw-w64-x86_64-doxygen-1.8.18-1-any                              5.3 MiB   341 KiB/s 00:16 [######################################################] 100%
 mingw-w64-x86_64-swig-4.0.2-1-any                               1091.5 KiB   342 KiB/s 00:03 [######################################################] 100%
 mingw-w64-x86_64-qt5-static-5.15.1-1-any                        1031.8 MiB  16.6 MiB/s 01:02 [######################################################] 100%
 mingw-w64-x86_64-c-ares-1.16.1-1-any                             182.1 KiB  3.35 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-libmetalink-0.1.3-3-any                          61.1 KiB   370 KiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-libpsl-0.21.1-1-any                              95.0 KiB  2.65 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-libssh2-1.9.0-2-any                             274.5 KiB   832 KiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-jansson-2.12-1-any                               65.8 KiB  3.38 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-jemalloc-5.2.1-1-any                            336.3 KiB   717 KiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-nghttp2-1.41.0-1-any                            221.9 KiB  3.10 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-curl-7.72.0-1-any                              1218.8 KiB  2.06 MiB/s 00:01 [######################################################] 100%
 mingw-w64-x86_64-jsoncpp-1.9.4-1-any                             240.6 KiB  2.64 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-lz4-1.9.2-1-any                                 171.0 KiB  3.27 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-libarchive-3.4.3-1-any                          742.6 KiB  2.46 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-libuv-1.40.0-1-any                              205.2 KiB  2.78 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-rhash-1.3.9-1-any                               209.1 KiB   823 KiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-cmake-3.17.3-3-any                                7.8 MiB  7.23 MiB/s 00:01 [######################################################] 100%
 mingw-w64-x86_64-nsis-3.05-1-any                                1426.9 KiB  3.85 MiB/s 00:00 [######################################################] 100%
 mingw-w64-x86_64-hidapi-0.9.0-1-any                               52.0 KiB  2.31 MiB/s 00:00 [######################################################] 100%
 autoconf-archive-2019.01.06-1-any                                550.8 KiB  5.78 MiB/s 00:00 [######################################################] 100%
 pkg-config-0.29.2-1-x86_64                                       185.7 KiB  1281 KiB/s 00:00 [######################################################] 100%
(58/58) checking keys in keyring                                                              [######################################################] 100%
(58/58) checking package integrity                                                            [######################################################] 100%
(58/58) loading package files                                                                 [######################################################] 100%
(58/58) checking for file conflicts                                                           [######################################################] 100%
(58/58) checking available disk space                                                         [######################################################] 100%
:: Processing package changes...
( 1/58) reinstalling autoconf                                                                 [######################################################] 100%
( 2/58) reinstalling automake-wrapper                                                         [######################################################] 100%
( 3/58) installing autoconf-archive                                                           [######################################################] 100%
( 4/58) reinstalling libtool                                                                  [######################################################] 100%
( 5/58) reinstalling make                                                                     [######################################################] 100%
( 6/58) installing pkg-config                                                                 [######################################################] 100%
( 7/58) reinstalling wget                                                                     [######################################################] 100%
( 8/58) reinstalling patch                                                                    [######################################################] 100%
( 9/58) reinstalling mingw-w64-x86_64-binutils                                                [######################################################] 100%
(10/58) reinstalling mingw-w64-x86_64-headers-git                                             [######################################################] 100%
(11/58) reinstalling mingw-w64-x86_64-crt-git                                                 [######################################################] 100%
(12/58) reinstalling mingw-w64-x86_64-libwinpthread-git                                       [######################################################] 100%
(13/58) reinstalling mingw-w64-x86_64-gcc-libs                                                [######################################################] 100%
(14/58) reinstalling mingw-w64-x86_64-winpthreads-git                                         [######################################################] 100%
(15/58) reinstalling mingw-w64-x86_64-gcc                                                     [######################################################] 100%
(16/58) installing mingw-w64-x86_64-gcc-ada                                                   [######################################################] 100%
(17/58) reinstalling mingw-w64-x86_64-gcc-libgfortran                                         [######################################################] 100%
(18/58) reinstalling mingw-w64-x86_64-gcc-fortran                                             [######################################################] 100%
(19/58) installing mingw-w64-x86_64-gcc-objc                                                  [######################################################] 100%
(20/58) reinstalling mingw-w64-x86_64-python                                                  [######################################################] 100%
(21/58) reinstalling mingw-w64-x86_64-gdb                                                     [######################################################] 100%
(22/58) reinstalling mingw-w64-x86_64-libmangle-git                                           [######################################################] 100%
(23/58) reinstalling mingw-w64-x86_64-make                                                    [######################################################] 100%
(24/58) reinstalling mingw-w64-x86_64-pkg-config                                              [######################################################] 100%
(25/58) reinstalling mingw-w64-x86_64-tools-git                                               [######################################################] 100%
(26/58) reinstalling mingw-w64-x86_64-winstorecompat-git                                      [######################################################] 100%
(27/58) reinstalling mingw-w64-x86_64-glib2                                                   [######################################################] 100%
/
(28/58) installing mingw-w64-x86_64-libsigc++                                                 [######################################################] 100%
(29/58) installing mingw-w64-x86_64-glibmm                                                    [######################################################] 100%
(30/58) reinstalling mingw-w64-x86_64-libusb                                                  [######################################################] 100%
(31/58) installing mingw-w64-x86_64-confuse                                                   [######################################################] 100%
(32/58) installing mingw-w64-x86_64-libftdi                                                   [######################################################] 100%
Optional dependencies for mingw-w64-x86_64-libftdi
    mingw-w64-x86_64-python3: Python3 bindings to libftdi [installed]
(33/58) installing mingw-w64-x86_64-check                                                     [######################################################] 100%
(34/58) reinstalling mingw-w64-x86_64-boost                                                   [######################################################] 100%
(35/58) installing mingw-w64-x86_64-libzip                                                    [######################################################] 100%
(36/58) installing mingw-w64-x86_64-xapian-core                                               [######################################################] 100%
(37/58) installing mingw-w64-x86_64-doxygen                                                   [######################################################] 100%
Optional dependencies for mingw-w64-x86_64-doxygen
    mingw-w64-x86_64-qt5 [installed]
(38/58) reinstalling mingw-w64-x86_64-python-numpy                                            [######################################################] 100%
(39/58) reinstalling mingw-w64-x86_64-python-gobject                                          [######################################################] 100%
(40/58) reinstalling mingw-w64-x86_64-python-setuptools                                       [######################################################] 100%
/
(41/58) installing mingw-w64-x86_64-swig                                                      [######################################################] 100%
(42/58) installing mingw-w64-x86_64-qt5-static                                                [######################################################] 100%

QtBinPatcher v2.2.0. Tool for patching paths in Qt binaries.
Yuri V. Krugloff, 2013-2015. http://www.tver-soft.org
This is free software released into the public domain.

Parsed command line options:
  force
  nobackup
  old-dir "@@QT_REAL_PREFIX/dir@@"
  verbose


Working directory: "C:/msys64/mingw64/qt5-static/bin".
Binary file location: "C:\msys64\mingw64\bin\qtbinpatcher.exe".
Path to "qmake.exe": "C:/msys64/mingw64/qt5-static/bin/".
Skipping backup of file "C:/msys64/mingw64/qt5-static/bin/qt.conf" - file not found.
qmake command line: ""C:/msys64/mingw64/qt5-static/bin/qmake.exe" -query".

>>>>>>>>>> BEGIN QMAKE OUTPUT >>>>>>>>>>
QT_SYSROOT:
QT_INSTALL_PREFIX:C:/msys64/mingw64/qt5-static
QT_INSTALL_ARCHDATA:C:/msys64/mingw64/qt5-static/share/qt5
QT_INSTALL_DATA:C:/msys64/mingw64/qt5-static/share/qt5
QT_INSTALL_DOCS:C:/msys64/mingw64/qt5-static/share/qt5/doc
QT_INSTALL_HEADERS:C:/msys64/mingw64/qt5-static/include
QT_INSTALL_LIBS:C:/msys64/mingw64/qt5-static/lib
QT_INSTALL_LIBEXECS:C:/msys64/mingw64/qt5-static/share/qt5/bin
QT_INSTALL_BINS:C:/msys64/mingw64/qt5-static/bin
QT_INSTALL_TESTS:C:/msys64/mingw64/qt5-static/share/qt5/tests
QT_INSTALL_PLUGINS:C:/msys64/mingw64/qt5-static/share/qt5/plugins
QT_INSTALL_IMPORTS:C:/msys64/mingw64/qt5-static/share/qt5/imports
QT_INSTALL_QML:C:/msys64/mingw64/qt5-static/share/qt5/qml
QT_INSTALL_TRANSLATIONS:C:/msys64/mingw64/qt5-static/share/qt5/translations
QT_INSTALL_CONFIGURATION:
QT_INSTALL_EXAMPLES:C:/msys64/mingw64/qt5-static/share/qt5/examples
QT_INSTALL_DEMOS:C:/msys64/mingw64/qt5-static/share/qt5/examples
QT_HOST_PREFIX:C:/msys64/mingw64/qt5-static
QT_HOST_DATA:C:/msys64/mingw64/qt5-static/share/qt5
QT_HOST_BINS:C:/msys64/mingw64/qt5-static/bin
QT_HOST_LIBS:C:/msys64/mingw64/qt5-static/lib
QMAKE_SPEC:win32-g++
QMAKE_XSPEC:win32-g++
QMAKE_VERSION:3.1
QT_VERSION:5.15.1
<<<<<<<<<<  END QMAKE OUTPUT  <<<<<<<<<<

Parsed qmake variables:
  QMAKE_SPEC = "win32-g++"
  QMAKE_VERSION = "3.1"
  QMAKE_XSPEC = "win32-g++"
  QT_HOST_BINS = "C:/msys64/mingw64/qt5-static/bin"
  QT_HOST_DATA = "C:/msys64/mingw64/qt5-static/share/qt5"
  QT_HOST_LIBS = "C:/msys64/mingw64/qt5-static/lib"
  QT_HOST_PREFIX = "C:/msys64/mingw64/qt5-static"
  QT_INSTALL_ARCHDATA = "C:/msys64/mingw64/qt5-static/share/qt5"
  QT_INSTALL_BINS = "C:/msys64/mingw64/qt5-static/bin"
  QT_INSTALL_CONFIGURATION = ""
  QT_INSTALL_DATA = "C:/msys64/mingw64/qt5-static/share/qt5"
  QT_INSTALL_DEMOS = "C:/msys64/mingw64/qt5-static/share/qt5/examples"
  QT_INSTALL_DOCS = "C:/msys64/mingw64/qt5-static/share/qt5/doc"
  QT_INSTALL_EXAMPLES = "C:/msys64/mingw64/qt5-static/share/qt5/examples"
  QT_INSTALL_HEADERS = "C:/msys64/mingw64/qt5-static/include"
  QT_INSTALL_IMPORTS = "C:/msys64/mingw64/qt5-static/share/qt5/imports"
  QT_INSTALL_LIBEXECS = "C:/msys64/mingw64/qt5-static/share/qt5/bin"
  QT_INSTALL_LIBS = "C:/msys64/mingw64/qt5-static/lib"
  QT_INSTALL_PLUGINS = "C:/msys64/mingw64/qt5-static/share/qt5/plugins"
  QT_INSTALL_PREFIX = "C:/msys64/mingw64/qt5-static"
  QT_INSTALL_QML = "C:/msys64/mingw64/qt5-static/share/qt5/qml"
  QT_INSTALL_TESTS = "C:/msys64/mingw64/qt5-static/share/qt5/tests"
  QT_INSTALL_TRANSLATIONS = "C:/msys64/mingw64/qt5-static/share/qt5/translations"
  QT_SYSROOT = ""
  QT_VERSION = "5.15.1"

Parsed Qt subdirs:
  QT_HOST_BINS = "bin"
  QT_HOST_DATA = "share/qt5"
  QT_HOST_LIBS = "lib"
  QT_INSTALL_ARCHDATA = "share/qt5"
  QT_INSTALL_BINS = "bin"
  QT_INSTALL_DATA = "share/qt5"
  QT_INSTALL_DEMOS = "share/qt5/examples"
  QT_INSTALL_DOCS = "share/qt5/doc"
  QT_INSTALL_EXAMPLES = "share/qt5/examples"
  QT_INSTALL_HEADERS = "include"
  QT_INSTALL_IMPORTS = "share/qt5/imports"
  QT_INSTALL_LIBEXECS = "share/qt5/bin"
  QT_INSTALL_LIBS = "lib"
  QT_INSTALL_PLUGINS = "share/qt5/plugins"
  QT_INSTALL_QML = "share/qt5/qml"
  QT_INSTALL_TESTS = "share/qt5/tests"
  QT_INSTALL_TRANSLATIONS = "share/qt5/translations"
Path to Qt directory: "C:/msys64/mingw64/qt5-static".
Path to new Qt directory: "C:/msys64/mingw64/qt5-static".
Skipping backup of files.

The new and the old pathes to Qt directory are the same.
Perform forced patching.


Patch values for text files:
  "@@QT_REAL_PREFIX/dir@@" -> "C:/msys64/mingw64/qt5-static"
  "@@QT_REAL_PREFIX\\dir@@" -> "C:\\msys64\\mingw64\\qt5-static"
  "@@QT_REAL_PREFIX\dir@@" -> "C:\msys64\mingw64\qt5-static"
  "C:/msys64/mingw64/qt5-static" -> "C:/msys64/mingw64/qt5-static"
  "C:\\msys64\\mingw64\\qt5-static" -> "C:\\msys64\\mingw64\\qt5-static"
  "C:\msys64\mingw64\qt5-static" -> "C:\msys64\mingw64\qt5-static"

Patch values for binary files:
  "qt_adatpath=" -> "qt_adatpath=C:/msys64/mingw64/qt5-static/share/qt5"
  "qt_binspath=" -> "qt_binspath=C:/msys64/mingw64/qt5-static/bin"
  "qt_datapath=" -> "qt_datapath=C:/msys64/mingw64/qt5-static/share/qt5"
  "qt_demopath=" -> "qt_demopath=C:/msys64/mingw64/qt5-static/share/qt5/examples"
  "qt_docspath=" -> "qt_docspath=C:/msys64/mingw64/qt5-static/share/qt5/doc"
  "qt_epfxpath=" -> "qt_epfxpath=C:/msys64/mingw64/qt5-static"
  "qt_hbinpath=" -> "qt_hbinpath=C:/msys64/mingw64/qt5-static/bin"
  "qt_hdatpath=" -> "qt_hdatpath=C:/msys64/mingw64/qt5-static/share/qt5"
  "qt_hdrspath=" -> "qt_hdrspath=C:/msys64/mingw64/qt5-static/include"
  "qt_hlibpath=" -> "qt_hlibpath=C:/msys64/mingw64/qt5-static/lib"
  "qt_hpfxpath=" -> "qt_hpfxpath=C:/msys64/mingw64/qt5-static"
  "qt_impspath=" -> "qt_impspath=C:/msys64/mingw64/qt5-static/share/qt5/imports"
  "qt_lbexpath=" -> "qt_lbexpath=C:/msys64/mingw64/qt5-static/share/qt5/bin"
  "qt_libspath=" -> "qt_libspath=C:/msys64/mingw64/qt5-static/lib"
  "qt_plugpath=" -> "qt_plugpath=C:/msys64/mingw64/qt5-static/share/qt5/plugins"
  "qt_prfxpath=" -> "qt_prfxpath=C:/msys64/mingw64/qt5-static"
  "qt_qml2path=" -> "qt_qml2path=C:/msys64/mingw64/qt5-static/share/qt5/qml"
  "qt_trnspath=" -> "qt_trnspath=C:/msys64/mingw64/qt5-static/share/qt5/translations"
  "qt_tstspath=" -> "qt_tstspath=C:/msys64/mingw64/qt5-static/share/qt5/tests"
  "qt_xmplpath=" -> "qt_xmplpath=C:/msys64/mingw64/qt5-static/share/qt5/examples"

List of text files for patch:
  C:/msys64/mingw64/qt5-static/lib/clip2tri.prl
  C:/msys64/mingw64/qt5-static/lib/clip2trid.prl
  C:/msys64/mingw64/qt5-static/lib/clipper.prl
  C:/msys64/mingw64/qt5-static/lib/clipperd.prl
  C:/msys64/mingw64/qt5-static/lib/poly2tri.prl
  C:/msys64/mingw64/qt5-static/lib/poly2trid.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DAnimation.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DAnimationd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DCore.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DCored.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DExtras.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DExtrasd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DInput.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DInputd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DLogic.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DLogicd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuick.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickAnimation.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickAnimationd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickExtras.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickExtrasd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickInput.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickInputd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickRender.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickRenderd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickScene2D.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DQuickScene2Dd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DRender.prl
  C:/msys64/mingw64/qt5-static/lib/Qt53DRenderd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5AccessibilitySupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5AccessibilitySupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5AxBase.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5AxBased.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5AxContainer.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5AxContainerd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5AxServer.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5AxServerd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Bluetooth.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Bluetoothd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Bodymovin.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Bodymovind.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Bootstrap.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Charts.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Chartsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Concurrent.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Concurrentd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Core.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Cored.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5DataVisualization.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5DataVisualizationd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5DBus.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5DBusd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Designer.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5DesignerComponents.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5DesignerComponentsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Designerd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5DeviceDiscoverySupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5DeviceDiscoverySupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5EdidSupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5EdidSupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5EventDispatcherSupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5EventDispatcherSupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5FbSupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5FbSupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5FontDatabaseSupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5FontDatabaseSupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Gamepad.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Gamepadd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Gui.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Guid.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Location.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Locationd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Multimedia.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Multimediad.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5MultimediaQuick.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5MultimediaQuickd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5MultimediaWidgets.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5MultimediaWidgetsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Network.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5NetworkAuth.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5NetworkAuthd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Networkd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Nfc.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Nfcd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5OpenGL.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5OpenGLd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5OpenGLExtensions.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5OpenGLExtensionsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5PacketProtocol.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5PacketProtocold.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5PlatformCompositorSupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5PlatformCompositorSupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Positioning.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Positioningd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5PositioningQuick.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5PositioningQuickd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5PrintSupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5PrintSupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Purchasing.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Purchasingd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Qml.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Qmld.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QmlDebug.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QmlDebugd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QmlDevTools.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QmlModels.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QmlModelsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QmlWorkerScript.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QmlWorkerScriptd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3D.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DAssetImport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DAssetImportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3Dd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DRender.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DRenderd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DRuntimeRender.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DRuntimeRenderd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DUtils.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DUtilsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickControls2.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickControls2d.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Quickd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickParticles.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickParticlesd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickShapes.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickShapesd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickTemplates2.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickTemplates2d.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickTest.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickTestd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickWidgets.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5QuickWidgetsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5RemoteObjects.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5RemoteObjectsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Script.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Scriptd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5ScriptTools.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5ScriptToolsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Scxml.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Scxmld.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Sensors.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Sensorsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5SerialBus.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5SerialBusd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5SerialPort.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5SerialPortd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Sql.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Sqld.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Svg.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Svgd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Test.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Testd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5TextToSpeech.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5TextToSpeechd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5ThemeSupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5ThemeSupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5UiTools.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5UiToolsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5VirtualKeyboard.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5VirtualKeyboardd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5VulkanSupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5VulkanSupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WebChannel.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WebChanneld.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WebSockets.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WebSocketsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WebView.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WebViewd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Widgets.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Widgetsd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WindowsUIAutomationSupport.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WindowsUIAutomationSupportd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WinExtras.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5WinExtrasd.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Xml.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5Xmld.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5XmlPatterns.prl
  C:/msys64/mingw64/qt5-static/lib/Qt5XmlPatternsd.prl
  C:/msys64/mingw64/qt5-static/lib/qtfreetype.prl
  C:/msys64/mingw64/qt5-static/lib/qtfreetyped.prl
  C:/msys64/mingw64/qt5-static/lib/qtharfbuzz.prl
  C:/msys64/mingw64/qt5-static/lib/qtharfbuzzd.prl
  C:/msys64/mingw64/qt5-static/lib/qtlibpng.prl
  C:/msys64/mingw64/qt5-static/lib/qtlibpngd.prl
  C:/msys64/mingw64/qt5-static/lib/qtmain.prl
  C:/msys64/mingw64/qt5-static/lib/qtmaind.prl
  C:/msys64/mingw64/qt5-static/lib/qtopenwnn.prl
  C:/msys64/mingw64/qt5-static/lib/qtopenwnnd.prl
  C:/msys64/mingw64/qt5-static/lib/qtpcre2.prl
  C:/msys64/mingw64/qt5-static/lib/qtpcre2d.prl
  C:/msys64/mingw64/qt5-static/lib/qtpinyin.prl
  C:/msys64/mingw64/qt5-static/lib/qtpinyind.prl
  C:/msys64/mingw64/qt5-static/lib/qttcime.prl
  C:/msys64/mingw64/qt5-static/lib/qttcimed.prl
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DAnimation.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DAnimationd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DCore.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DCored.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DExtras.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DExtrasd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DInput.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DInputd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DLogic.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DLogicd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuick.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickAnimation.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickAnimationd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickExtras.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickExtrasd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickInput.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickInputd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickRender.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickRenderd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickScene2D.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickScene2Dd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DRender.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DRenderd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxBase.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxBased.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxContainer.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxContainerd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxServer.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxServerd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Bluetooth.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Bluetoothd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Charts.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Chartsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Concurrent.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Concurrentd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Core.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Cored.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5DataVisualization.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5DataVisualizationd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5DBus.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5DBusd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Designer.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Designerd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Gamepad.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Gamepadd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Gui.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Guid.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Location.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Locationd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Multimedia.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Multimediad.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5MultimediaWidgets.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5MultimediaWidgetsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Network.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5NetworkAuth.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5NetworkAuthd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Networkd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Nfc.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Nfcd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5OpenGL.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5OpenGLd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5OpenGLExtensions.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5OpenGLExtensionsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Positioning.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Positioningd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5PositioningQuick.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5PositioningQuickd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5PrintSupport.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5PrintSupportd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Purchasing.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Purchasingd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Qml.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Qmld.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QmlModels.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QmlModelsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QmlWorkerScript.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QmlWorkerScriptd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3D.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DAssetImport.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DAssetImportd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3Dd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DRender.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DRenderd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DRuntimeRender.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DRuntimeRenderd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DUtils.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DUtilsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickControls2.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickControls2d.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quickd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickTemplates2.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickTemplates2d.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickTest.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickTestd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickWidgets.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickWidgetsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5RemoteObjects.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5RemoteObjectsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Script.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Scriptd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5ScriptTools.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5ScriptToolsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Scxml.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Scxmld.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Sensors.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Sensorsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5SerialBus.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5SerialBusd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5SerialPort.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5SerialPortd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Sql.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Sqld.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Svg.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Svgd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Test.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Testd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5TextToSpeech.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5TextToSpeechd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5UiTools.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5UiToolsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5VirtualKeyboard.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5VirtualKeyboardd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebChannel.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebChanneld.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebSockets.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebSocketsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebView.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebViewd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Widgets.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Widgetsd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WinExtras.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WinExtrasd.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Xml.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Xmld.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5XmlPatterns.pc
  C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5XmlPatternsd.pc
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/dbuscommon.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/repcclient.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/repccommon.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/repcmerged.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/repcserver.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3danimation.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3danimation_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dcore.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dcore_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dextras.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dextras_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dinput.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dinput_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dlogic.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dlogic_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquick.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickanimation.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickanimation_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickextras.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickextras_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickinput.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickinput_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickrender.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickrender_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickscene2d.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickscene2d_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquick_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3drender.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3drender_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_accessibility_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axbase.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axbase_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axcontainer.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axcontainer_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axserver.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axserver_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_bluetooth.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_bluetooth_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_bodymovin_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_bootstrap_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_charts.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_charts_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_concurrent.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_concurrent_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_core.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_core_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_datavisualization.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_datavisualization_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_dbus.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_dbus_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_designer.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_designercomponents_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_designer_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_devicediscovery_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_edid_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_eventdispatcher_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_fb_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_fontdatabase_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_gamepad.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_gamepad_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_gui.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_gui_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_location.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_location_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_multimedia.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_multimediawidgets.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_multimediawidgets_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_multimedia_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_network.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_networkauth.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_networkauth_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_network_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_nfc.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_nfc_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_opengl.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_openglextensions.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_openglextensions_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_opengl_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_packetprotocol_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_platformcompositor_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_positioning.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_positioningquick.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_positioningquick_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_positioning_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_printsupport.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_printsupport_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_purchasing.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_purchasing_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qml.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmldebug_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmldevtools_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmlmodels.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmlmodels_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmltest.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmltest_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmlworkerscript.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmlworkerscript_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qml_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3d.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3dassetimport.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3dassetimport_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3drender.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3drender_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3druntimerender.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3druntimerender_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3dutils.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3dutils_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3d_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickcontrols2.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickcontrols2_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickparticles_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickshapes_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quicktemplates2.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quicktemplates2_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickwidgets.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickwidgets_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_remoteobjects.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_remoteobjects_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_repparser.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_repparser_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_script.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_scripttools.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_scripttools_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_script_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_scxml.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_scxml_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_sensors.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_sensors_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_serialbus.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_serialbus_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_serialport.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_serialport_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_sql.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_sql_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_svg.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_svg_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_testlib.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_testlib_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_texttospeech.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_texttospeech_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_theme_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_uiplugin.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_uitools.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_uitools_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_virtualkeyboard.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_virtualkeyboard_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_vulkan_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_webchannel.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_webchannel_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_websockets.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_websockets_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_webview.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_webview_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_widgets.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_widgets_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_windowsuiautomation_support_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_winextras.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_winextras_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_xml.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_xmlpatterns.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_xmlpatterns_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_xml_private.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_assimp.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_assimpsceneimport.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_defaultgeometryloader.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_dsengine.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_gltfgeometryloader.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_gltfsceneexport.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_gltfsceneimport.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_openglrenderer.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qdirect2d.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qgenericbearer.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qgif.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qicns.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qico.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qjpeg.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qminimal.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_debugger.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_inspector.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_local.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_messages.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_native.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_nativedebugger.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_preview.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_profiler.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_quickprofiler.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_server.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_tcp.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qoffscreen.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qsqlite.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qsvg.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qsvgicon.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtaudio_windows.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtexttospeech_sapi.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtga.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_esri.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_itemsoverlay.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_mapbox.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_nokia.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_osm.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtiff.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtmedia_audioengine.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtmultimedia_m3u.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtpassthrucanbus.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtpeakcanbus.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtposition_positionpoll.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtposition_serialnmea.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtsensorgestures_plugin.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtsensorgestures_shakeplugin.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtsensors_generic.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtsysteccanbus.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qttinycanbus.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtuiotouchplugin.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvectorcanbus.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualcanbus.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboardplugin.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_hangul.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_openwnn.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_pinyin.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_tcime.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_thai.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwbmp.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwebgl.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwebp.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwindows.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwindowsvistastyle.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_scene2d.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_uip.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_windowsprintersupport.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_xinputgamepad.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/qconfig.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/qdevice.pri
  C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/qmodule.pri
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/assetimporters/assimp.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/assetimporters/assimpd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/assetimporters/uip.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/assetimporters/uipd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/audio/qtaudio_windows.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/audio/qtaudio_windowsd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/bearer/qgenericbearer.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/bearer/qgenericbearerd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtpassthrucanbus.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtpassthrucanbusd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtpeakcanbus.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtpeakcanbusd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtsysteccanbus.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtsysteccanbusd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qttinycanbus.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qttinycanbusd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtvectorcanbus.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtvectorcanbusd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtvirtualcanbus.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtvirtualcanbusd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/gamepads/xinputgamepad.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/gamepads/xinputgamepadd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/generic/qtuiotouchplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/generic/qtuiotouchplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geometryloaders/defaultgeometryloader.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geometryloaders/defaultgeometryloaderd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geometryloaders/gltfgeometryloader.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geometryloaders/gltfgeometryloaderd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_esri.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_esrid.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_itemsoverlay.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_itemsoverlayd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_mapbox.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_mapboxd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_nokia.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_nokiad.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_osm.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_osmd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/iconengines/qsvgicon.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/iconengines/qsvgicond.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qgif.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qgifd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qicns.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qicnsd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qico.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qicod.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qjpeg.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qjpegd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qsvg.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qsvgd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qtga.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qtgad.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qtiff.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qtiffd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qwbmp.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qwbmpd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qwebp.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qwebpd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/mediaservice/dsengine.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/mediaservice/dsengined.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/mediaservice/qtmedia_audioengine.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/mediaservice/qtmedia_audioengined.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforminputcontexts/qtvirtualkeyboardplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforminputcontexts/qtvirtualkeyboardplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qdirect2d.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qdirect2dd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qminimal.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qminimald.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qoffscreen.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qoffscreend.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qwebgl.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qwebgld.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qwindows.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qwindowsd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/playlistformats/qtmultimedia_m3u.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/playlistformats/qtmultimedia_m3ud.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/position/qtposition_positionpoll.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/position/qtposition_positionpolld.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/position/qtposition_serialnmea.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/position/qtposition_serialnmead.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/printsupport/windowsprintersupport.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/printsupport/windowsprintersupportd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_debugger.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_debuggerd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_inspector.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_inspectord.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_local.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_locald.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_messages.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_messagesd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_native.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_natived.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_nativedebugger.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_nativedebuggerd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_preview.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_previewd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_profiler.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_profilerd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_quickprofiler.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_quickprofilerd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_server.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_serverd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_tcp.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_tcpd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/renderers/openglrenderer.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/renderers/openglrendererd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/renderplugins/scene2d.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/renderplugins/scene2dd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/assimpsceneimport.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/assimpsceneimportd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/gltfsceneexport.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/gltfsceneexportd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/gltfsceneimport.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/gltfsceneimportd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensorgestures/qtsensorgestures_plugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensorgestures/qtsensorgestures_plugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensorgestures/qtsensorgestures_shakeplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensorgestures/qtsensorgestures_shakeplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensors/qtsensors_generic.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensors/qtsensors_genericd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sqldrivers/qsqlite.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/sqldrivers/qsqlited.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/styles/qwindowsvistastyle.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/styles/qwindowsvistastyled.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/texttospeech/qtexttospeech_sapi.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/texttospeech/qtexttospeech_sapid.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_hangul.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_hanguld.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_openwnn.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_openwnnd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_pinyin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_pinyind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_tcime.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_tcimed.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_thai.prl
  C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_thaid.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/animation/labsanimationplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/animation/labsanimationplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/calendar/qtlabscalendarplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/calendar/qtlabscalendarplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/folderlistmodel/qmlfolderlistmodelplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/folderlistmodel/qmlfolderlistmodelplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/location/locationlabsplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/location/locationlabsplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/lottieqt/lottieqtplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/lottieqt/lottieqtplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/platform/qtlabsplatformplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/platform/qtlabsplatformplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/qmlmodels/labsmodelsplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/qmlmodels/labsmodelsplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/settings/qmlsettingsplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/settings/qmlsettingsplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/sharedimage/sharedimageplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/sharedimage/sharedimageplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/wavefrontmesh/qmlwavefrontmeshplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/wavefrontmesh/qmlwavefrontmeshplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Animation/quick3danimationplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Animation/quick3danimationplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Core/quick3dcoreplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Core/quick3dcoreplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Extras/quick3dextrasplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Extras/quick3dextrasplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Input/quick3dinputplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Input/quick3dinputplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Logic/quick3dlogicplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Logic/quick3dlogicplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Render/quick3drenderplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Render/quick3drenderplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtAudioEngine/declarative_audioengine.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtAudioEngine/declarative_audioengined.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtBluetooth/declarative_bluetooth.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtBluetooth/declarative_bluetoothd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtCharts/qtchartsqml2.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtCharts/qtchartsqml2d.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtDataVisualization/datavisualizationqml2.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtDataVisualization/datavisualizationqml2d.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGamepad/declarative_gamepad.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGamepad/declarative_gamepadd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGraphicalEffects/private/qtgraphicaleffectsprivate.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGraphicalEffects/private/qtgraphicaleffectsprivated.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGraphicalEffects/qtgraphicaleffectsplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGraphicalEffects/qtgraphicaleffectsplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtLocation/declarative_location.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtLocation/declarative_locationd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtMultimedia/declarative_multimedia.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtMultimedia/declarative_multimediad.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtNfc/declarative_nfc.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtNfc/declarative_nfcd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtPositioning/declarative_positioning.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtPositioning/declarative_positioningd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtPurchasing/declarative_purchasing.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtPurchasing/declarative_purchasingd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/Models.2/modelsplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/Models.2/modelsplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/RemoteObjects/qtqmlremoteobjects.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/RemoteObjects/qtqmlremoteobjectsd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/StateMachine/qtqmlstatemachine.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/StateMachine/qtqmlstatemachined.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/WorkerScript.2/workerscriptplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/WorkerScript.2/workerscriptplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/qmlplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/qmlplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls/Styles/Flat/qtquickextrasflatplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls/Styles/Flat/qtquickextrasflatplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls/qtquickcontrolsplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls/qtquickcontrolsplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Fusion/qtquickcontrols2fusionstyleplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Fusion/qtquickcontrols2fusionstyleplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Imagine/qtquickcontrols2imaginestyleplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Imagine/qtquickcontrols2imaginestyleplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Material/qtquickcontrols2materialstyleplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Material/qtquickcontrols2materialstyleplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Universal/qtquickcontrols2universalstyleplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Universal/qtquickcontrols2universalstyleplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/qtquickcontrols2plugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/qtquickcontrols2plugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Dialogs/Private/dialogsprivateplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Dialogs/Private/dialogsprivateplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Dialogs/dialogplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Dialogs/dialogplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Extras/qtquickextrasplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Extras/qtquickextrasplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Layouts/qquicklayoutsplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Layouts/qquicklayoutsplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/LocalStorage/qmllocalstorageplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/LocalStorage/qmllocalstorageplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Particles.2/particlesplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Particles.2/particlesplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/PrivateWidgets/widgetsplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/PrivateWidgets/widgetsplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Scene2D/qtquickscene2dplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Scene2D/qtquickscene2dplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Scene3D/qtquickscene3dplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Scene3D/qtquickscene3dplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Shapes/qmlshapesplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Shapes/qmlshapesplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Templates.2/qtquicktemplates2plugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Templates.2/qtquicktemplates2plugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Timeline/qtquicktimelineplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Timeline/qtquicktimelineplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/Settings/qtquickvirtualkeyboardsettingsplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/Settings/qtquickvirtualkeyboardsettingsplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/Styles/qtquickvirtualkeyboardstylesplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/Styles/qtquickvirtualkeyboardstylesplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/qtquickvirtualkeyboardplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/qtquickvirtualkeyboardplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Window.2/windowplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Window.2/windowplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/XmlListModel/qmlxmllistmodelplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/XmlListModel/qmlxmllistmodelplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick.2/qtquick2plugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick.2/qtquick2plugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Effects/qtquick3deffectplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Effects/qtquick3deffectplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Helpers/qtquick3dhelpersplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Helpers/qtquick3dhelpersplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Materials/qtquick3dmaterialplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Materials/qtquick3dmaterialplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/qquick3dplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/qquick3dplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtRemoteObjects/qtremoteobjects.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtRemoteObjects/qtremoteobjectsd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtScxml/declarative_scxml.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtScxml/declarative_scxmld.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtSensors/declarative_sensors.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtSensors/declarative_sensorsd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtTest/qmltestplugin.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtTest/qmltestplugind.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebChannel/declarative_webchannel.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebChannel/declarative_webchanneld.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebSockets/declarative_qmlwebsockets.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebSockets/declarative_qmlwebsocketsd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebView/declarative_webview.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebView/declarative_webviewd.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWinExtras/qml_winextras.prl
  C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWinExtras/qml_winextrasd.prl
  C:/msys64/mingw64/qt5-static/lib/cmake/Qt5Gui/Qt5GuiConfigExtras.cmake
  C:/msys64/mingw64/qt5-static/lib/cmake/Qt5LinguistTools/Qt5LinguistToolsConfig.cmake


List of binary files for patch:
  C:/msys64/mingw64/qt5-static/bin/qmake.exe
  C:/msys64/mingw64/qt5-static/bin/lrelease.exe

Patching text file "C:/msys64/mingw64/qt5-static/lib/clip2tri.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/clip2trid.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/clipper.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/clipperd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/poly2tri.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/poly2trid.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DAnimation.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DAnimationd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DCore.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DCored.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DExtras.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DExtrasd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DInput.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DInputd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DLogic.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DLogicd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuick.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickAnimation.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickAnimationd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickExtras.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickExtrasd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickInput.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickInputd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickRender.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickRenderd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickScene2D.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DQuickScene2Dd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DRender.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt53DRenderd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5AccessibilitySupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5AccessibilitySupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5AxBase.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5AxBased.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5AxContainer.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5AxContainerd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5AxServer.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5AxServerd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Bluetooth.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Bluetoothd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Bodymovin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Bodymovind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Bootstrap.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Charts.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Chartsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Concurrent.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Concurrentd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Core.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Cored.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5DataVisualization.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5DataVisualizationd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5DBus.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5DBusd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Designer.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5DesignerComponents.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5DesignerComponentsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Designerd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5DeviceDiscoverySupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5DeviceDiscoverySupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5EdidSupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5EdidSupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5EventDispatcherSupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5EventDispatcherSupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5FbSupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5FbSupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5FontDatabaseSupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5FontDatabaseSupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Gamepad.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Gamepadd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Gui.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Guid.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Location.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Locationd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Multimedia.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Multimediad.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5MultimediaQuick.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5MultimediaQuickd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5MultimediaWidgets.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5MultimediaWidgetsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Network.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5NetworkAuth.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5NetworkAuthd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Networkd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Nfc.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Nfcd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5OpenGL.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5OpenGLd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5OpenGLExtensions.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5OpenGLExtensionsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5PacketProtocol.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5PacketProtocold.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5PlatformCompositorSupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5PlatformCompositorSupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Positioning.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Positioningd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5PositioningQuick.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5PositioningQuickd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5PrintSupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5PrintSupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Purchasing.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Purchasingd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Qml.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Qmld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QmlDebug.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QmlDebugd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QmlDevTools.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QmlModels.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QmlModelsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QmlWorkerScript.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QmlWorkerScriptd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3D.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DAssetImport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DAssetImportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3Dd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DRender.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DRenderd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DRuntimeRender.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DRuntimeRenderd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DUtils.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quick3DUtilsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickControls2.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickControls2d.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Quickd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickParticles.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickParticlesd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickShapes.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickShapesd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickTemplates2.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickTemplates2d.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickTest.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickTestd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickWidgets.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5QuickWidgetsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5RemoteObjects.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5RemoteObjectsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Script.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Scriptd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5ScriptTools.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5ScriptToolsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Scxml.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Scxmld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Sensors.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Sensorsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5SerialBus.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5SerialBusd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5SerialPort.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5SerialPortd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Sql.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Sqld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Svg.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Svgd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Test.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Testd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5TextToSpeech.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5TextToSpeechd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5ThemeSupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5ThemeSupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5UiTools.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5UiToolsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5VirtualKeyboard.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5VirtualKeyboardd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5VulkanSupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5VulkanSupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WebChannel.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WebChanneld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WebSockets.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WebSocketsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WebView.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WebViewd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Widgets.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Widgetsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WindowsUIAutomationSupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WindowsUIAutomationSupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WinExtras.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5WinExtrasd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Xml.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5Xmld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5XmlPatterns.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/Qt5XmlPatternsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtfreetype.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtfreetyped.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtharfbuzz.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtharfbuzzd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtlibpng.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtlibpngd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtmain.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtmaind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtopenwnn.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtopenwnnd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtpcre2.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtpcre2d.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtpinyin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qtpinyind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qttcime.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/qttcimed.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DAnimation.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DAnimationd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DCore.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DCored.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DExtras.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DExtrasd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DInput.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DInputd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DLogic.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DLogicd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuick.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickAnimation.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickAnimationd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickExtras.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickExtrasd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickInput.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickInputd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickRender.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickRenderd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickScene2D.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DQuickScene2Dd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DRender.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt53DRenderd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxBase.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxBased.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxContainer.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxContainerd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxServer.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5AxServerd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Bluetooth.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Bluetoothd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Charts.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Chartsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Concurrent.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Concurrentd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Core.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Cored.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5DataVisualization.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5DataVisualizationd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5DBus.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5DBusd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Designer.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Designerd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Gamepad.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Gamepadd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Gui.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Guid.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Location.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Locationd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Multimedia.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Multimediad.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5MultimediaWidgets.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5MultimediaWidgetsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Network.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5NetworkAuth.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5NetworkAuthd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Networkd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Nfc.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Nfcd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5OpenGL.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5OpenGLd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5OpenGLExtensions.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5OpenGLExtensionsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Positioning.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Positioningd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5PositioningQuick.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5PositioningQuickd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5PrintSupport.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5PrintSupportd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Purchasing.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Purchasingd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Qml.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Qmld.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QmlModels.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QmlModelsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QmlWorkerScript.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QmlWorkerScriptd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3D.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DAssetImport.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DAssetImportd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3Dd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DRender.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DRenderd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DRuntimeRender.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DRuntimeRenderd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DUtils.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quick3DUtilsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickControls2.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickControls2d.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Quickd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickTemplates2.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickTemplates2d.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickTest.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickTestd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickWidgets.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5QuickWidgetsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5RemoteObjects.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5RemoteObjectsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Script.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Scriptd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5ScriptTools.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5ScriptToolsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Scxml.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Scxmld.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Sensors.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Sensorsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5SerialBus.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5SerialBusd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5SerialPort.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5SerialPortd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Sql.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Sqld.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Svg.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Svgd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Test.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Testd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5TextToSpeech.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5TextToSpeechd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5UiTools.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5UiToolsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5VirtualKeyboard.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5VirtualKeyboardd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebChannel.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebChanneld.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebSockets.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebSocketsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebView.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WebViewd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Widgets.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Widgetsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WinExtras.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5WinExtrasd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Xml.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5Xmld.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5XmlPatterns.pc".
Patching text file "C:/msys64/mingw64/qt5-static/lib/pkgconfig/Qt5XmlPatternsd.pc".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/dbuscommon.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/repcclient.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/repccommon.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/repcmerged.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/features/repcserver.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3danimation.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3danimation_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dcore.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dcore_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dextras.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dextras_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dinput.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dinput_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dlogic.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dlogic_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquick.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickanimation.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickanimation_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickextras.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickextras_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickinput.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickinput_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickrender.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickrender_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickscene2d.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquickscene2d_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3dquick_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3drender.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_3drender_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_accessibility_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axbase.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axbase_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axcontainer.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axcontainer_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axserver.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_axserver_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_bluetooth.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_bluetooth_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_bodymovin_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_bootstrap_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_charts.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_charts_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_concurrent.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_concurrent_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_core.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_core_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_datavisualization.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_datavisualization_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_dbus.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_dbus_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_designer.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_designercomponents_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_designer_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_devicediscovery_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_edid_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_eventdispatcher_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_fb_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_fontdatabase_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_gamepad.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_gamepad_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_gui.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_gui_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_location.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_location_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_multimedia.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_multimediawidgets.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_multimediawidgets_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_multimedia_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_network.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_networkauth.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_networkauth_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_network_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_nfc.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_nfc_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_opengl.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_openglextensions.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_openglextensions_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_opengl_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_packetprotocol_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_platformcompositor_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_positioning.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_positioningquick.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_positioningquick_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_positioning_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_printsupport.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_printsupport_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_purchasing.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_purchasing_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qml.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmldebug_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmldevtools_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmlmodels.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmlmodels_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmltest.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmltest_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmlworkerscript.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qmlworkerscript_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qml_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3d.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3dassetimport.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3dassetimport_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3drender.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3drender_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3druntimerender.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3druntimerender_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3dutils.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3dutils_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick3d_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickcontrols2.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickcontrols2_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickparticles_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickshapes_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quicktemplates2.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quicktemplates2_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickwidgets.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quickwidgets_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_quick_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_remoteobjects.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_remoteobjects_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_repparser.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_repparser_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_script.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_scripttools.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_scripttools_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_script_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_scxml.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_scxml_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_sensors.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_sensors_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_serialbus.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_serialbus_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_serialport.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_serialport_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_sql.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_sql_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_svg.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_svg_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_testlib.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_testlib_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_texttospeech.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_texttospeech_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_theme_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_uiplugin.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_uitools.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_uitools_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_virtualkeyboard.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_virtualkeyboard_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_vulkan_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_webchannel.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_webchannel_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_websockets.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_websockets_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_webview.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_webview_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_widgets.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_widgets_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_windowsuiautomation_support_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_winextras.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_winextras_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_xml.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_xmlpatterns.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_xmlpatterns_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_lib_xml_private.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_assimp.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_assimpsceneimport.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_defaultgeometryloader.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_dsengine.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_gltfgeometryloader.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_gltfsceneexport.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_gltfsceneimport.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_openglrenderer.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qdirect2d.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qgenericbearer.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qgif.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qicns.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qico.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qjpeg.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qminimal.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_debugger.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_inspector.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_local.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_messages.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_native.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_nativedebugger.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_preview.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_profiler.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_quickprofiler.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_server.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qmldbg_tcp.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qoffscreen.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qsqlite.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qsvg.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qsvgicon.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtaudio_windows.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtexttospeech_sapi.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtga.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_esri.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_itemsoverlay.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_mapbox.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_nokia.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtgeoservices_osm.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtiff.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtmedia_audioengine.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtmultimedia_m3u.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtpassthrucanbus.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtpeakcanbus.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtposition_positionpoll.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtposition_serialnmea.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtsensorgestures_plugin.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtsensorgestures_shakeplugin.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtsensors_generic.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtsysteccanbus.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qttinycanbus.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtuiotouchplugin.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvectorcanbus.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualcanbus.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboardplugin.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_hangul.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_openwnn.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_pinyin.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_tcime.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qtvirtualkeyboard_thai.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwbmp.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwebgl.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwebp.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwindows.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_qwindowsvistastyle.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_scene2d.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_uip.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_windowsprintersupport.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/modules/qt_plugin_xinputgamepad.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/qconfig.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/qdevice.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/mkspecs/qmodule.pri".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/assetimporters/assimp.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/assetimporters/assimpd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/assetimporters/uip.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/assetimporters/uipd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/audio/qtaudio_windows.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/audio/qtaudio_windowsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/bearer/qgenericbearer.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/bearer/qgenericbearerd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtpassthrucanbus.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtpassthrucanbusd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtpeakcanbus.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtpeakcanbusd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtsysteccanbus.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtsysteccanbusd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qttinycanbus.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qttinycanbusd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtvectorcanbus.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtvectorcanbusd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtvirtualcanbus.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/canbus/qtvirtualcanbusd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/gamepads/xinputgamepad.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/gamepads/xinputgamepadd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/generic/qtuiotouchplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/generic/qtuiotouchplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geometryloaders/defaultgeometryloader.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geometryloaders/defaultgeometryloaderd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geometryloaders/gltfgeometryloader.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geometryloaders/gltfgeometryloaderd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_esri.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_esrid.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_itemsoverlay.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_itemsoverlayd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_mapbox.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_mapboxd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_nokia.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_nokiad.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_osm.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/geoservices/qtgeoservices_osmd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/iconengines/qsvgicon.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/iconengines/qsvgicond.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qgif.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qgifd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qicns.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qicnsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qico.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qicod.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qjpeg.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qjpegd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qsvg.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qsvgd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qtga.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qtgad.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qtiff.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qtiffd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qwbmp.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qwbmpd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qwebp.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/qwebpd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/mediaservice/dsengine.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/mediaservice/dsengined.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/mediaservice/qtmedia_audioengine.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/mediaservice/qtmedia_audioengined.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforminputcontexts/qtvirtualkeyboardplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforminputcontexts/qtvirtualkeyboardplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qdirect2d.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qdirect2dd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qminimal.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qminimald.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qoffscreen.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qoffscreend.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qwebgl.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qwebgld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qwindows.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/qwindowsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/playlistformats/qtmultimedia_m3u.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/playlistformats/qtmultimedia_m3ud.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/position/qtposition_positionpoll.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/position/qtposition_positionpolld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/position/qtposition_serialnmea.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/position/qtposition_serialnmead.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/printsupport/windowsprintersupport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/printsupport/windowsprintersupportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_debugger.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_debuggerd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_inspector.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_inspectord.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_local.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_locald.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_messages.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_messagesd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_native.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_natived.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_nativedebugger.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_nativedebuggerd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_preview.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_previewd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_profiler.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_profilerd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_quickprofiler.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_quickprofilerd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_server.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_serverd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_tcp.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/qmltooling/qmldbg_tcpd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/renderers/openglrenderer.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/renderers/openglrendererd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/renderplugins/scene2d.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/renderplugins/scene2dd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/assimpsceneimport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/assimpsceneimportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/gltfsceneexport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/gltfsceneexportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/gltfsceneimport.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sceneparsers/gltfsceneimportd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensorgestures/qtsensorgestures_plugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensorgestures/qtsensorgestures_plugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensorgestures/qtsensorgestures_shakeplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensorgestures/qtsensorgestures_shakeplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensors/qtsensors_generic.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sensors/qtsensors_genericd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sqldrivers/qsqlite.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/sqldrivers/qsqlited.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/styles/qwindowsvistastyle.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/styles/qwindowsvistastyled.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/texttospeech/qtexttospeech_sapi.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/texttospeech/qtexttospeech_sapid.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_hangul.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_hanguld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_openwnn.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_openwnnd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_pinyin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_pinyind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_tcime.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_tcimed.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_thai.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/plugins/virtualkeyboard/qtvirtualkeyboard_thaid.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/animation/labsanimationplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/animation/labsanimationplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/calendar/qtlabscalendarplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/calendar/qtlabscalendarplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/folderlistmodel/qmlfolderlistmodelplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/folderlistmodel/qmlfolderlistmodelplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/location/locationlabsplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/location/locationlabsplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/lottieqt/lottieqtplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/lottieqt/lottieqtplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/platform/qtlabsplatformplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/platform/qtlabsplatformplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/qmlmodels/labsmodelsplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/qmlmodels/labsmodelsplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/settings/qmlsettingsplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/settings/qmlsettingsplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/sharedimage/sharedimageplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/sharedimage/sharedimageplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/wavefrontmesh/qmlwavefrontmeshplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt/labs/wavefrontmesh/qmlwavefrontmeshplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Animation/quick3danimationplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Animation/quick3danimationplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Core/quick3dcoreplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Core/quick3dcoreplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Extras/quick3dextrasplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Extras/quick3dextrasplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Input/quick3dinputplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Input/quick3dinputplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Logic/quick3dlogicplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Logic/quick3dlogicplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Render/quick3drenderplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/Qt3D/Render/quick3drenderplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtAudioEngine/declarative_audioengine.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtAudioEngine/declarative_audioengined.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtBluetooth/declarative_bluetooth.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtBluetooth/declarative_bluetoothd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtCharts/qtchartsqml2.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtCharts/qtchartsqml2d.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtDataVisualization/datavisualizationqml2.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtDataVisualization/datavisualizationqml2d.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGamepad/declarative_gamepad.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGamepad/declarative_gamepadd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGraphicalEffects/private/qtgraphicaleffectsprivate.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGraphicalEffects/private/qtgraphicaleffectsprivated.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGraphicalEffects/qtgraphicaleffectsplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtGraphicalEffects/qtgraphicaleffectsplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtLocation/declarative_location.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtLocation/declarative_locationd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtMultimedia/declarative_multimedia.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtMultimedia/declarative_multimediad.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtNfc/declarative_nfc.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtNfc/declarative_nfcd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtPositioning/declarative_positioning.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtPositioning/declarative_positioningd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtPurchasing/declarative_purchasing.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtPurchasing/declarative_purchasingd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/Models.2/modelsplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/Models.2/modelsplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/RemoteObjects/qtqmlremoteobjects.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/RemoteObjects/qtqmlremoteobjectsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/StateMachine/qtqmlstatemachine.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/StateMachine/qtqmlstatemachined.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/WorkerScript.2/workerscriptplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/WorkerScript.2/workerscriptplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/qmlplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQml/qmlplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls/Styles/Flat/qtquickextrasflatplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls/Styles/Flat/qtquickextrasflatplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls/qtquickcontrolsplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls/qtquickcontrolsplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Fusion/qtquickcontrols2fusionstyleplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Fusion/qtquickcontrols2fusionstyleplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Imagine/qtquickcontrols2imaginestyleplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Imagine/qtquickcontrols2imaginestyleplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Material/qtquickcontrols2materialstyleplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Material/qtquickcontrols2materialstyleplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Universal/qtquickcontrols2universalstyleplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/Universal/qtquickcontrols2universalstyleplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/qtquickcontrols2plugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Controls.2/qtquickcontrols2plugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Dialogs/Private/dialogsprivateplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Dialogs/Private/dialogsprivateplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Dialogs/dialogplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Dialogs/dialogplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Extras/qtquickextrasplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Extras/qtquickextrasplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Layouts/qquicklayoutsplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Layouts/qquicklayoutsplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/LocalStorage/qmllocalstorageplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/LocalStorage/qmllocalstorageplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Particles.2/particlesplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Particles.2/particlesplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/PrivateWidgets/widgetsplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/PrivateWidgets/widgetsplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Scene2D/qtquickscene2dplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Scene2D/qtquickscene2dplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Scene3D/qtquickscene3dplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Scene3D/qtquickscene3dplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Shapes/qmlshapesplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Shapes/qmlshapesplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Templates.2/qtquicktemplates2plugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Templates.2/qtquicktemplates2plugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Timeline/qtquicktimelineplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Timeline/qtquicktimelineplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/Settings/qtquickvirtualkeyboardsettingsplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/Settings/qtquickvirtualkeyboardsettingsplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/Styles/qtquickvirtualkeyboardstylesplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/Styles/qtquickvirtualkeyboardstylesplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/qtquickvirtualkeyboardplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/VirtualKeyboard/qtquickvirtualkeyboardplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Window.2/windowplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/Window.2/windowplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/XmlListModel/qmlxmllistmodelplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick/XmlListModel/qmlxmllistmodelplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick.2/qtquick2plugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick.2/qtquick2plugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Effects/qtquick3deffectplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Effects/qtquick3deffectplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Helpers/qtquick3dhelpersplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Helpers/qtquick3dhelpersplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Materials/qtquick3dmaterialplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/Materials/qtquick3dmaterialplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/qquick3dplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtQuick3D/qquick3dplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtRemoteObjects/qtremoteobjects.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtRemoteObjects/qtremoteobjectsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtScxml/declarative_scxml.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtScxml/declarative_scxmld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtSensors/declarative_sensors.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtSensors/declarative_sensorsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtTest/qmltestplugin.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtTest/qmltestplugind.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebChannel/declarative_webchannel.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebChannel/declarative_webchanneld.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebSockets/declarative_qmlwebsockets.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebSockets/declarative_qmlwebsocketsd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebView/declarative_webview.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWebView/declarative_webviewd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWinExtras/qml_winextras.prl".
Patching text file "C:/msys64/mingw64/qt5-static/share/qt5/qml/QtWinExtras/qml_winextrasd.prl".
Patching text file "C:/msys64/mingw64/qt5-static/lib/cmake/Qt5Gui/Qt5GuiConfigExtras.cmake".
Patching text file "C:/msys64/mingw64/qt5-static/lib/cmake/Qt5LinguistTools/Qt5LinguistToolsConfig.cmake".
Patching binary file "C:/msys64/mingw64/qt5-static/bin/qmake.exe".
Patching binary file "C:/msys64/mingw64/qt5-static/bin/lrelease.exe".
/
(43/58) installing mingw-w64-x86_64-c-ares                                                    [######################################################] 100%
(44/58) installing mingw-w64-x86_64-libmetalink                                               [######################################################] 100%
(45/58) installing mingw-w64-x86_64-libpsl                                                    [######################################################] 100%
(46/58) installing mingw-w64-x86_64-libssh2                                                   [######################################################] 100%
(47/58) installing mingw-w64-x86_64-jansson                                                   [######################################################] 100%
(48/58) installing mingw-w64-x86_64-jemalloc                                                  [######################################################] 100%
(49/58) installing mingw-w64-x86_64-nghttp2                                                   [######################################################] 100%
(50/58) installing mingw-w64-x86_64-curl                                                      [######################################################] 100%
(51/58) installing mingw-w64-x86_64-jsoncpp                                                   [######################################################] 100%
(52/58) installing mingw-w64-x86_64-lz4                                                       [######################################################] 100%
(53/58) installing mingw-w64-x86_64-libarchive                                                [######################################################] 100%
(54/58) installing mingw-w64-x86_64-libuv                                                     [######################################################] 100%
(55/58) installing mingw-w64-x86_64-rhash                                                     [######################################################] 100%
(56/58) installing mingw-w64-x86_64-cmake                                                     [######################################################] 100%
Optional dependencies for mingw-w64-x86_64-cmake
    mingw-w64-x86_64-qt5: CMake Qt GUI [installed]
    mingw-w64-x86_64-emacs: for cmake emacs mode
(57/58) installing mingw-w64-x86_64-nsis                                                      [######################################################] 100%
(58/58) installing mingw-w64-x86_64-hidapi                                                    [######################################################] 100%
:: Running post-transaction hooks...
(1/1) Updating the info directory file...
```

Ok, now, let's edit the script, to try enable the python bindings:

```
sed -i -b 's/# V="V=1 VERBOSE=1"/V="V=1 VERBOSE=1"/' ./cross-compile/msys2/sigrok-native-msys2
sed -i -b 's/DEBUG=0/DEBUG=1/' ./cross-compile/msys2/sigrok-native-msys2
sed -i -b 's/L="--disable-shared --enable-static"/# L="--disable-shared --enable-static"/' ./cross-compile/msys2/sigrok-native-msys2
sed -i -b 's@PKG_CONFIG_PATH=$P PYTHON=python3 ../configure $C $L --disable-python@PKG_CONFIG_PATH=$P PYTHON=python3 ../configure $C $L # --disable-python@' ./cross-compile/msys2/sigrok-native-msys2
sed -i -b 's@$GIT_CLONE git://github.com/dickens/libusb -b event-abstraction-v4@$GIT_CLONE git://github.com/dickens/libusb # -b event-abstraction-v4@' ./cross-compile/msys2/sigrok-native-msys2
```

And finally, let's start the build:

```
$ ./cross-compile/msys2/sigrok-native-msys2
Cloning into 'libusb'...
remote: Enumerating objects: 184, done.
remote: Counting objects: 100% (184/184), done.
remote: Compressing objects: 100% (143/143), done.
remote: Total 184 (delta 64), reused 78 (delta 39), pack-reused 0
Receiving objects: 100% (184/184), 375.41 KiB | 3.00 MiB/s, done.
Resolving deltas: 100% (64/64), done.
Updating files: 100% (176/176), done.
libtoolize: putting auxiliary files in '.'.
libtoolize: copying file './ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'm4'.
libtoolize: copying file 'm4/libtool.m4'
libtoolize: copying file 'm4/ltoptions.m4'
libtoolize: copying file 'm4/ltsugar.m4'
libtoolize: copying file 'm4/ltversion.m4'
libtoolize: copying file 'm4/lt~obsolete.m4'
configure.ac:4: installing './compile'
configure.ac:4: installing './config.guess'
configure.ac:4: installing './config.sub'
configure.ac:2: installing './install-sh'
configure.ac:2: installing './missing'
Makefile.am: installing './depcomp'
libtoolize: putting auxiliary files in '.'.
libtoolize: copying file './ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'm4'.
libtoolize: copying file 'm4/libtool.m4'
libtoolize: copying file 'm4/ltoptions.m4'
libtoolize: copying file 'm4/ltsugar.m4'
libtoolize: copying file 'm4/ltversion.m4'
libtoolize: copying file 'm4/lt~obsolete.m4'
configure.ac:38: installing './compile'
configure.ac:39: installing './config.guess'
configure.ac:39: installing './config.sub'
configure.ac:29: installing './install-sh'
configure.ac:29: installing './missing'
examples/Makefile.am: installing './depcomp'
configure: loading site script /mingw64/etc/config.site
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether to enable maintainer-specific portions of Makefiles... no
checking whether make supports nested variables... (cached) yes
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.exe
checking for suffix of executables... .exe
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking whether gcc understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of gcc... gcc3
checking build system type... x86_64-w64-mingw32
checking host system type... x86_64-w64-mingw32
checking how to print strings... printf
checking for a sed that does not truncate output... /usr/bin/sed
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc... C:/msys64/mingw64/x86_64-w64-mingw32/bin/ld.exe
checking if the linker (C:/msys64/mingw64/x86_64-w64-mingw32/bin/ld.exe) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... /mingw64/bin/nm -B
checking the name lister (/mingw64/bin/nm -B) interface... BSD nm
checking whether ln -s works... no, using cp -pR
checking the maximum length of command line arguments... 8192
checking how to convert x86_64-w64-mingw32 file names to x86_64-w64-mingw32 format... func_convert_file_msys_to_w32
checking how to convert x86_64-w64-mingw32 file names to toolchain format... func_convert_file_msys_to_w32
checking for C:/msys64/mingw64/x86_64-w64-mingw32/bin/ld.exe option to reload object files... -r
checking for objdump... objdump
checking how to recognize dependent libraries... file_magic ^x86 archive import|^x86 DLL
checking for dlltool... dlltool
checking how to associate runtime and link libraries... func_cygming_dll_for_implib
checking for ar... ar
checking for archiver @FILE support... @
checking for strip... strip
checking for ranlib... ranlib
checking command to parse /mingw64/bin/nm -B output from gcc object... ok
checking for sysroot... no
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for mt... no
checking if : is a manifest tool... no
checking how to run the C preprocessor... gcc -E
checking for ANSI C header files...
...
libtool: link: ar cru .libs/libusb-1.0.a  libusb_1_0_la-core.o libusb_1_0_la-descriptor.o libusb_1_0_la-io.o libusb_1_0_la-strerror.o libusb_1_0_la-sync.o libusb_1_0_la-hotplug.o os/libusb_1_0_la-events_windows.o os/libusb_1_0_la-threads_windows.o os/libusb_1_0_la-windows_usb.o libusb-1.0.o
libtool: link: ranlib .libs/libusb-1.0.a
libtool: link: ( cd ".libs" && rm -f "libusb-1.0.la" && cp -pR "../libusb-1.0.la" "libusb-1.0.la" )
make[3]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb/libusb'
dlltool  --kill-at --input-def ./libusb-1.0.def --dllname libusb-1.0.dll --output-lib .libs/libusb-1.0.dll.a
make[2]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb/libusb'
Making all in doc
make[2]: Entering directory '/d/src/sigrok-util_git/build_debug_64/libusb/doc'
make[2]: Nothing to be done for 'all'.
make[2]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb/doc'
make[2]: Entering directory '/d/src/sigrok-util_git/build_debug_64/libusb'
make[2]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb'
make[1]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb'
Making install in libusb
make[1]: Entering directory '/d/src/sigrok-util_git/build_debug_64/libusb/libusb'
make[2]: Entering directory '/d/src/sigrok-util_git/build_debug_64/libusb/libusb'
make[3]: Entering directory '/d/src/sigrok-util_git/build_debug_64/libusb/libusb'
 /usr/bin/mkdir -p '/home/sd/sr_msys2_debug_64/lib'
 /bin/sh ../libtool   --mode=install /usr/bin/install -c   libusb-1.0.la '/home/sd/sr_msys2_debug_64/lib'
libtool: install: /usr/bin/install -c .libs/libusb-1.0.dll.a /home/sd/sr_msys2_debug_64/lib/libusb-1.0.dll.a
libtool: install: base_file=`basename libusb-1.0.la`
...
make[1]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb'
Cloning into 'libserialport'...
remote: Enumerating objects: 57, done.
remote: Counting objects: 100% (57/57), done.
remote: Compressing objects: 100% (45/45), done.
remote: Total 57 (delta 15), reused 20 (delta 12)
Receiving objects: 100% (57/57), 102.22 KiB | 12.78 MiB/s, done.
Resolving deltas: 100% (15/15), done.
autoreconf: Entering directory `.'
autoreconf: configure.ac: not using Gettext
autoreconf: running: aclocal --force -I autostuff
autoreconf: configure.ac: tracing
autoreconf: running: libtoolize --copy --force
libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'autostuff'.
libtoolize: copying file 'autostuff/ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'autostuff'.
libtoolize: copying file 'autostuff/libtool.m4'
libtoolize: copying file 'autostuff/ltoptions.m4'
libtoolize: copying file 'autostuff/ltsugar.m4'
libtoolize: copying file 'autostuff/ltversion.m4'
libtoolize: copying file 'autostuff/lt~obsolete.m4'
autoreconf: running: /usr/bin/autoconf --force
autoreconf: running: /usr/bin/autoheader --force
autoreconf: running: automake --add-missing --copy --force-missing
...
mv -f .deps/windows.Tpo .deps/windows.Plo
/bin/sh ./libtool  --tag=CC --silent  --mode=link gcc -std=c99 -Wall -Wextra -pedantic -Wmissing-prototypes -Wshadow -DLIBSERIALPORT_ATBUILD -g -O2 -version-info 1:0:1 -no-undefined   -o libserialport.la -rpath /home/sd/sr_msys2_debug_64/lib serialport.lo timing.lo  windows.lo   -lsetupapi
 /usr/bin/mkdir -p '/home/sd/sr_msys2_debug_64/lib'
 /bin/sh ./libtool --silent  --mode=install /usr/bin/install -c   libserialport.la '/home/sd/sr_msys2_debug_64/lib'
 /usr/bin/mkdir -p '/home/sd/sr_msys2_debug_64/include'
 /usr/bin/install -c -m 644 ../libserialport.h '/home/sd/sr_msys2_debug_64/include'
 /usr/bin/mkdir -p '/home/sd/sr_msys2_debug_64/lib/pkgconfig'
 /usr/bin/install -c -m 644 libserialport.pc '/home/sd/sr_msys2_debug_64/lib/pkgconfig'
Cloning into 'libsigrok'...
...
configure: creating ./config.status
config.status: creating Makefile
config.status: creating libsigrok.pc
config.status: creating bindings/cxx/libsigrokcxx.pc
config.status: creating config.h
config.status: creating include/libsigrok/version.h
config.status: executing depfiles commands
config.status: executing libtool commands

libsigrok configuration summary:
 - Package version................. 0.6.0-git-ec30291
 - Library ABI version............. 4:0:0
 - Prefix.......................... /home/sd/sr_msys2_debug_64
 - Building on..................... x86_64-w64-mingw32
 - Building for.................... x86_64-w64-mingw32
 - Building shared / static........ yes / yes

Compile configuration:
 - C compiler...................... gcc
 - C compiler version.............. gcc.exe (Rev4, Built by MSYS2 project) 10.2.0
 - C compiler flags................ -g -O2
 - Additional C compiler flags..... -std=c99 -fvisibility=hidden
 - C compiler warnings............. -Wall -Wextra -Wmissing-prototypes
 - C++ compiler.................... g++
 - C++ compiler version............ g++.exe (Rev4, Built by MSYS2 project) 10.2.0
 - C++ compiler flags.............. -g -O2
 - C++ compiler warnings........... -Wall -Wextra
 - Linker flags....................

Detected libraries (required):
 - glib-2.0 >= 2.32.0.............. 2.66.1
 - libzip >= 0.10.................. 1.7.3

Detected libraries (optional):
 - libserialport >= 0.1.1.......... 0.1.1
 - libftdi1 >= 1.0................. 1.4
 - hidapi >= 0.8.0................. 0.9.0
 - bluez >= 4.0.................... no
 - nettle.......................... 3.6
 - libusb-1.0 >= 1.0.20............ 1.0.20
 - librevisa >= 0.0.20130412....... no
 - libgpib......................... no
 - libieee1284..................... no
 - gio-2.0 >= 2.24.0............... 2.66.1
 - check >= 0.9.4.................. 0.15.0
 - glibmm-2.4 >= 2.32.0............ 2.64.2
 - python = 3.8.................... no
 - python3 = 3.8................... 3.8
 - pygobject-3.0 >= 3.0.0.......... 3.38.0
 - ruby >= 2.5.0................... no
 - ruby-. >= 2.5.0................. no
...
Enabled language bindings:
 - C++............................. yes
 - Python.......................... yes
 - Ruby............................ no (missing: Ruby, Headers)
 - Java............................ no (missing: JavaC, JNI headers)

make  all-am
depbase=`echo src/serial.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
/bin/sh ./libtool  --tag=CC --silent  --mode=compile gcc -DHAVE_CONFIG_H   -Iinclude -I../include -I../src -I. -Ibindings/cxx/include -I../bindings/cxx/include -Ibindings/cxx   -std=c99 -fvisibility=hidden -Wall -Wextra -Wmissing-prototypes -pthread -mms-bitfields -IC:/msys64/home/sd/sr_msys2_debug_64/include -IC:/msys64/home/sd/sr_msys2_debug_64/include/libusb-1.0 -IC:/msys64/mingw64/include -IC:/msys64/mingw64/include/libftdi1 -IC:/msys64/mingw64/include/hidapi -IC:/msys64/mingw64/include -IC:/msys64/mingw64/include/glib-2.0 -IC:/msys64/mingw64/lib/glib-2.0/include -IC:/msys64/mingw64/include -g -O2 -MT src/serial.lo -MD -MP -MF $depbase.Tpo -c -o src/serial.lo ../src/serial.c &&\
...
copying selected object files to avoid basename conflicts...
cd ../bindings/cxx && SRCDIR=/d/src/sigrok-util_git/build_debug_64/libsigrok/build/../bindings/cxx/ BUILDDIR=/d/src/sigrok-util_git/build_debug_64/libsigrok/build/bindings/cxx/ doxygen Doxyfile 2>/dev/null
/bin/sh ./libtool  --tag=CC --silent  --mode=link gcc -std=c99 -fvisibility=hidden -Wall -Wextra -Wmissing-prototypes -pthread -mms-bitfields -IC:/msys64/home/sd/sr_msys2_debug_64/include -IC:/msys64/home/sd/sr_msys2_debug_64/include/libusb-1.0 -IC:/msys64/mingw64/include -IC:/msys64/mingw64/include/libftdi1 -IC:/msys64/mingw64/include/hidapi -IC:/msys64/mingw64/include -IC:/msys64/mingw64/include/glib-2.0 -IC:/msys64/mingw64/lib/glib-2.0/include -IC:/msys64/mingw64/include -g -O2   -o src/libdrivers.o src/libdrivers_head.la src/libdrivers.la \
        src/libdrivers_tail.la
test -d bindings/python/sigrok/core || /usr/bin/mkdir -p bindings/python/sigrok/core
python3 ../bindings/swig/doc.py python bindings/cxx/doxy/xml/index.xml start > bindings/python/sigrok/core/doc_start.i
test -d bindings/python/sigrok/core || /usr/bin/mkdir -p bindings/python/sigrok/core
python3 ../bindings/swig/doc.py python bindings/cxx/doxy/xml/index.xml end > bindings/python/sigrok/core/doc_end.i
echo "# Generated by libtool" > src/libdrivers.lo
echo "pic_object='libdrivers.o'" >> src/libdrivers.lo
echo "non_pic_object='libdrivers.o'" >> src/libdrivers.lo
/bin/sh ./libtool  --tag=CC --silent  --mode=link gcc -std=c99 -fvisibility=hidden -Wall -Wextra -Wmissing-prototypes -pthread -mms-bitfields -IC:/msys64/home/sd/sr_msys2_debug_64/include -IC:/msys64/home/sd/sr_msys2_debug_64/include/libusb-1.0 -IC:/msys64/mingw64/include -IC:/msys64/mingw64/include/libftdi1 -IC:/msys64/mingw64/include/hidapi -IC:/msys64/mingw64/include -IC:/msys64/mingw64/include/glib-2.0 -IC:/msys64/mingw64/lib/glib-2.0/include -IC:/msys64/mingw64/include -g -O2 -version-info 4:0:0 -no-undefined  -o libsigrok.la -rpath /home/sd/sr_msys2_debug_64/lib src/backend.lo src/binary_helpers.lo src/conversion.lo src/crc.lo src/device.lo src/session.lo src/session_file.lo src/session_driver.lo src/hwdriver.lo src/trigger.lo src/soft-trigger.lo src/analog.lo src/fallback.lo src/resource.lo src/strutil.lo src/log.lo src/version.lo src/error.lo src/std.lo src/sw_limits.lo src/input/input.lo src/input/feed_queue.lo src/input/binary.lo src/input/chronovu_la8.lo src/input/csv.lo src/input/logicport.lo src/input/raw_analog.lo src/input/saleae.lo src/input/trace32_ad.lo src/input/vcd.lo src/input/wav.lo src/input/null.lo src/output/output.lo src/output/analog.lo src/output/ascii.lo src/output/bits.lo src/output/binary.lo src/output/csv.lo src/output/chronovu_la8.lo src/output/wav.lo src/output/hex.lo src/output/ols.lo src/output/srzip.lo src/output/vcd.lo src/output/wavedrom.lo src/output/null.lo src/transform/transform.lo src/transform/nop.lo src/transform/scale.lo src/transform/invert.lo src/scpi/scpi.lo src/scpi/scpi_tcp.lo  src/bt/bt_bluez.lo src/serial.lo src/serial_bt.lo src/serial_hid.lo src/serial_hid_bu86x.lo src/serial_hid_ch9325.lo src/serial_hid_cp2110.lo src/serial_hid_victor.lo src/serial_libsp.lo src/scpi/scpi_serial.lo src/ezusb.lo src/usb.lo src/scpi/scpi_usbtmc_libusb.lo   src/modbus/modbus.lo src/modbus/modbus_serial_rtu.lo src/dmm/asycii.lo src/dmm/bm25x.lo src/dmm/bm52x.lo src/dmm/bm86x.lo src/dmm/dtm0660.lo src/dmm/eev121gw.lo src/dmm/es519xx.lo src/dmm/fs9721.lo src/dmm/fs9922.lo src/dmm/m2110.lo src/dmm/metex14.lo src/dmm/ms2115b.lo src/dmm/ms8250d.lo src/dmm/rs9lcd.lo src/dmm/ut372.lo src/dmm/ut71x.lo src/dmm/vc870.lo src/dmm/vc96.lo src/lcr/es51919.lo src/lcr/vc4080.lo src/scale/kern.lo src/libdrivers.lo -lws2_32 -LC:/msys64/home/sd/sr_msys2_debug_64/lib -LC:/msys64/mingw64/bin -LC:/msys64/mingw64/lib -lserialport -lftdi1 -lhidapi -lnettle -lusb-1.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0 -lintl -lzip
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/10.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: src/.libs/usb.o: in function `usb_source_new':
D:\src\sigrok-util_git\build_debug_64\libsigrok\build/../src/usb.c:289: undefined reference to `libusb_free_pollfds'
collect2.exe: error: ld returned 1 exit status
make[1]: *** [Makefile:2428: libsigrok.la] Error 1
make[1]: *** Waiting for unfinished jobs....
make: *** [Makefile:2074: all] Error 2
```

Note, at this time, the files and directories are:

```
$ ls -l
total 60K
drwxr-xr-x 1 user None    0 Oct 19 09:27 build_debug_64/
drwxr-xr-x 1 user None    0 Oct 19 08:49 build_release_64/
drwxr-xr-x 1 user None    0 Oct 19 08:46 cross-compile/
drwxr-xr-x 1 user None    0 Oct 19 08:46 debug/
drwxr-xr-x 1 user None    0 Oct 19 08:46 firmware/
drwxr-xr-x 1 user None    0 Oct 19 08:46 source/
drwxr-xr-x 1 user None    0 Oct 19 08:46 util/
-rw-r--r-- 1 user None  18K Oct 19 08:46 COPYING.v2
-rw-r--r-- 1 user None  35K Oct 19 08:46 COPYING.v3
-rw-r--r-- 1 user None 1.4K Oct 19 08:46 README
```

So, we can inspect like this:

```
$ grep -r libusb_free_pollfds build_debug_64
Binary file build_debug_64/libsigrok/build/src/.libs/usb.o matches
Binary file build_debug_64/libsigrok/build/src/usb.o matches
build_debug_64/libsigrok/src/usb.c:     libusb_free_pollfds(upollfds);

$ grep -r libusb_free_pollfds $HOME/sr_msys2_debug_64
$ # NOTHING!
```

This process does shallow git clones - so in another directory:

```
$ git clone https://github.com/dickens/libusb.git libusb_git
Cloning into 'libusb_git'...
remote: Enumerating objects: 15443, done.
remote: Total 15443 (delta 0), reused 0 (delta 0), pack-reused 15443
Receiving objects: 100% (15443/15443), 4.54 MiB | 5.44 MiB/s, done.
Resolving deltas: 100% (11247/11247), done.
Updating files: 100% (176/176), done.

$ cd libusb_git/

$ grep -r libusb_free_pollfds .
$ # nothing
$ git log -Slibusb_free_pollfds
$ # nothing

$ git --no-pager grep libusb_free_pollfds $(git rev-list --all) | grep libusb.h | (head -n1; tail -n1)
4eac78fadd62c03c689bea7b3c775b22850c24c3:libusb/libusb.h:void LIBUSB_CALL libusb_free_pollfds(const struct libusb_pollfd **pollfds);
a4d2cb89b0c4f10f6c0cc02a2657cbaa94135470:libusb/libusb.h:void LIBUSB_CALL libusb_free_pollfds(const struct libusb_pollfd **pollfds);

$ git log 4eac78fadd62c03c689bea7b3c775b22850c24c3 -1
commit 4eac78fadd62c03c689bea7b3c775b22850c24c3 (origin/examples)
Author: Chris Dickens <christopher.a.dickens@gmail.com>
Date:   Tue Sep 15 14:15:00 2020 -0700

    examples

$ git log a4d2cb89b0c4f10f6c0cc02a2657cbaa94135470 -1
commit a4d2cb89b0c4f10f6c0cc02a2657cbaa94135470
Author: Chris Dickens <christopher.a.dickens@gmail.com>
Date:   Sun Mar 1 00:45:11 2015 -0800

    API: Add libusb_free_pollfds() function
...
```

Turns out, master branch here is old, from 2015 - latest existing is examples branch; try that one? Back to `sigrok-util_git` directory:

```
sed -i -b 's@$GIT_CLONE git://github.com/dickens/libusb # -b event-abstraction-v4@$GIT_CLONE git://github.com/dickens/libusb -b examples # -b event-abstraction-v4@' ./cross-compile/msys2/sigrok-native-msys2
```

And again:

```
$ ./cross-compile/msys2/sigrok-native-msys2
...
 /usr/bin/install -c -m 644 libusb.h '/home/sd/sr_msys2_debug_64/include/libusb-1.0'
make[2]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb/libusb'
make[1]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb/libusb'
make[1]: Entering directory '/d/src/sigrok-util_git/build_debug_64/libusb'
make[2]: Entering directory '/d/src/sigrok-util_git/build_debug_64/libusb'
make[2]: Nothing to be done for 'install-exec-am'.
 /usr/bin/mkdir -p '/home/sd/sr_msys2_debug_64/lib/pkgconfig'
 /usr/bin/install -c -m 644 libusb-1.0.pc '/home/sd/sr_msys2_debug_64/lib/pkgconfig'
make[2]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb'
make[1]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/libusb'
Cloning into 'libserialport'...
...
Must specify package names on the command line
checking for libusb_os_handle... no
checking for zip_discard... yes
configure: error: Windows builds require the event-abstraction branch of libusb
```

Eh, there is no such branch anymore; however, now libusb now is indeed built with `libusb_free_pollfds`:

```
$ grep -r pollfds build_debug_64/libusb/
build_debug_64/libusb/ChangeLog:* New libusb_free_pollfds() API
Binary file build_debug_64/libusb/libusb/.libs/io.o matches
Binary file build_debug_64/libusb/libusb/.libs/libusb-1.0.a matches
Binary file build_debug_64/libusb/libusb/.libs/libusb-1.0.dll matches
Binary file build_debug_64/libusb/libusb/.libs/libusb-1.0.dll.a matches
build_debug_64/libusb/libusb/core.c:  * - libusb_free_pollfds()
build_debug_64/libusb/libusb/core.c:  * - libusb_get_pollfds()
build_debug_64/libusb/libusb/core.c:  * - libusb_pollfds_handle_timeouts()
build_debug_64/libusb/libusb/io.c: * On Windows, libusb_get_pollfds() simply returns NULL. Applications which
build_debug_64/libusb/libusb/io.c:libusb_get_pollfds(ctx)
build_debug_64/libusb/libusb/io.c:libusb_get_pollfds(ctx)
...
```

