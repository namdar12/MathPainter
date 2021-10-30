import numpy as np
from PIL import Image

data = np.zeros((5,4,3), dtype=np.uint8)  # create a 3d numpy array of zeros, then replace zeros with
                        #np zeros takes a tuple as an argument, with the three variables as the dimensions of the matrix
                        #Heigh, width, and depth
data[:] = [255,255,0] # replace each 0s in the array with 255, 255 and 0 to give yellow
# the marix is 5 height, 4 width, and 3 depth, i.e 5 pixels height, 4 pixels long, and the 3 pixels deep

#make a red patch
data[1:3] = [255,0,0] #this will update rows 1 and 2

#make a red patch for the columns
data[:,1:3] = [255,0,0] # this will change the columns 1 and 2 for each row.

#make a small green patch in the middle
data[1:3,1:3] = [0,255,0] #This will make a green path at rows 1 and 2/ columns 1 and 2


img = Image.fromarray(data,'RGB')
img.save('canvas.png')
