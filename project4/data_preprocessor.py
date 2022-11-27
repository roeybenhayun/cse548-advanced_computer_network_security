# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:36:17 2020

@author: created by Sowmya Myneni and updated by Dijiang Huang
"""
import numpy as np
import pandas as pd
from keras.utils import np_utils
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


def merge_test_train(test_category_path, train_category_path,merge_out_path):
    
    # get the test categorical features
    test_temp1 = pd.read_csv(test_category_path + "1.csv", header=None)
    test_temp2 = pd.read_csv(test_category_path + "2.csv", header=None)
    test_temp3 = pd.read_csv(test_category_path + "3.csv", header=None)
    test_temp41 = pd.read_csv(test_category_path + "41.csv", header=None)

    test_temp1 = test_temp1.drop(test_temp1.columns[1],axis=1)
    test_temp2 = test_temp2.drop(test_temp2.columns[1],axis=1)
    test_temp3 = test_temp3.drop(test_temp3.columns[1],axis=1)            
    test_temp41 = test_temp41.drop(test_temp41.columns[1],axis=1)   

    # get the train categorical features
    train_temp1 = pd.read_csv(train_category_path + "1.csv", header=None)
    train_temp2 = pd.read_csv(train_category_path + "2.csv", header=None)
    train_temp3 = pd.read_csv(train_category_path + "3.csv", header=None)
    train_temp41 = pd.read_csv(train_category_path + "41.csv", header=None)

    train_temp1 = train_temp1.drop(train_temp1.columns[1],axis=1)
    train_temp2 = train_temp2.drop(train_temp2.columns[1],axis=1)
    train_temp3 = train_temp3.drop(train_temp3.columns[1],axis=1)
    train_temp41 = train_temp41.drop(train_temp41.columns[1],axis=1)
    

    # Merge test and train. Default is inner merge
    test_train_1 = pd.merge(test_temp1, train_temp1, how='inner')
    test_train_2 = pd.merge(test_temp2, train_temp2, how='inner')
    test_train_3 = pd.merge(test_temp3, train_temp3, how='inner')
    test_train_41 = pd.merge(test_temp41, train_temp41, how='inner')

    print(test_train_1.shape[0])
    print(test_train_2.shape[0])
    print(test_train_3.shape[0])
    print(test_train_41.shape[0])


    a1 = np.arange(test_train_1.shape[0])
    a2 = np.arange(test_train_2.shape[0])
    a3 = np.arange(test_train_3.shape[0])
    a41 = np.arange(test_train_41.shape[0])
    

    np.random.shuffle(a1)
    np.random.shuffle(a2)
    np.random.shuffle(a3)
    np.random.shuffle(a41)

    print(a1)
    print(a2)
    print(a3)
    print(a41)

    test_train_1.insert(1,'',a1,True)
    test_train_2.insert(1,'',a2,True)
    test_train_3.insert(1,'',a3,True)
    test_train_41.insert(1,'',a41,True)

    # save to CSV to check the results
    test_train_1.to_csv(merge_out_path + "1.csv",index=False, header=False)
    test_train_2.to_csv(merge_out_path + "2.csv",index=False, header = False)
    test_train_3.to_csv(merge_out_path + "3.csv",index=False, header = False)
    test_train_3.to_csv(merge_out_path + "41.csv",index=False, header = False)

    return


def get_processed_data(datasetFile, categoryMappingsPath, classType='binary'):
    inputFile = pd.read_csv(datasetFile, header=None)
    X = inputFile.iloc[:, 0:-2].values
    label_column = inputFile.iloc[:, -2].values
    
    temp1 = pd.read_csv(categoryMappingsPath + "1.csv", header=None)
    temp2 = pd.read_csv(categoryMappingsPath + "2.csv", header=None)
    temp3 = pd.read_csv(categoryMappingsPath + "3.csv", header=None)

    category_1 = np.array(pd.read_csv(categoryMappingsPath + "1.csv", header=None).iloc[:, 0].values)
    category_2 = np.array(pd.read_csv(categoryMappingsPath + "2.csv", header=None).iloc[:, 0].values)
    category_3 = np.array(pd.read_csv(categoryMappingsPath + "3.csv", header=None).iloc[:, 0].values)

    
    #category_label = np.array(pd.read_csv(categoryMappingsPath + "41.csv", header=None).iloc[:, 0].values)
    ct = ColumnTransformer(
                [('X_one_hot_encoder', OneHotEncoder(categories=[category_1, category_2, category_3], handle_unknown='ignore'), [1,2,3])],    # The column numbers to be transformed ([1, 2, 3] represents three columns to be transferred)
                remainder='passthrough'# Leave the rest of the columns untouched
            )
    X = np.array(ct.fit_transform(X), dtype=np.float)

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(np.array(X))  # Scaling to the range [0,1]
        
    if classType == 'binary':               
        y = []
        for i in range(len(label_column)):
            if label_column[i] == 'normal' or str(label_column[i]) == '0':
                y.append(0)
            else:
                y.append(1)        
        # Convert ist to array
        y = np.array(y)        
    else:    
        #Converting to integers from the mappings file
        label_map = pd.read_csv(categoryMappingsPath + "41.csv", header=None)
        label_category = label_map.iloc[:, 0].values
        label_value = label_map.iloc[:, 1].values
        
        y = []
        for i in range(len(label_column)):
            y.append(label_value[label_category.tolist().index(label_column[i])])
        # Encoding the Dependent Variable
        y = np_utils.to_categorical(y)
    
    return X, y
