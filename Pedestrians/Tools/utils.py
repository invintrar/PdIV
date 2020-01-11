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

import numpy as np

# Reads the annotations in the INRIA format [XC, YC, W, H]
#   XC: Center of the pedestrian in X
#   YC: Center of the pedestrian in Y
#    W: Width of the window
#    H: Height of the window
#
# And returns the bounging boxes as [TLx,TLy,BRx,BRy]
#   TLx :Top-Left X,
#   TLy :Top-Left Y,
#   BRx :Bottom-Right X,
#   BRy :Bottom-Right y,
def readINRIAAnnotations(annotationsPath):

    annotatedBoxes = None

    with open(annotationsPath,'r') as fp:
        for line in fp:

            #Inria annotates the center of the pedestrian, and the width and height
            xc, yc, w, h, string = line.split(' ')

            x1 = float(xc) - float(w)/2
            y1 = float(yc) - float(h)/2
            x2 = float(x1) + float(w)
            y2 = float(y1) + float(h)

            bbox = (x1, y1, x2, y2)

            if annotatedBoxes is not None:
                annotatedBoxes = np.vstack((bbox, annotatedBoxes))
            else:
                annotatedBoxes = np.array([bbox])
    return annotatedBoxes
