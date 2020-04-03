# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:29:27 2020

@author: Jeremy.Inman
"""

import os
#from datetime import datetime
import time
import glob
import pandas as pd


print(os.getcwd())

config = {}

with open('config\\config.txt') as f:
    for line in f.readlines():
        variable, value = line.split(':',1)[0].strip(),line.split(':',1)[1].strip()
        
        config[variable] = value

print(config)

def getFiles(filePath = ''):
    
    print('getting files from filepath: ' + filePath)
    
    fileList = []
    
    for file in os.listdir(filePath):
        if file.find('.csv') > 1:
            fileList.append(file)
            
    print(fileList)
    return fileList

def mergeFile(outputDir = '', inputDir = '', filesToMerge = []):
    
    print('merging files into directory: ' + outputDir)
    
    outputname = 'output_'+time.strftime("%Y%m%d")+'.csv'
    os.chdir(inputDir)
    
    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]    
    
    
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( outputDir+outputname, index=False, encoding='utf-8-sig')
    
    print('file output to: '+outputname)
    

filesToMerge = getFiles(config['raw_data_file_dir'])

mergeFile(config['output_file_dir'],config['raw_data_file_dir'],filesToMerge)


    
    
    
    