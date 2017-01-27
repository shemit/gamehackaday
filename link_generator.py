import os 
if __name__ == '__main__':
  dirs = os.listdir('.')
  gen_dirs = []
  for afile in dirs:
    if (os.path.isdir(afile)) and afile != "lib" and afile != ".git":
      gen_dirs.append(afile)
  
