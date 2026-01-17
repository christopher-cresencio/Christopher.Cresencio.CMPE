import os
import csv
import time
import gspread
from googleapiclient.errors import HttpError
from gspread.utils import ValueInputOption
from oauth2client.service_account import ServiceAccountCredentials


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCE_FOLDER = os.path.join(BASE_PATH, "RESOURCESdec13")
SERVICE_KEY = os.path.join(RESOURCE_FOLDER, "")

credential = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_KEY, scopes=['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)

sheet_url = "https://docs.google.com/spreadsheets/d /193QA8E5WWKWqzqPQ1m06u-0WMTg-GGg9AwhOzWk6lns/edit"

gs_instance = client.open_by_url(sheet_url)
sheet_instance = gs_instance.get_worksheet(0)

googlesheet_data_tab0 = sheet_instance.get_all_records()
print(googlesheet_data_tab0)

new_row_data = ["4", "Lolo Jiar", "BSECE", "4th", "4-5", "Rizal"]
sheet_instance.append_row(new_row_data)



'''''
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

CSV_FOLDER = os.path.join(BASE_PATH, "RESOURCESdec13")
CSV_PATH = os.path.join(CSV_FOLDER, "MYFIRSTCSV.csv")

print(CSV_PATH)

csv_data = []

with open(CSV_PATH, mode='r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        csv_data.append(row)
print("-------------------------------------------------------")
print(csv_data)
print(csv_data[3])

#NAME IS COLUMS 1
#ADDRESS IS COLUMN 5

csv_new_data = []
for row in csv_data:
    csv_new_data.append([row[1], row[5]])

print(csv_new_data)

with open(os.path.join(CSV_FOLDER, "WRITE_CSV.csv"), mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_new_data)
'''

'''''
print(os.getcwd())
print(os.listdir(os.getcwd()))
#os.makedirs(os.getcwd() + "/test")
#os.makedirs(os.path.join(os.getcwd(), "testtest"))

print(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(BASE_PATH)

with open("virus.txt", "w", newline="") as dangerfile:
    print("Virus Found")

time.sleep(10)

pathdir = ""
for root, dirs, files in os.walk(BASE_PATH):
    for filename in files:
        print(filename)
        if filename == "virus.txt":
            print(os.path.join(root, filename))
            pathdir = os.path.join(root, filename)
            os.remove(pathdir)
            break
'''


