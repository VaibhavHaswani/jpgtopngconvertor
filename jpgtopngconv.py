#Script will convert jpg files in the folder given to command line to png folder name given as command line

from PIL import Image
import sys
import os
path=sys.argv[1]
pngf=sys.argv[2]
li=[f for f in os.listdir(path) if "." in f and f.split('.')[1]=="jpg"]

npath=f"{path}\\{pngf}"
if not os.path.isdir(npath):   #check if directory exist
	os.mkdir(npath)	

for img in li:
	jpg=Image.open(path+"\\"+img)
	jpg.save(f"{path}\\{pngf}\\{img.split('.')[0]}.png","png")



