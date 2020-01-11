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

import extract_features
import train_model
import test_image
import test_folder
import show_results
import evaluate_results


extract_features.run() #Extracts the features for all the images
train_model.run() #Train the classifier

#Tests a single image and shows the results
#test_image.run()

#Test a whole folder
test_folder.run()
show_results.run() #Saves the resulting images
evaluate_results.run()# Runs the evaluation
