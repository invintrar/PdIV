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

import pickle
import os.path
from skimage import io
from Tools import drawing
import Config as cfg
from PIL import Image
import numpy as np
import nms

def run():
    fileList = os.listdir(cfg.resultsFolder)
    resultsFileList = filter(lambda element: '.result' in element, fileList)

    for resultsFile in resultsFileList:

        resultsFilePath = cfg.resultsFolder + '/' +resultsFile
        file = open(resultsFilePath, 'rb')
        imageResults = pickle.load(file)

        boxes = imageResults['bboxes']
        scores = imageResults['scores']
        imagepath = imageResults['imagepath']

        filename = os.path.basename(imagepath)
        if boxes is None:
            print ('No pedestrians found for image '+imagepath)
            continue

        print ('Saving results for image '+filename)

        idx = np.where(scores > cfg.decision_threshold)
        boxes = boxes[idx]
        scores = scores[idx]

        boxes, scores = nms.non_max_suppression_fast(boxes, scores, overlapthresh= cfg.nmsOverlapThresh)

        img = Image.open(imagepath)
        #Show the results on a colored image
        img = drawing.drawResultsOnImage(img, boxes, scores)
        img.save('Results/'+filename,"PNG")

        file.close()

    print ('Finished!')

if __name__ == '__main__':
    run()