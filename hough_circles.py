import numpy as np 
from PIL import Image, ImageDraw 

  
img=Image.open('C:/Users/alimo/Documents/FRT/Contour Detection (Basketball)/contour-detection/test_circle.png') 
display(img) 
  
height,width = img.size 
lum_img = Image.new('L', [height,width] , 0) 
  
draw = ImageDraw.Draw(lum_img) 
draw.pieslice([(0,0), (height,width)], 0, 360,  
              fill = 255, outline = "white") 
img_arr =np.array(img) 
lum_img_arr =np.array(lum_img) 
display(Image.fromarray(lum_img_arr)) 
final_img_arr = np.dstack((img_arr,lum_img_arr)) 
display(Image.fromarray(final_img_arr))