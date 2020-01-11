#!/usr/bin/python
#Copyright 2015 CVC-UAB

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

import os
import feature_extractor
import pickle
import numpy as np
from skimage import io
from skimage.util import pad
from skimage.transform import pyramid_gaussian
from skimage.util.shape import view_as_windows
import skimage.util as util
import math
import nms
import Config as cfg

import sys 
sys.path.append('/Tools/')



def testImage(imagePath, decisionThreshold = cfg.decision_threshold, applyNMS=True):

    file = open(cfg.modelPath, 'rb')
    svc = pickle.load(file, encoding='latin1')

    image = io.imread(imagePath, as_grey=True)
    image = util.img_as_ubyte(image) #Read the image as bytes (pixels with values 0-255)

    rows, cols = image.shape
    pyramid = tuple(pyramid_gaussian(image, downscale=cfg.downScaleFactor))

    scale = 0
    boxes = None
    scores = None

    for p in pyramid[0:]:
        #We now have the subsampled image in p

        #Add padding to the image, using reflection to avoid border effects
        if cfg.padding > 0:
            p = pad(p,cfg.padding,'reflect')

        try:
            views = view_as_windows(p, cfg.window_shape, step=cfg.window_step)
        except ValueError:
            #block shape is bigger than image
            break

        num_rows, num_cols, width, height = views.shape
        for row in range(0, num_rows):
            for col in range(0, num_cols):

                #Get current window
                subImage = views[row, col]
                #Extract features
                feats = feature_extractor.extractFeatures(subImage)
                #Obtain prediction score
                decision_func = svc.decision_function(np.array(feats).reshape(1, -1))

                if decision_func > decisionThreshold:
                    # Pedestrian found!
                    h, w = cfg.window_shape
                    scaleMult = math.pow(cfg.downScaleFactor, scale)

                    x1 = int(scaleMult * (col*cfg.window_step - cfg.padding + cfg.window_margin))
                    y1 = int(scaleMult * (row*cfg.window_step - cfg.padding + cfg.window_margin))
                    x2 = int(x1 + scaleMult*(w - 2*cfg.window_margin))
                    y2 = int(y1 + scaleMult*(h - 2*cfg.window_margin))

                    bbox = (x1, y1, x2, y2)
                    score = decision_func[0]

                    if boxes is not None:
                        boxes = np.vstack((bbox, boxes))
                        scores = np.hstack((score, scores))
                    else:
                        boxes = np.array([bbox])
                        scores = np.array([score])
        scale += 1

    if applyNMS:
        #From all the bounding boxes that are overlapping, take those with maximum score.
        boxes, scores = nms.non_max_suppression_fast(boxes, scores, cfg.nmsOverlapThresh)

    return boxes, scores


def testFolder(inputfolder, outputfolder, decisionThreshold = cfg.decision_threshold, applyNMS=True):

    fileList = os.listdir(inputfolder)
    imagesList = filter(lambda element: '.png' in element, fileList)

    print ('Start processing '+inputfolder)
    for filename in imagesList:

        imagepath = inputfolder + '/' + filename
        print ('Processing '+imagepath)

        #Test the current image
        bboxes, scores = testImage(imagepath, decisionThreshold=decisionThreshold, applyNMS=applyNMS)

        #Store the result in a dictionary
        result = dict()
        result['imagepath'] = imagepath
        result['bboxes'] = bboxes
        result['scores'] = scores

        #Save the features to a file using pickle
        outputFile = open(outputfolder+'/'+filename+'.results', "wb")
        pickle.dump(result, outputFile)
        outputFile.close()
