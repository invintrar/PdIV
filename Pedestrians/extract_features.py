#!/usr/bin/python
#Copyright 2015 CVC-UAB

# extract_features.py: Extract features for a given dataset, and stores them.
# TODO: Modify Config.py to point to the location where you stored the dataset.

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Miquel Ferrarons, David Vazquez"
__copyright__ = "Copyright 2015, CVC-UAB"
__credits__ = ["Miquel Ferrarons", "David Vazquez"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Miquel Ferrarons"

from Tools import feature_extractor

from skimage import io
import os
import Config as cfg
from skimage import util

import pickle

def run():

    # Create necessary directories to save the features of the images
    if not os.path.exists(cfg.positiveFeaturesPath):
        os.makedirs(cfg.positiveFeaturesPath)
    if not os.path.exists(cfg.negativeFeaturesPath):
        os.makedirs(cfg.negativeFeaturesPath)

    #Extract features for positive samples
    print ('Extracting features from images in '+cfg.positiveInputPath)
    extractAndStoreFeatures(cfg.positiveInputPath,  cfg.positiveFeaturesPath)

    print ('Extracting features from images in '+cfg.negativeInputPath)
    #Extract features for negative samples
    extractAndStoreFeatures(cfg.negativeInputPath,  cfg.negativeFeaturesPath)


def extractAndStoreFeatures(inputFolder, outputFolder):

    #List all files
    fileList = os.listdir(inputFolder)
    #Select only files that end with .png
    imagesList = filter(lambda element: '.png' in element, fileList)

    for filename in imagesList:
        imagepath = inputFolder + '/' + filename
        outputpath = outputFolder+'/'+filename+'.feat'

        if os.path.exists(outputpath):
            print ('Features for ' + imagepath + '. Delete the file if you want to replace.')
            continue

        print ('Extracting features for ' + imagepath)

        image = io.imread(imagepath, as_grey=True)
        #Read the image as bytes (pixels with values 0-255)
        image = util.img_as_ubyte(image)

        #Extract the features
        feats = feature_extractor.extractFeatures(image)

        #Save the features to a file
        outputFile = open(outputpath, "wb")
        pickle.dump(feats, outputFile)
        outputFile.close()


if __name__ == '__main__':
    run()

