# kivy-buildozer-bug
Sample python code demonstrating kivy/buildozer android build problems

Sample python/kivy code with 3 screens, each screen has own class. 
Depending on repository files configuration kivy buildozer makes either working or crashing .apk

Crashinng apk leaves the following message on Android (adb logcat)

E/dalvikvm( 2277): dlopen("/data/data/eu.ijbd.nmeter/files/lib/python2.7/lib-dynload/_sqlite3.so") failed: dlopen failed: library "/data/data/eu.ijbd.nmeter/files/lib/python2.7/lib-dynload/_sqlite3.so" not found
E/dalvikvm( 2277): dlopen("/data/data/eu.ijbd.nmeter/files/lib/python2.7/lib-dynload/_imaging.so") failed: dlopen failed: library "/data/data/eu.ijbd.nmeter/files/lib/python2.7/lib-dynload/_imaging.so" not found
 

Workarounds
buildozer spec needs hostpython2 in requirements, without it buidozer android_new crashes
requirements = kivy, hostpython2

