# Requires Jobs_API to be running to work jobs api returns json files IBM Capstone Week 1
# uses api created by Jobs_API to create 2 excel files
# for job posting using a list of locations and techonolgies

#Import required libraries
!pip3 install openpyxl
from openpyxl import Workbook 
#import Workbook class from module openpyxl
import pandas as pd
import json

# list given in assignment
listL = ['Los Angeles', 'New York', 'San Francisco', 'Washington DC', 'Seattle', 'Austin', 'Detroit']
listT = ['C', 'C#', 'C++', 'Java', 'JavaScript', 'Python', 'Scala', 'Oracle', 'SQL Server', 'MySQL Server', 'PostgreSQL', 'MongoDB']


api_url="http://127.0.0.1:5000/data"

def get_number_of_jobs_T(technology):
    dataT=requests.get(api_url,params={"Key Skills":technology})
    jobs= dataT.json()
    number_of_jobs= len(jobs)
    return technology, number_of_jobs
  
  def get_number_of_jobs_L(location):
    dataL=requests.get(api_url,params={"Location":location})
    locations = dataL.json()
    number_of_jobs= len(locations)
    return location,number_of_jobs
  
wbl=Workbook()
wsl=wbl.active
wbt=Workbook()
wst=wbt.active

wsl.append(['Location', 'Job Postings'])
wst.append(['Technology', 'Job Postings'])

for i in listL:
    wsl.append(get_number_of_jobs_L(i))

for i in listT:
    wst.append(get_number_of_jobs_T(i))
    
wbl.save("job-postings.xlsx")
wbt.save("tech-postings.xlsx")
