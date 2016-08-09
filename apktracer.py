#!/usr/bin/python
import re
import os
import tempfile

print "Starting apk analysis...\n"

##### This flag will insert debugging statements into the APK.
JonestownThisAPK = True
InsertFakeLineNumbers = True

##### Some packages can be nosiy and not important for analysis. Use this to skip them in APKSmash.
##### This match happens on the file directory name or the package, so use '\\' instead of '.'
##### Example: skip_classes = ['\\com\\flurry', '\\org\\cocos2dx']
#skip_classes = []
skip_classes = ['$', '/android/support']

"""	
 Function (dir_byfiletype) lets us get all files based on extension from
 a directory and its subdirectories
"""
def dir_byfiletype(dir_name, *args):
    fileList = []
    for dirname, dirnames, filenames in os.walk(dir_name):
        for filename in filenames:
            dirfile = os.path.join(dirname, filename)
            if os.path.isfile(dirfile):
                if os.path.splitext(dirfile)[1][1:] in args:
                    fileList.append(dirfile)
                pass
    return fileList


#####  XML read and loaded, now go thru code 
dir_path = raw_input(">>> Input APP dir path: ")
fileList = dir_byfiletype(dir_path, 'smali', 'java')

##### New Method, clear stored values Counter is as follows: {searchterm: [count, [list_of_occurnces]]}
linecount = 1

for f in fileList:
        #print "Searching file: " + f
        
        if any(badpath in f for badpath in skip_classes):
            print "Skipping file: " + f
            continue
         
	smali_name = f
	smaliIn = open(smali_name, "r")

	tmp_fd, tmp_name = tempfile.mkstemp(suffix='.smalitemp')
	smaliOut = open(tmp_name, 'w+b')

	for line in smaliIn:
		smashline = ""
		smaliOut.write(line) 
		
		##### At this point, writes are adding after the orginal line of smali code
		if JonestownThisAPK:
			#####    To help with obfuscated apps, log out each time we enter a new method
			if line.find('prologue') > 0:
				smashline += "    invoke-static {}, Lcom/7a6ac0/iglogger;->trace_method()I" + "\n"
					
		if InsertFakeLineNumbers and len(smashline) > 0 :
			smashline = "    .line " + str(linecount) + "\n" + smashline 
			linecount += 1
			
		##### Write out afterwards
		smaliOut.write(smashline)
			
	
	smaliIn.close()
	smaliOut.close()
	os.close(tmp_fd)
	os.remove(smali_name)
	os.rename(tmp_name, smali_name)
