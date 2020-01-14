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

import detector
import drawing
from PIL import Image
import matplotlib.pyplot as plt
import platform
def run():
    imagePath = 'C:/Users/Darwin/Documents/GitHub/PdIV/Pedestrians/Images/Image001.png'
    bboxes, scores = detector.testImage(imagePath, applyNMS=True)

    img = Image.open(imagePath)
    img = drawing.drawResultsOnImage(img, bboxes, scores)

    if platform.system() is 'Windows':
        plt.imshow(img) #img.show() does not work properly on windows. We upse matplotlib.imshow instead
        plt.show()
    else:
        img.show()

if __name__ == '__main__':
    run()

