# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:03:56 2019

Load and Manipulate images with PIL/Pillow

"""

file_name = 'images/mamamoo.jpg'

## load and show an image with Pillow
#from PIL import Image
## load the image
#image = Image.open(file_name)
## summarize some details about the image
#print(image.format)
#print(image.mode)
#print(image.size)
## show the image
#image.show()

## Load and display an image with Matplotlib
#from matplotlib import image
#from matplotlib import pyplot
## load image as pixel array
#data = image.imread(file_name)
## summarize shape of the pixel array
#print(data.dtype)
#print(data.shape)
## display the array of pixels as an image
#pyplot.imshow(data)
#pyplot.show()

##### Convert image to NumPy Arrays

## load image & convert to and from Numpy array
#from PIL import Image
#from numpy import asarray
##load the image
#image = Image.open(file_name)
## convert image to numpy array
#data = asarray(image)
## summarize shape
#print(data.shape)
## create Pillow image
#image2 = Image.fromarray(data)
## summarize image details
#print(image2.format)
#print(image2.mode)
#print(image2.size)

## load all images in a directory
#from os import listdir
#from matplotlib import image
## load all images in a directory
#loaded_images = list()
#for filename in listdir('images'):
#    # load image
#    img_data = image.imread('images/' + filename)
#    # store loaded image
#    loaded_images.append(img_data)
#    print('> loaded %s %s' % (filename, img_data.shape))

##### Save image

## Save an image in another format
#from PIL import Image
## load the image
#image = Image.open(file_name)
## save as PNG format
#image.save('images/mamamoo.gif', format = 'GIF')
## load the image again and inspect the format
#image3 = Image.open('images/mamamoo.GIF')
#print(image3.format)
#image3.show()

##### Grayscale image

## Saving a grayscale version of a loaded image
#from PIL import Image
## load the image
#image = Image.open(file_name)
## convert the image to grayscale
#gs_image = image.convert(mode='L')
## save in jpeg format
#gs_image.save('images/mamamoo_greyscale.jpg')
## load the image again and show it
#image4 = Image.open('images/mamamoo_greyscale.jpg')
## show the image
#image4.show()

##### Resize image

## Create a thumbnail of an image
#from PIL import Image
## load the image
#image = Image.open(file_name)
## report the size of the image
#print(image.size)
## create a thumbnail and preserve aspect ratio
#image.thumbnail((200,200))
## save the image
#image.save('images/mamamoo_resized.jpg')
## show the image
#image.show()
## report the size of the thumbnail
#print(image.size)

## Resize image and force a new shape
#from PIL import Image
## load the imge
#image = Image.open(file_name)
## report the size of the image
#print(image.size)
## resize image and ignore original aspect ratio
#img_resized = image.resize((200,200))
## save the image
#image.save('images/mamamoo_resized.jpg')
## show the image
#img_resized.show()
## report the size of thumbnail
#print(img_resized.size)

##### Flip image

## Create flipped versions of an image
#from PIL import Image
#from matplotlib import pyplot
## load image
#image = Image.open(file_name)
## horizontal flip
#hoz_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
#hoz_flip.save('images/mamamoo_hozflip.jpg')
## vertical flip
#ver_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
#ver_flip.save('images/mamamoo_verflip.jpg')
## plot all three images using matplotlib
#pyplot.subplot(311)
#pyplot.imshow(image)
#pyplot.subplot(312)
#pyplot.imshow(hoz_flip)
#pyplot.subplot(313)
#pyplot.imshow(ver_flip)
#pyplot.show()

##### Rotate image

#from PIL import Image
#from matplotlib import pyplot
## load image
#image = Image.open(file_name)
## plot original image
#pyplot.subplot(311)
#pyplot.imshow(image)
## rotate 45 degrees
#pyplot.subplot(312)
#pyplot.imshow(image.rotate(45))
## rotate 90 degree
#pyplot.subplot(313)
#pyplot.imshow(image.rotate(90))
#pyplot.show()

##### Cropped image

#from PIL import Image
## load image
#image = Image.open(file_name)
## create a cropped image
#cropped = image.crop((350,30,480,180))
## show cropped image
#cropped.show()






