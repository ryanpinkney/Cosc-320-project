import csv
import json
from RecommenderSystem import algorithmAforProject,algorithmBforProject
import time
#this is the testing code
print('Magazine_Subscription')
#open the file and run with algorithmA
start = time.process_time()
with open('Magazine_Subscriptions.json') as json_file:
    algorithmAforProject(json.load(json_file))
print(time.process_time() - start)
#open the file and run with algorithmB
start2 = time.process_time()
with open('Magazine_Subscriptions.json') as json_file:
    algorithmBforProject(json.load(json_file))
print(time.process_time() - start2)

print("Patio_Lawn")

start = time.process_time()
with open('Patio_Lawn_and_Garden.json') as json_file:
    algorithmAforProject(json.load(json_file))
print(time.process_time() - start)

start2 = time.process_time()
with open('Patio_Lawn_and_Garden.json') as json_file:
    algorithmBforProject(json.load(json_file))
print(time.process_time() - start2)

print('Musical INstruments')
start = time.process_time()
with open('Musical_Instruments.json') as json_file:
    algorithmAforProject(json.load(json_file))
print(time.process_time() - start)

start2 = time.process_time()
with open('Musical_Instruments.json') as json_file:
    algorithmBforProject(json.load(json_file))
print(time.process_time() - start2)

print('Office_Products')
start = time.process_time()
with open('Office_Products.json') as json_file:
    algorithmAforProject(json.load(json_file))
print(time.process_time() - start)

start2 = time.process_time()
with open('Office_Products.json') as json_file:
    algorithmBforProject(json.load(json_file))
print(time.process_time() - start2)

print('ratings_Amazon_Instant_Video')

start = time.process_time()
with open('ratings_Amazon_Instant_Video.json') as json_file:
    algorithmAforProject(json.load(json_file))
print(time.process_time() - start)

start2 = time.process_time()
with open('ratings_Amazon_Instant_Video.json') as json_file:
    algorithmBforProject(json.load(json_file))
print(time.process_time() - start2)

#some code for converting csv to json


# data_set_names = ["Magazine_Subscriptions","Magazine_Subscriptions","Patio_Lawn_and_Garden"]
# for set_name in data_set_names:
#     #The following code will read .csv file into the dictionary 'data'as shown below
#     #'userID': {"likes":likes_array,"dislikes":dislikes_array}
#     data ={}
#     with open(set_name+".csv") as csvFile:
#         csvReader = csv.DictReader(csvFile)
#         for rows in csvReader:
#             userId = rows["user"]
#             item = rows["item"]
#             rating = rows["rating"]

#             if userId in data:
#                 if float(rating) >3.0:
#                     data[userId]["likes"].append(item)
#                 else:
#                     data[userId]["dislikes"].append(item)
#             else:
#                 data[userId] = {"likes":[],"dislikes":[item]}
#                 if float(rating) >3.0:
#                     data[userId]["likes"].append(item)
#                 else:
#                     data[userId]["dislikes"].append(item)
                
#     #write into ratings_Amazon_Instant_Video.json
#     with open(set_name+".json","w") as jsonFile:
#         jsonFile.write(json.dumps(data,indent=4))
    #'user1': {'likes': ['NJKNO', 'HHNONI', 'BNJBIO'], 'dislikes': ['HJKBK', 'NJUINIO']}