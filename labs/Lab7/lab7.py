import PIL
from PIL import Image
from PIL import ImageFilter
#this loads the image into memory for manipulation
image = Image.open("corgi.jpg")

#bluring an image
blurredimage = image.filter(ImageFilter.GaussianBlur())
blurredimage.show()

#making image greyscale
greyscaleimage = image.convert('L')


#creating a half and half image
##creating new image
combinedimage = Image.new('RGB', (image.width, image.height))

##cropping images
cropped_left = image.crop((0, 0, image.width/2, image.height))
cropped_right = greyscaleimage.crop((image.width/2, 0, image.width, image.height))

##inputing new part of images
combinedimage.paste(cropped_left, (0,0))
combinedimage.paste(cropped_right , (cropped_left.width,0))
combinedimage.show()