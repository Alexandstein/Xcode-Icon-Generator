#!/usr/bin/env python

import sys
from PIL import Image
from os import path
import glob, os
import argparse

class IconType(object):
    #The output format of the filenames
    fileNameFormat = "{0}_{1}pt@{2}x.png"

    #icon sizes in Pts
    macIconSizes = [512, 256, 128, 32, 16]
    iOSIconSizes = [83.5, 76, 40, 29, 60, 40, 29]

    #Mapping from icon sizes to resolutions
    macIconResolutions = {
        512 : [1, 2],
        256 : [1, 2],
        128 : [1, 2],
        32 : [1, 2],
        16 : [1, 2]
    }

    #Mapping from icon sizes to resolutions
    iOSIconResolution = {
        83.5 : [2],
        76 : [1,2],
        40 : [1,2,3],
        29 : [1,2],
        60 : [2,3],
        29 : [2,3]
    }

    #Creates a string which with act as the icon's name
    #
    #Parameter :
    #   - baseName : the base image's name
    #   - imageSize : the image size in pts
    #   - resolution : the image resolution
    @staticmethod
    def getIconName(baseName, imageSize, resolution):
        output = IconType.fileNameFormat.format(baseName, imageSize, resolution)
        return output

####################
#Important Constants
####################

#Image needs to be at least 1024 pixel
MIN_IMAGE_SIZE = 1024

#Default output directory
OUTPUT_DIR = "IconGenTumbnails"
OUTPUT_DIR_MACOS = OUTPUT_DIR + "/macOS"
OUTPUT_DIR_IOS = OUTPUT_DIR + "/iOS"

#Helper function generates and writes out images
def generateIcon(baseFileName, size, resolution, outputDir = OUTPUT_DIR):
    iconFileName = IconType.getIconName(imageBaseName, size, resolution)
    print("Generating icon: " + iconFileName)

    newImageSize = int(resolution * size)
    newImage = sourceImage.resize((newImageSize, newImageSize), Image.ANTIALIAS)
    newImage.save(outputDir + '/' + iconFileName, 'png')

if __name__ == "__main__":
    #Checks for argument in command line
    sourceImage = None
    targetPath = ""
    try:
        targetPath = path.abspath(sys.argv[1])
    except:
        print('Usage: iconGen <path to image to be processed>')
        exit()

    print('Opening image...' + str(path.splitext(path.basename(targetPath))))
    #Get an image object
    if path.isfile(targetPath):
        try:
            sourceImage = Image.open(targetPath)
        except:
            print('Error: Failed to open image')
            exit()
    else:
        print('Error: Not a proper image file')

    #Run some checks on the file to make sure image is properly formatted
    print('Validating image properties...')
    #Check whether square
    if (sourceImage.size[0] != sourceImage.size[1]):
        print('Error: Image must be square')
        exit()
    if (sourceImage.size[0] < MIN_IMAGE_SIZE):
        print('Error: Image too small; must be at least 1024x1024 px')
        exit()


    #Now to start doing work with the images...
    #Save the current working directory to navigate back to later
    savedCurrentDir = os.getcwd()

    #Navigate to the source image's path to work in
    os.chdir(path.dirname(targetPath))
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR_MACOS)
        os.makedirs(OUTPUT_DIR_IOS)

    imageBaseName = path.splitext(path.basename(targetPath))[0]
    #newIm = sourceImage.resize((200,200),Image.ANTIALIAS)
    #newIm.save(OUTPUT_DIR + "/snurge.png", 'png')

    #Generate macOS icons
    for size in IconType.macIconSizes:
        for resolution in IconType.macIconResolutions[size]:
            generateIcon(imageBaseName, size, resolution, OUTPUT_DIR_MACOS)

    #Generate iOSIcons
    for size in IconType.iOSIconSizes:
        for resolution in IconType.iOSIconResolution[size]:
            generateIcon(imageBaseName, size, resolution, OUTPUT_DIR_IOS)

    #Do cleanup; reset directory
    os.chdir(savedCurrentDir)
