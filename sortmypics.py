#!/usr/bin/env python

# version 0.1 
# TODO: a lot :-) 



import exifread
import locale
import os
import sys
import shutil
import string
import errno

from optparse import OptionParser
from datetime import datetime



from sys import argv, stderr, exit
answer = ""

def main():
 usage = "usage: %prog [options]"
 parser = OptionParser(usage=usage)
 parser.add_option("-d","--directory",dest="directory",help="directory with the pics", metavar="/home/user/mypics")
 parser.add_option("-p","--prefix",dest="prefix",help="/prefix/", metavar="/pics/destination")
 (options,args) = parser.parse_args()
 dir = "."
 global answer
 if options.directory:
   dir = options.directory
 else:
   parser.print_help()
   sys.exit(0)
 locale.setlocale(locale.LC_ALL,'de_CH.UTF-8')
 os.chdir(dir)
 try:
   pics = os.listdir(dir)
   for pic in pics:
     if not os.path.isdir(pic):
       f = open(pic,'rb')
       tags = exifread.process_file(f, stop_tag='DateTimeOriginal')
       f.close()
       date = tags.get('EXIF DateTimeOriginal')
       if date:
         # 2013:08:10 14:54:03
         dat = datetime.strptime(str(date),'%Y:%m:%d %H:%M:%S')
         dir_string = dat.strftime("./%Y/%B/")
         try:
           if options.prefix:
             dir_string = options.prefix+dir_string
           os.makedirs(dir_string)
         except OSError as exc: # Python >2.5
           if exc.errno == errno.EEXIST:
             if not os.path.isdir(dir_string):
               answer = ask_if_overwrite(dir_string)
               if answer == "y" or answer == "a":
                 try:
                   os.makedirs(dir_string)
                 except OSError as exc:
                   if exc.errno == errno.EEXIST:
                      pass
                   else:
                     raise
           else:
             raise
         print "copying %s to %s"%(pic,dir_string)
         if os.path.exists(dir_string+pic):
           anwser = ask_if_overwrite(pic)
           if answer == "y" or answer == "a":
             shutil.copy2(pic,dir_string)
             print "overwriting %s to %s"%(pic,dir_string)
           else:
             print "skipping %s" %pic
         else:
           shutil.copy2(pic,dir_string)
       else:
         if not os.path.exists("./sortyourself"):
           os.makedirs("./sortyourself")
         shutil.copy2(pic,"./sortyourself")
         print "copying %s to %s"%(pic,"./sortyourself")
     else:
       print "file not a pic"
 except OSError as e:
   print e
   print "Directory does not contain any files"

def ask_if_overwrite(path):
  global answer
  if answer == "a" or answer == "s":
    return answer
  while answer != "y" and answer != "n" and answer != "a" and answer != "s" :
    answer = raw_input("%s file or directory exists. Do you want to overwrite?(Y/N/A (ALL) /S (Skipp all) )"%path)
  return str.lower(answer)


if __name__ == "__main__":
  try:
    main()

  except KeyboardInterrupt:
    sys.exit(0)

