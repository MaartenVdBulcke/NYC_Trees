# Data cleaning project - NYC Trees

## Description
New York residents were asked to report on the state of the nearest tree in their neighborhood. A lot of residents have 
responded but the way they reported was not uniform.
This project cleans the resulting dataset and provides a cleaned dataset. 
The goal of the cleaning is to prepare the data for machine learning. 

## Cleaning operations
These cleaning operations were performed: 
+ duplication was reduced
+ missing values from relevant columns were filled in
+ a lot of missing values for dead trees and stumps was not filed in
+ datatypes were changed
+ string-values were consolidated
+ several columns were reduced to one 

## Usage 
### CSV-file 
The cleaned dataset is to be found in the file trees_cleaned_xl.csv. 
It contains data on 222.222 New York trees.

### Python scripts
The used Python-scripts are also present in the subfolder. 

+ trees_cleaning_functions.py: contains the written functions to perform datacleaning and to check the dataset
+ trees_xl_cleaning.py: here is the dataset imported. It contains general functions to clean the data and export the dataframe to a csv-file 
+ main.py: run this file to use the scripts 

### Dataset
To be able to use the scripts, please download a tree dataset from https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh/data and read your dataset in the trees_xl_cleaning.py-script. 

![NYC Picture (Image)](https://media.architecturaldigest.com/photos/56a177c6f62777972f2fe407/16:9/w_3104,h_1746,c_limit/million-trees-new-york-01.jpg)
