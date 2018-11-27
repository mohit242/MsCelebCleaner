import os
import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument('imgFolder',type=str,default='./raw')
parser.add_argument('--washList',type=str,default='./list.txt')
args = parser.parse_args()
washList = args.washList
r=[]
if os.path.exists(args.imgFolder):
    for path, dnames, fnames in os.walk(args.imgFolder):
        r.extend([os.path.join(path, x) for x in fnames])
        # r.extend(fold for fold in dnames)
# print(len(r))
wlFile = open(washList,'r')
goodFiles = wlFile.readlines()
goodFiles = [f.strip('\n ') for f in goodFiles]
print("Warning !!!!!!!!!!!!!!\nCheck folder path before deleting files: {}\nDo you want to continue?".format(args.imgFolder))
accept= input()
if accept.lower() != 'y':
    print("ABORTING")
    exit()
print(goodFiles[:10])
counter=0
for imgFile in goodFiles:
    if(os.path.exists(os.path.join(args.imgFolder,imgFile))):
        splitPath = os.path.split(imgFile)
        modImgFile=os.path.join(splitPath[0],'zx_'+splitPath[1])
        os.rename(os.path.join(args.imgFolder,imgFile),os.path.join(args.imgFolder,modImgFile))
        counter+=1
print('Total files found-{}'.format(counter))
counter=0
for imgFile in r:
    if(os.path.exists(imgFile)):
        splitPath = os.path.split(imgFile)

        if not re.match( r'zx_', splitPath[1]):
            os.remove(imgFile)
