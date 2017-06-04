import os
import sys
import shutil

if __name__ == '__main__':
  search_dir = sys.argv[1]
  files = os.listdir(search_dir)
  imgs = []
  for f in files:
    if f.find('.jpg'):
      imgs.append(f)
  
  month = 4
  day = 2
  year = 2017
  idx = 0

  for i in range(day, 15):
    prev_date = `month` + "." + `i - 1` + "." + `2017`
    date = `month` + "." + `i` + "." + `2017`
    img_loc = search_dir + "/" + imgs[i]
    img_dest = date + "/sketch.jpg"
    shutil.copytree(prev_date, date) 
    os.remove(date + "/sketch.jpg")
    shutil.move(img_loc, img_dest)
    print img_loc
    print img_dest
    
