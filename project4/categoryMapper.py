# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:02:38 2019

@author: Sowmya
Modified by Dijiang Huang, 4/19/2020
"""

import numpy as np
import pandas as pd
import random
import os

# Define variables
file_extension='.csv'  # .csv or .txt
#file_folder='NSL-KDD/'
file_folder='scenario_c/'
# load files and content into X
fileToStandardize = input("Please enter the file to be standardized without the extension\n")
dataset = pd.read_csv(file_folder + fileToStandardize + file_extension, header=None, encoding="ISO-8859-1")
X = dataset.iloc[:, :].values

# the number of features equals to the number of columns of the loaded file
nFeatures = len(X[0])
print("Extracting String Columns....")

stringColumns = []
i = random.randint(10, 100) #Just choose a row at random (a value between 10 and 100) to check for string columns
for j in range(nFeatures):
    try:
        floatValue = float(X[i, j])
    except: 
        stringColumns.append(j)
print("String Columns are : " + str(stringColumns)) # print string column indexes starting from 0


shouldSaveFeatureMappings = input("Do you want to save feature mappings result[y/n]?")
if shouldSaveFeatureMappings == 'y':
    directory_featureMapping = input("What local directory to store the created feature mappings?\n")
    if not os.path.exists(directory_featureMapping):
        os.mkdir(directory_featureMapping)
    print("************************************************")
    # the for loop store each string column into a file with name of the column index
    for j in stringColumns:
        distinctValues = []
        featureMap = []
        print("Distinct values for feature index " + str(j) + " are: ")
        for i in range(len(X)):
            if X[i, j] not in distinctValues:
                distinctValues.append(str(X[i, j]))
                featureMap.append(str(X[i, j]) + ", " + str(len(distinctValues)-1))
                #If header exists prints, feature name, else prints feature value as an example
                print(str(distinctValues))
                if shouldSaveFeatureMappings == 'y':
                    featureMapFile = directory_featureMapping+"/" + str(j) + file_extension
                    np.savetxt(featureMapFile, np.array(featureMap), delimiter=',', fmt="%s")
                    print(featureMapFile + " has been saved for column index " + str(j))
                    print("************************************************")
    # the following if converts the original data file into a standardized file by replacing strings to their indexing ID
    shouldContinue = input("Do you want to standardize the given input file?[y/n/]?")
    if shouldContinue == 'y':
        #featuresMappingsFolder = input("Please enter the path to the featureMappings folder\n")
        print("Now, Standardizing.....")    
        for j in stringColumns:
            featureMapping = (pd.read_csv(directory_featureMapping + "/" + str(j) + file_extension, header=None, encoding="ISO-8859-1")).iloc[:, :].values
            for i in range(len(X)):   
                for k in range(len(featureMapping)):
                    if str.lower(str(X[i, j])) == str.lower(str(featureMapping[k, 0])):
                        X[i, j] = featureMapping[k, 1]

        print("Creating standardized file.....")
        standardizedFile = file_folder + fileToStandardize + "_standardized"+file_extension
        np.savetxt(standardizedFile, np.array(X), delimiter=',', fmt="%s")
        print("*********************************************")
        print("Standardized file " + standardizedFile + " has been created")
    else:
        print("Execution completed")
else:
    print("Quit")
    
