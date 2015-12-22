#!/usr/bin/env python

# version 0.3 
# TODO: - document
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
    self.__pics = []
    self.__sortyourself = []
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
         dir_string = ""
         if date:
           # 2013:08:10 14:54:03
           dat = datetime.strptime(str(date),'%Y:%m:%d %H:%M:%S')
           dir_string = dat.strftime("%Y/%B/")
           self.__pics.append((src_dir+pic,dest_dir+dir_string))
         else:
           print "file not a pic %s or no exif date" %pic
           dir_string = "sortyourself/"
           self.__sortyourself.append((src_dir+pic,dest_dir+dir_string))
         try:
           os.makedirs(dest_dir+dir_string)
         except OSError as exc: # Python >2.5
           if exc.errno == errno.EEXIST:
             if not os.path.isdir(dir_string):
               try:
                 os.makedirs(dest_dir+dir_string)
               except OSError as exc:
                 if exc.errno == errno.EEXIST:
                   pass
                 else:
                   raise
           else:
             raise

    except OSError as e:
     print e
     print "Directory does not contain any files"
 
  def copy_pics(self,pics):
    for pic,dir_string in pics:
      (head,tail) = os.path.split(pic)
      dir_string = dir_string+tail
      print "ldldld %s" %(dir_string)
      if os.path.exists(dir_string):
        self.ask_if_overwrite(pic)
        if self.__answer == "y" or self.__answer == "a":
          shutil.copy2(pic,dir_string)
          print "overwriting %s to %s"%(pic,dir_string)
        if self.__answer == "s" :
           print "skipping %s" %pic
      else:
           shutil.copy2(pic,dir_string)

  def ask_if_overwrite(self,path):
    if self.__answer == "a" or self.__answer == "s":
      return 
    while (self.__answer == "y" or self.__answer == "n") or (self.__answer != "a" and self.__answer != "s") :
      self.__answer = raw_input("%s file or directory exists. Do you want to overwrite?(Y/N/A (ALL) /S (Skipp all) )"%path)
    str.lower(self.__answer)

  def get_pics(self):
    return self.__pics

  def get_sortyourself(self):
    return self.__sortyourself


if __name__ == "__main__":
  try:
   smp = SortMyPics()
   (options,args) = smp.parse_commands()
   prefix = "."
   if options.prefix:
     prefix = options.prefix
   smp.make_destination_directories(options.directory,prefix)
   smp.copy_pics(smp.get_pics())
   smp.copy_pics(smp.get_sortyourself())

   

  except KeyboardInterrupt:
    sys.exit(0)

