##############################
# Requirements:
# Python 2.7.x

# Python packages:
#	scikit-image
#	scikit-learn
#	PIL
##############################


##############################
# WINDOWS
# (Recomended installation)
##############################

# Download and install Mini-Conda: http://conda.pydata.org/miniconda.html
# Download and install Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/
# Download and install latest Python 2 release https://www.python.org/downloads/

# Open a console (cmd)
conda install scikit-image
conda install scikit-learn
conda install PIL

##############################
# Ubuntu / Debian
# (Recomended installation)
##############################

# Download Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/

sudo apt-get install scikit-image
sudo apt-get install scikit-learn
sudo apt-get install PIL

# Import the project to Pycharm

# In Pycharm, set Project interpreter as Conda-python 2.7
# Go to File-> Settings -> Project Interpreter and select python.exe from miniconda (Default C:/Miniconda/python.exe)

##############################
# Ubuntu / Debian
# (Recomended installation)
##############################

# Download Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/

sudo apt-get install scikit-image
sudo apt-get install scikit-learn
sudo apt-get install PIL


##############################
# MacOSx
# (Recomended installation)
##############################

# Download Pycharm Community Edition: https://www.jetbrains.com/pycharm/download/

sudo easy_install scikit-image
sudo easy_install scikit-learn
sudo easy_install PIL

---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------

# FIRST Steps:
	- Run file test_image.py: It will run the detection algorithm on a single image, and show the results.

# Main files description:

    # Config.py: Contains the configuration of the whole project. You can set here the location of your dataset, and other projects.

    # main.py: Runs all the pipeline:
        - Extracts features for the images in the dataset
        - Trains the classifier
        - Tests a folder and stores the results
        - Draws the results
        - Evaluates the results

    # extract_features.py: Extracts features for the images in the dataset specified in Config.py
    # train_model.py: Trains a model (SVM or LinearRegression) with the features extracted from extract_features.py
    # test_image.py: Tests a single image
    # test_folder.py: Tests a folder (specified in Config.testFolderPath) and stores the results for every image in Results/*.result
    # show_results.py: Using the results from test_folder, draws the bounding boxes on the images and stores them in Results/*.png
    # evaluate_results: Using the results from test_folder, runs the evaluation framework.