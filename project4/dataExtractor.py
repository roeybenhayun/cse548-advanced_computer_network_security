# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:02:38 2019

@author: Sowmya
Modified by Dijiang Huang 4/19/2020
"""
import numpy as np
import pandas as pd

# Define variables
# Data file Path
DatasetPath='NSL-KDD/'
# Data file name
input_train = "KDDTrain+.txt"
input_test = "KDDTest+.txt"
file_extension = '.csv'  # .csv or .txt
num_attack_class = 4 # total number of attack classes

#All attacks in NSL-KDD classed based on their attack classes: DoS, Prob, U2R, and R2L
attacks_subClass = [['apache2', 'back', 'land', 'neptune', 'mailbomb', 'pod', 'processtable', 'smurf', 'teardrop', 'udpstorm', 'worm'], 
     ['ipsweep', 'mscan', 'portsweep', 'saint', 'satan','nmap'],
     ['buffer_overflow', 'loadmodule', 'perl', 'ps', 'rootkit', 'sqlattack', 'xterm'],
     ['ftp_write', 'guess_passwd', 'httptunnel', 'imap', 'multihop', 'named', 'phf', 'sendmail', 'snmpgetattack', 'spy', 'snmpguess', 'warezclient', 'warezmaster', 'xlock', 'xsnoop']
     ]

# Set1 is selected attack classes
training_attack_class_list = []
# Set2 is removed attack classes
testing_attack_class_list = []
attack_class_1 = list(map(int, input("(Training Dataset) Please enter the attack class(es) that you want from the below list:\n(Note that you can choose one or multiple classes, e.g., 1 3,  and input 0 means nothing is chosen) \na1 -> DoS (Enter 1 for this selection)\na2 -> Probe (Enter 2 for this selection)\na3 -> U2R (Enter 3 for this selection)\na4 -> R2L (Enter 4 for this selection)\n\n").split()))
attack_class_2 = list(map(int, input("(Testing Dataset) Please enter the attack class(es) that you want from the below list:\n(Note that you can choose one or multiple classes, e.g., 1 3,  and input 0 means nothing is chosen) \na1 -> DoS (Enter 1 for this selection)\na2 -> Probe (Enter 2 for this selection)\na3 -> U2R (Enter 3 for this selection)\na4 -> R2L (Enter 4 for this selection)\n\n").split()))
training_attack_class_list.append(attack_class_1)
testing_attack_class_list.append(attack_class_2)

print("Loading", input_train, "and", input_test, "files from the current folder where this script resides.....\n")
dataset_train = pd.read_csv(DatasetPath + input_train, header=None, encoding="ISO-8859-1")
dataset_test = pd.read_csv(DatasetPath + input_test, header=None, encoding="ISO-8859-1")
print("Loading Completed !\n")

X_train = dataset_train.iloc[:, :].values
X_test = dataset_test.iloc[:, :].values

print("Creating training set.....\n")
setA_train = []
# the following for loop choose selected attack classes and normal labeled data and put them into the setA_train.
if training_attack_class_list[0][0] != 0 and len(training_attack_class_list[0]) != num_attack_class:
    for i in range(len(X_train)):
        # exp., X_train[i, -2] is the label of attack subclass, and attacks_subClass[training_attack_class_list[0][j]-1] identify the selected attack class
        if str.lower(str(X_train[i,-2])) == 'normal':
            setA_train.append(X_train[i])
        for j in range(len(training_attack_class_list[0])):
            if str.lower(str(X_train[i, -2])) in attacks_subClass[training_attack_class_list[0][j]-1]:
                setA_train.append(X_train[i])
    trainingFileName="Training"
    for i in range(len(training_attack_class_list[0])):
        trainingFileName = trainingFileName + "-a" + str(training_attack_class_list[0][i])
    trainingFileName = trainingFileName + file_extension
    np.savetxt(trainingFileName, setA_train, delimiter=',', fmt="%s" )
    print("Files " + trainingFileName + " have been created in the same folder this script resides\n")
elif len(training_attack_class_list[0]) == num_attack_class:
    print("No changes is needed for training dataset!\n")
else:
    print("No attack classes are chosen, thus no new training file is created!\n")
        
print("Creating testing set.....\n")    
setA_test = []
# the following for loop choose selected attack classes and normal labeled data and put them into the setA_train.
if testing_attack_class_list[0][0] != 0 and len(testing_attack_class_list[0]) != num_attack_class:
    for i in range(len(X_test)):
        # exp., X_train[i, -2] is the label of attack subclass, and attacks_subClass[training_attack_class_list[0][j]-1] identify the selected attack class
        if str.lower(str(X_test[i,-2])) == 'normal':
            setA_test.append(X_test[i])
        for j in range(len(testing_attack_class_list[0])):
            if str.lower(str(X_test[i, -2])) in attacks_subClass[testing_attack_class_list[0][j]-1]:
                setA_test.append(X_test[i])
    testingFileName="Testing"
    for i in range(len(testing_attack_class_list[0])):
        testingFileName = testingFileName + "-a" + str(testing_attack_class_list[0][i])
    testingFileName = testingFileName + file_extension
    np.savetxt(testingFileName, setA_test, delimiter=',', fmt="%s" )
    print("Files " + testingFileName + " have been created in the same folder this script resides\n")
elif len(testing_attack_class_list[0]) == num_attack_class:
    print("No changes is needed for testing dataset!\n")
else:
    print("No attack classes are chosen, thus no new training file is created!\n")