import csv
import json
from RecommenderSystem import algorithmAforProject,algorithmBforProject
import time

x_axis = []
start = time.process_time()
with open('Magazine_Subscriptions.json') as json_file:
    algorithmAforProject(json.load(json_file))
print(time.process_time() - start)

start2 = time.process_time()
with open('Magazine_Subscriptions.json') as json_file:
    algorithmBforProject(json.load(json_file))
print(time.process_time() - start2)


#some code convertign csv to json


# data_set_names = ["Pet_Supplies"]
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
#     #'user1': {'likes': ['NJKNO', 'HHNONI', 'BNJBIO'], 'dislikes': ['HJKBK', 'NJUINIO']}