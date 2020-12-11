import os
import sys
import datetime
import shutil

req_path = input("Enter Your path: ")
age=30

if not os.path.exists(req_path):
    print("Please enter valid path")
    sys.exit(1)
    
if os.path.isfile(req_path):
    print("Please enter directory path")
    sys.exit(2)
    
today=datetime.datetime.now()

for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path, each_file)
    
    if os.path.exists(each_file_path):
        file_cre_data=datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        dif_days=(today-file_cre_data).days
        
        if dif_days > age:
            print(each_file_path,dif_days)
            shutil.rmtree(each_file_path)