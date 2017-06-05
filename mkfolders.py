import os
import sys
import shutil

if __name__ == '__main__':
  search_dir = sys.argv[1]
  files = os.listdir(search_dir)
  imgs = []
  for f in files:
    ig = f.lower()
    wasfound = ig.find('.jpg') > -1 or ig.find('.png') > -1
    if wasfound:
      imgs.append(f)
  month = 4
  day = 26
  year = 2017
  idx = 0

  for i in range(day, 31):
    prev_date = `month` + "." + `i - 1` + "." + `2017`
    date = `month` + "." + `i` + "." + `2017`
    img_loc = search_dir + "/" + imgs[idx]
    ext = img_loc.split('.')
    img_dest = date + "/sketch." + ext[1]
    shutil.copytree(prev_date, date) 
    if os.path.exists(date + "/sketch.jpg"):
      os.remove(date + "/sketch.jpg")
    else:
      os.remove(date + "/sketch.PNG")
    shutil.move(img_loc, img_dest)
    idx += 1
    print img_loc
    print img_dest
    
