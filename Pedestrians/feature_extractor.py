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
import Config as cfg
from skimage.feature import hog
from skimage.feature import local_binary_pattern
from skimage.util import view_as_windows

import sys 
sys.path.append('C:/Users/Darwin/Documents/GitHub/PdIV/Pedestrians/')



def extractFeatures(img):

    feats = []
    if 'LBP' in cfg.featuresToExtract:
        lbpFeats = extractLBPfeatures(img)
        feats.extend(lbpFeats)
    if 'HOG' in cfg.featuresToExtract:
        hogFeats = extractHOGfeatures(img)
        feats.extend(hogFeats)
    return feats

def extractLBPfeatures(img):

    lbp = local_binary_pattern(img, cfg.lbp_n_points, cfg.lbp_radius, cfg.lbp_METHOD)
    #lbpin=lbp.astype('Int64')
    lbp_windows = view_as_windows(lbp, window_shape=cfg.lbp_win_shape, step=cfg.lbp_win_step)
    features = []
    count = 0
    for windows_list in lbp_windows:
        for window in windows_list:
            lbp_hist, bin_edges = np.histogram(window, bins=cfg.lbp_n_bins)
            lbp_hist_norm = sum(abs(lbp_hist))
            lbp_hist_l1sqrtnorm = np.sqrt(lbp_hist/float(lbp_hist_norm))
            features.append(lbp_hist_l1sqrtnorm)
            count += 1
    features_flatten = [item for sublist in features for item in sublist]
    return features_flatten

def extractHOGfeatures(img):

    fd = hog(img,
             orientations=cfg.hog_orientations,
             pixels_per_cell=cfg.hog_pixels_per_cell,
             cells_per_block=cfg.hog_cells_per_block,
             visualize=False)
    return fd