from PIL import Image
import os
 
for f in os.listdir('images'):
    
    # In my case i have all images in jpg format, you can change it according your requirment
     if f.endswith('.jpg'):
         
    #Create a image specific object
       image=Image.open('images/{}'.format(f))

    #Create a copy of image for safety 
       image.copy()
       fname,fexten=os.path.splitext(f)

       if not os.path.exists('B&W images'):
           os.mkdir('B&W images')

    #Applying black&white filter on copy image
       image=image.convert(mode='L')

    #Save those as .png format
       image.save('B&W images/{}.png'.format(fname))


