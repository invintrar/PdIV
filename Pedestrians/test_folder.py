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

from Tools import detector
import Config as cfg
import pickle
import os
def run():

    #Create the results directory if it doesn't exist
    if not os.path.exists(cfg.resultsFolder):
        os.makedirs(cfg.resultsFolder)

    # As we will later filter out the results for different thresholds,
    # we don't apply NMS here, and we set the threshold to a low value,
    # so we get more detections that we can filter later when doing the
    # evaluation for different thresholds.
    detector.testFolder(cfg.testFolderPath,
                        cfg.resultsFolder,
                        decisionThreshold=cfg.decision_threshold_min,
                        applyNMS=False)



if __name__ == '__main__':
    run()

