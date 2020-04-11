#Script will convert jpg files in the folder given to command line to png folder name given as command line

from PIL import Image
import sys
import os
path=sys.argv[1]
pngf=sys.argv[2]
li=[f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) and f.split('.')[1]=="jpg"]

npath=os.path.join(path,pngf)
if not os.path.isdir(npath):   #check if directory exist
	os.mkdir(npath)	

for img in li:
	jpg=Image.open(os.path.join(path,img))
	jpg.save(os.path.join(npath,f"{img.split('.')[0]}.png"),"png")



