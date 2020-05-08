import os

folderPath = r'D:\Documents\YouthComputing\Rename'
fileNumber = 1

for filename in os.listdir(folderPath):
    os.rename(folderPath + '\\'+ filename, folderPath+ '\\'+ "Test" + str(fileNumber)+ '.png') 
    fileNumber+=1
    
