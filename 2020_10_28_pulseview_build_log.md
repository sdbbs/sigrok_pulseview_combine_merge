# Pulseview build log


Trying to build pulseview from git - failed at something libusb; ... ok, fixed that ( [sigrok / ThreaC: [sigrok-devel] error: Windows builds require the event-abstraction branch of libusb ?](https://sourceforge.net/p/sigrok/mailman/sigrok-devel/thread/bc98f387-cfce-2832-ab3f-18dcea9fb87d%40brothers-sons.dk/#msg37138755) ); now this is the problem:

```
[100%] Linking CXX executable pulseview.exe
C:/msys64/mingw64/bin/cmake.exe -E rm -f CMakeFiles/pulseview.dir/objects.a
C:/msys64/mingw64/bin/ar.exe cr CMakeFiles/pulseview.dir/objects.a @CMakeFiles/pulseview.dir/objects1.rsp
C:/msys64/mingw64/bin/c++.exe -g -Wl,--whole-archive CMakeFiles/pulseview.dir/objects.a -Wl,--no-whole-archive -o pulseview.exe -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles/pulseview.dir/linklibs.rsp
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/10.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: CMakeFiles/pulseview.dir/objects.a(main.cpp.obj): in function `StaticQWindowsIntegrationPluginPluginInstance::StaticQWindowsIntegrationPluginPluginInstance()':
C:/src/sigrok-util_git/build_debug_64/pulseview/main.cpp:73: undefined reference to `qt_static_plugin_QWindowsIntegrationPlugin()'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/10.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: CMakeFiles/pulseview.dir/objects.a(main.cpp.obj): in function `StaticQSvgPluginPluginInstance::StaticQSvgPluginPluginInstance()':
C:/src/sigrok-util_git/build_debug_64/pulseview/main.cpp:74: undefined reference to `qt_static_plugin_QSvgPlugin()'
```

At this time, everything freezes; run SysInternals Process Explorer procexp64.exe as Administrator - can see a sequence make.exe > c++.exe > collect2.exe > ld.exe ; ld keeps on using CPU% time, but has no change in RAM usage, and even if it left, nothing much seems to happen. But, if we hit ctrl-C in terminal, it is these processes will remain as "ghosts". So, kill ld.exe from Process Explorer ... when that happens, we have this:

```
collect2.exe: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/pulseview.dir/build.make:1966: pulseview.exe] Error 1
make[2]: *** Deleting file 'pulseview.exe'
make[2]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/pulseview/build'
make[1]: *** [CMakeFiles/Makefile2:118: CMakeFiles/pulseview.dir/all] Error 2
make[1]: Leaving directory '/d/src/sigrok-util_git/build_debug_64/pulseview/build'
make: *** [Makefile:171: all] Error 2
```

Then comment out most of sigrok-native-msys2 script; save the library list given in the file `C:\src\sigrok-util_git\build_debug_64\pulseview\build\CMakeFiles\pulseview.dir\linklibs.rsp`, and then do manually:

```
$ cd build_debug_64/pulseview/build/
$ C:/msys64/mingw64/bin/cmake.exe -E rm -f CMakeFiles/pulseview.dir/objects.a
$ /c/msys64/mingw64/bin/ar.exe cr CMakeFiles/pulseview.dir/objects.a @CMakeFiles/pulseview.dir/objects1.rsp

$ /c/msys64/mingw64/bin/c++.exe -g -Wl,--whole-archive CMakeFiles/pulseview.dir/objects.a -Wl,--no-whole-archive -o pulseview.exe -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles/pulseview.dir/linklibs.rsp
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/10.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: CMakeFiles/pulseview.dir/objects.a(main.cpp.obj): in function `StaticQWindowsIntegrationPluginPluginInstance::StaticQWindowsIntegrationPluginPluginInstance()':
C:/src/sigrok-util_git/build_debug_64/pulseview/main.cpp:73: undefined reference to `qt_static_plugin_QWindowsIntegrationPlugin()'
```

Ok, so that worked .. but now we have to insert all those missing libraries in the `linklibs.rsp` ...

Tried to add C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/libqsvg.a
C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/libqwindows.a - everything fails here, even if it has .text$_Z42qt_static_plugin_QWindowsIntegrationPluginv symbol?

```
$ /c/msys64/mingw64/bin/c++.exe -g -Wl,--whole-archive CMakeFiles/pulseview.dir/objects.a -Wl,--no-whole-archive -o pulseview.exe -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles/pulseview.dir/linklibs.rsp
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/10.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/libqsvg.a(main.o):main.cpp:(.text$_ZNK10QSvgPlugin6createEP9QIODeviceRK10QByteArray+0x2c): undefined reference to `QImageIOHandler::setDevice(QIODevice*)'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/10.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/libqsvg.a(main.o):main.cpp:(.text$_ZNK10QSvgPlugin6createEP9QIODeviceRK10QByteArray+0x37): undefined reference to `QImageIOHandler::setFormat(QByteArray const&)'
C:/msys64/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/10.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/libqsvg.a(main.o):main.cpp:(.text$_ZN10QSvgPluginD1Ev[_ZN10QSvgPluginD1Ev]+0xb): undefined reference to `QImageIOPlugin::~QImageIOPlugin()'
```

...

Actually,  just noticed that there is C:/msys64/mingw64/share/qt5/plugins/imageformats/qsvg.dll C:/msys64/mingw64/share/qt5/plugins/platforms/qwindows.dll in the linklibs (and there are no .dll.a versions of these - and this is a static build!); maybe should replace those? Otherwise I tried adding: C:/msys64/mingw64/qt5-static/share/qt5/plugins/imageformats/libqsvg.a C:/msys64/mingw64/qt5-static/share/qt5/plugins/platforms/libqwindows.a C:/msys64/mingw64/qt5-static/lib/libQt5FontDatabaseSupport.a - but that keeps failing with undefined references ... also seemingly -ldwmapi is needed ...

In the end, after manually looking up symbols using:

    $ find /c/msys64/mingw64/qt5-static/ -name \*.a -exec bash -c "nm --defined-only {} 2>/dev/null | grep windowsMessageName && echo {}" \;

... and changing the order of the libraries listed in `linklibs.rsp`, I got a `linklibs.rsp` which actually does compile - and it is here:

* [linklibs.rsp](linklibs.rsp)

After this, Pulseview is built - but it will not run "out of the box":

```
$ ./pulseview.exe
Python path configuration:
  PYTHONHOME = (not set)
  PYTHONPATH = (not set)
  program name = 'python3'
  isolated = 0
  environment = 1
  user site = 1
  import site = 1
  sys._base_executable = 'C:/src/sigrok-util_git/build_debug_64/pulseview/build/pulseview.exe'
  sys.base_prefix = 'C:/a/_temp/msys/msys64/mingw64'
  sys.base_exec_prefix = 'C:/a/_temp/msys/msys64/mingw64'
  sys.executable = 'C:/src/sigrok-util_git/build_debug_64/pulseview/build/pulseview.exe'
  sys.prefix = 'C:/a/_temp/msys/msys64/mingw64'
  sys.exec_prefix = 'C:/a/_temp/msys/msys64/mingw64'
  sys.path = [
    'C:/a/_temp/msys/msys64/mingw64/lib/python38.zip',
    'C:/a/_temp/msys/msys64/mingw64/lib/python3.8',
    'C:/a/_temp/msys/msys64/mingw64/lib/python3.8',
    'C:/a/_temp/msys/msys64/mingw64/lib/lib-dynload',
  ]
Could not find platform independent libraries <prefix>
Could not find platform dependent libraries <exec_prefix>
Consider setting $PYTHONHOME to <prefix>[:<exec_prefix>]
Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding
Python runtime state: core initialized
ModuleNotFoundError: No module named 'encodings'

Current thread 0x000030e4 (most recent call first):
<no Python frame>
```

We can try something like this to find the Python path ( see https://stackoverflow.com/questions/7850908/what-exactly-should-be-set-in-pythonpath ):

```
$ python3 -c "import sys;print(sys.path)"
['', 'C:/msys64/mingw64/lib/python38.zip', 'C:/msys64/mingw64/lib/python3.8', 'C:/msys64/mingw64/lib/python3.8/lib-dynload', 'C:/msys64/mingw64/lib/python3.8/site-packages', 'C:/msys64/mingw64/lib/python3.8/site-packages/pyliblo-0.10.0-py3.8-mingw.egg', 'C:/msys64/mingw64/lib/python3.8/site-packages/saleae-0.9.0-py3.8.egg', 'C:/msys64/mingw64/lib/python3.8/site-packages/enum34-1.1.9-py3.8.egg', 'C:/msys64/mingw64/lib/python3.8/site-packages/future-0.18.2-py3.8.egg']
```

So, we can now set the following PYTHONHOME:

```
$ PYTHONHOME=/c/msys64/mingw64 ./pulseview.exe
Segmentation fault
```

... however, it segfaults. A quick inspection with gdb reveals this:

```
$ PYTHONHOME=/c/msys64/mingw64 gdb --args ./pulseview.exe
GNU gdb (GDB) 9.2
...
Reading symbols from ./pulseview.exe...
(gdb) r
Starting program: D:\src\sigrok-util_git\build_debug_64\pulseview\build\pulseview.exe
[New Thread 13812.0x366c]
[New Thread 13812.0xd28]
[New Thread 13812.0x320c]
[New Thread 13812.0xde0]
[New Thread 13812.0x35e4]
warning:
warning: AllK required contiguous memory = 534200 (64bit)
warning:   8 HotK Handles: HandleSize 2112 PoolSize 16912 (bytes)
warning:   64 LstK Handles: HandleSize 64 PoolSize 4112 (bytes)
warning:   1024 LstInfoK Handles: HandleSize 64 PoolSize 65552 (bytes)
warning:   64 UsbK Handles: HandleSize 96 PoolSize 6160 (bytes)
warning:   32 DevK Handles: HandleSize 112 PoolSize 3600 (bytes)
warning:   4096 OvlK Handles: HandleSize 104 PoolSize 426000 (bytes)
warning:   64 OvlPoolK Handles: HandleSize 96 PoolSize 6160 (bytes)
warning:   32 StmK Handles: HandleSize 176 PoolSize 5648 (bytes)
warning:
warning: Dynamically allocated as needed:
warning:        KLST_DEVINFO = 2596 bytes each
[New Thread 13812.0x2e9c]
[New Thread 13812.0x2924]
[New Thread 13812.0x3440]
[Thread 13812.0x3440 exited with code 0]
[New Thread 13812.0x3d14]

Thread 1 received signal SIGSEGV, Segmentation fault.
list_del (entry=0x1104be68) at libusbi.h:195
195             entry->next->prev = entry->prev;
(gdb) p entry
$1 = (struct list_head *) 0x1104be68
...
```

We will also notice the device enumeration startup window of PulseView be frozen at this time. So regardless of what the actual problem is, we can try avoiding it by using the `-D, --dont-scan` command line option:

```
$ PYTHONHOME=/c/msys64/mingw64 ./pulseview.exe -D
"Note for device developers: Ignoring device configuration capability 'Capture file' as it is missing GET and/or SET"
...
```

... and PulseView finally runs!
