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
import pickle
from sklearn import svm
from sklearn import linear_model

import os

def loadImageFeatures(featuresPath):
    print ('Loading features from '+str(featuresPath))
    file = open(featuresPath, 'r')
    return pickle.load(file)

def run():
    #List all the files .feat in the positives directory
    positiveList = os.listdir(cfg.positiveFeaturesPath)
    positiveList = filter(lambda element: '.feat' in element, positiveList)

    #List all the files .feat in the negatives directory
    negativeList = os.listdir(cfg.negativeFeaturesPath)
    negativeList = filter(lambda element: '.feat' in element, negativeList)

    #Count how many samples we have
    positiveSamplesCount = len(positiveList)
    negativeSamplesCount = len(negativeList)
    samplesCount = positiveSamplesCount + negativeSamplesCount

    #Load the features of the first element, to obtain the size of the feature vectors.
    filepath = cfg.positiveFeaturesPath + '/'+positiveList[0]
    file = open(filepath, 'r')
    feats = pickle.load(file)
    featuresLength = len(feats)

    #Initialize the structure that we will pass to the model for training
    # X will be the samples for training
    # y will be the labels
    X = np.zeros(shape=(samplesCount, featuresLength))
    y = np.append(np.ones(shape=(1, positiveSamplesCount)),
                  -1*np.ones(shape=(1, negativeSamplesCount)))

    # Load all the positive feature vectors in X
    count = 0
    for filename in positiveList:
        filepath = cfg.positiveFeaturesPath+'/'+filename
        X[count] = loadImageFeatures(filepath)
        count += 1

    # Load all the negative feature vectors in y
    for filename in negativeList:
        filepath = cfg.negativeFeaturesPath+'/'+filename
        X[count] = loadImageFeatures(filepath)
        count += 1

    # Train the classifier with X and y, and some given parameters
    if cfg.model == 'SVM':
        print ('Training SVM....')
        model = svm.LinearSVC(C=cfg.svm_C,
                                #loss='hinge',# loss
                                penalty=cfg.svm_penalty,
                                dual=cfg.svm_dual,
                                tol=cfg.svm_tol,
                                fit_intercept=cfg.svm_fit_intercept,
                                intercept_scaling=cfg.svm_intercept_scaling)
    elif cfg.model == 'LogisticRegression':
        print ('Training linear model....')
        model = linear_model.LogisticRegression(C=cfg.logReg_C,
                                   penalty=cfg.logReg_penalty,
                                   dual=cfg.logReg_dual,
                                   tol=cfg.logReg_tol,
                                   fit_intercept=cfg.logReg_fit_intercept,
                                   intercept_scaling=cfg.logReg_intercept_scaling)
    else:
        print ('ERROR: Model can only be SVM or LogisticRegression')
        exit(0)

    model.fit(X, y)
    #Obtain the model score for the training set
    print ('MODEL score')
    print (model.score(X, y))

    #Save the model
    modelDirectory, modelFilename = os.path.split(cfg.modelPath)
    if not os.path.exists(modelDirectory):
        os.makedirs(modelDirectory)

    outputModelFile = open(cfg.modelPath, 'wb')
    pickle.dump(model, outputModelFile)

if __name__ == '__main__':
    run()