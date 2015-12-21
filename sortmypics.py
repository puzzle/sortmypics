#!/usr/bin/env python

# version 0.2 
# TODO: - document
#       - fix copy function
#       - header



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



class SortMyPics:

  "Constructor" 
  def __init__(self):
    self.__answer = ""
    locale.setlocale(locale.LC_ALL,'de_CH.UTF-8')

  """Return parsed args. If destination directory is empty return None"""
  def parse_commands(self):
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("-d","--directory",dest="directory",help="directory with the pics", metavar="/home/user/mypics")
    parser.add_option("-p","--prefix",dest="prefix",help="/prefix/", metavar="/pics/destination")
    (options,args) = parser.parse_args()
    if options.directory:
      return parser.parse_args() 
    else:
      parser.print_help()
      return None
  """Get date of pics and make destination directories""" 
  def make_destination_directories(self,src_dir, dest_dir):
    try:
      pics = os.listdir(src_dir)
      for pic in pics:
       if not os.path.isdir(src_dir+pic):
         f = open(src_dir+pic,'rb')
         tags = exifread.process_file(f, stop_tag='DateTimeOriginal')
         f.close()
         date = tags.get('EXIF DateTimeOriginal')
         if date:
           # 2013:08:10 14:54:03
           dat = datetime.strptime(str(date),'%Y:%m:%d %H:%M:%S')
           dir_string = dat.strftime("/%Y/%B/")
           try:
             if dest_dir:
               dir_string = dest_dir+dir_string
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
         else:
           print "file not a pic %s" %pic
    except OSError as e:
     print e
     print "Directory does not contain any files"
 
  def copy_pics(self,src_dir, dest_dir):
    pics = os.listdir(src_dir)
    dir_string = dest_dir
    for pic in pics:
      print "copying %s to %s"%(src_dir+pic,dir_string)
      if os.path.exists(dir_string+pic):
        anwser = self.ask_if_overwrite(pic)
        if answer == "y" or answer == "a":
          shutil.copy2(src_dir+pic,dir_string)
          print "overwriting %s to %s"%(pic,dir_string)
        if answer == "s" :
           print "skipping %s" %pic
        else:
           shutil.copy2(src_dir+pic,dir_string)
      else:
         if not os.path.exists("./sortyourself"):
           os.makedirs("./sortyourself")
         shutil.copy2(src_dir+pic,"./sortyourself")
         print "copying %s to %s"%(pic,"./sortyourself")

  def ask_if_overwrite(self,path):
    if answer == "a" or answer == "s":
      return answer
    while answer != "y" and answer != "n" and answer != "a" and answer != "s" :
      answer = raw_input("%s file or directory exists. Do you want to overwrite?(Y/N/A (ALL) /S (Skipp all) )"%path)
    return str.lower(answer)




if __name__ == "__main__":
  try:
   smp = SortMyPics()
   (options,args) = smp.parse_commands()
   prefix = "."
   if options.prefix:
     prefix = options.prefix
   smp.make_destination_directories(options.directory,prefix)
   smp.copy_pics(options.directory,prefix)

   

  except KeyboardInterrupt:
    sys.exit(0)

