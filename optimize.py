#!/usr/bin/python

import os
import glob
from subprocess import Popen, PIPE
from os import listdir

dir_path = os.getcwd()

success = 0

file_names = listdir('.')
for file_path in file_names:
if file_path.endswith(".jpg"):
    optimize = Popen(["mozjpeg", "-optimize", "-outfile", file_path + ".tmp", file_path], stdout=PIPE)
    optimize.wait()
    try:
        os.remove(os.path.join(dir_path, file_path))
    except:
        print "Insufficient permissions to remove ", file_path
    else:
        try:
            os.rename(os.path.join(dir_path, file_path + ".tmp"), os.path.join(dir_path, file_path))
        except:
            print "Could not move ", file_path
        else:
            success += 1

print ""
print "===================================================="
print " ** Image Optimization Complete **"
print "", success, "JPG images optimized"
print " Don't forget to optimize your PNG and SVG images"
print " \ (^_^) / "
print "===================================================="
print ""
