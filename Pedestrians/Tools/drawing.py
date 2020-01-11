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
from PIL import Image, ImageDraw, ImageFont, ImageChops

def drawResultsOnImage(img, boxes, scores, bboxColorRGB =(0, 255, 0)):

    boxcount = 0

    draw = ImageDraw.Draw(img)
    textSize=20
    fnt = ImageFont.truetype(os.getcwd()+'/fonts/FreeMonoBold.ttf', textSize)

    #Draw a bounding box with color bbocColorBGR for every detection in bboxes
    #Draw also the score of that bounding box in it's top-left corner
    for bbox in boxes:
        x1 = bbox[0]
        y1 = bbox[1]
        x2 = bbox[2]
        y2 = bbox[3]

        # Remark the object with a rectangle, and draw the text
        draw.line((x1, y1, x2, y1), fill=bboxColorRGB, width=2)
        draw.line((x2, y1, x2, y2), fill=bboxColorRGB, width=2)
        draw.line((x2, y2, x1, y2), fill=bboxColorRGB, width=2)
        draw.line((x1, y2, x1, y1), fill=bboxColorRGB, width=2)

        #Obtain the score and take it's 4 first decimals
        if scores is not None:
            score = scores[boxcount]
            scoreText = "{0:.4f}".format(score)
            draw.text((x1, y1), scoreText, fill=(255, 255, 255, 255), font=fnt)
            boxcount += 1

    return img