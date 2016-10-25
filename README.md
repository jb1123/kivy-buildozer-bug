# kivy-buildozer-bug
Sample python code demonstrating kivy/buildozer android build problems I have encountered. 
The code has 3 screens, each screen has own class. Depending on repository files configuration kivy buildozer makes either working or crashing .apk

working_apk – all code in main.py, apk works
crashing apk – code imports used, apk crashes

Both versions built with 'buildozer android_new debug'

Crashinng apk leaves the following message on Android (adb logcat)

E/dalvikvm( 2277): dlopen("/data/data/eu.ijbd.nmeter/files/lib/python2.7/lib-dynload/_sqlite3.so") failed: dlopen failed: library "/data/data/eu.ijbd.nmeter/files/lib/python2.7/lib-dynload/_sqlite3.so" not found
E/dalvikvm( 2277): dlopen("/data/data/eu.ijbd.nmeter/files/lib/python2.7/lib-dynload/_imaging.so") failed: dlopen failed: library "/data/data/eu.ijbd.nmeter/files/lib/python2.7/lib-dynload/_imaging.so" not found


Workarounds
buildozer spec needs hostpython2 in requirements, without it buidozer android_new crashes
requirements = kivy, hostpython2
buildozer android (legacy pygame provider) works without hostpython2 I requirements

In crashing_apk import stetement modification seems to fix crashing_apk problem: 

from nmeter.meterlist import MeterList #apk crashes
from meterlist import MeterList #apk works

Since both versions work on linux I believe it is a buildozer bug
