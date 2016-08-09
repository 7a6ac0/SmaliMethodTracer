SmaliMethodTracer
=================

Inject log message into smali file, you can use logcat(tag:IGLogger) to find out the method is called or not.

Usage
=====

1. Use APKTool to decompile an APK.
2. copy iglogger.smali into smali directory.
2. python apktracer.py, and enter the directory path which apktool generated.
3. Rebuild to an APK, and have fun.
