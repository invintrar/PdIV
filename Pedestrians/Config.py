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

#############################
# FEATURE extraction settings
#############################

#featuresToExtract = ['HOG']
featuresToExtract = ['LBP']
#featuresToExtract = ['HOG', 'LBP']

# LBP Parameters
lbp_win_shape = (16, 16)
lbp_win_step = int(lbp_win_shape[0]/2)
lbp_radius = 1
lbp_n_points = 8 * lbp_radius
lbp_METHOD = 'nri_uniform'
lbp_n_bins = 59 # NRI uniform LBP has 59 values

# HOG Parameters
hog_orientations = 9
hog_pixels_per_cell = (8, 8)
hog_cells_per_block = (2, 2)
hog_normalise = True

##################
# DATASET Settings
##################

#TODO: Modify datasetRoot to point to your training dataset.
datasetRoot = 'Datasets/Pedestrians-Dataset'

positive_folder = 'Pedestrians/'
negative_folder = 'Background/'

#Locatiom of the positive and negative sample images
positiveInputPath = datasetRoot+'/'+positive_folder
negativeInputPath = datasetRoot+'/'+negative_folder

#Location to store the features of of the positive and negative sample images
featuresFolder = '-'.join(featuresToExtract)
positiveFeaturesPath = 'Features/'+featuresFolder+'/'+positive_folder
negativeFeaturesPath = 'Features/'+featuresFolder+'/'+negative_folder

#TODO: Modify testFolderPath and annotationsFolderPath to point
#TODO: to your location of the test and annotations folders
testFolderPath = '/Datasets/INRIA_dummy/Test/FramesPos'
annotationsFolderPath = '/Datasets/INRIA_dummy/Test/Annotations'
resultsFolder = '/Results/'

#################
# MODEL settings
#################

#model = 'SVM'  # 'SVM' or 'LogisticRegression'
model = 'LogisticRegression'
# Location of the model

modelFeatures = '-'.join(featuresToExtract)
modelPath = 'Models/'+model+'_'+modelFeatures+'.model'

# SVM.LinearSVC parameters
svm_C = 0.01
svm_penalty = 'l2'
svm_dual = False
svm_tol = 0.0001
svm_fit_intercept = True
svm_intercept_scaling = 100

# LogisticRegression parameters
logReg_C = 1.0
logReg_penalty = 'l2'
logReg_dual = False
logReg_tol = 0.0001
logReg_fit_intercept = True
logReg_intercept_scaling = 100

##############################
# TEST settings
##############################

# Size of windows for the sliding window on the test images
window_shape = (128, 64)
window_margin = 16
window_step = 32

#Decision threshold for the classification
decision_threshold = 0. # Default, if not matching any combination of [HOG-LBP]-[SVM-LogisticRegression]
if model is 'SVM':
    if 'HOG' in featuresToExtract and 'LBP' in featuresToExtract:
        decision_threshold = 1.2  # for SVM-HOG-LBP
    elif 'HOG' in featuresToExtract:
        decision_threshold = 1.2  # for SVM-HOG
    elif 'LBP' in featuresToExtract:
        decision_threshold = 1.2  # for SVM-LBP
elif model is 'LogisticRegression':
    if 'HOG' in featuresToExtract and 'LBP' in featuresToExtract:
        decision_threshold = 3.5  # for SVM-HOG-LBP
    if 'HOG' in featuresToExtract:
        decision_threshold = 3.5  # for LogisticRegression-HOG
    elif 'LBP' in featuresToExtract:
        decision_threshold = 8.2  # for LogisticRegression-LBP

#Downscale factor for the pyramid
downScaleFactor = 1.2

#Padding added to the test images. Used to detect pedestrians at the border of the image.
padding = 16

#Non-Maximum suppression overlap threshold
#   Two bounding boxes are considered the same
#   if their overlapping percentage exceeds this value.
nmsOverlapThresh = 0.5

#Values used in evaluation
decision_threshold_min = -2
decision_threshold_max = 10
decision_threshold_step = 0.1

#Percentage that the detections and the annotations have to overlap, to consider a detection correct.
annotation_min_overlap = 0.5

