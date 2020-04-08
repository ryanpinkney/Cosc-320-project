import csv
import json



#The following code will read ratings_Amazon_Instant_Video.csv into the dictionary 'data 'as shown below
#'userID': {"likes":likes_array,"dislikes":dislikes_array}
data ={}
with open("ratings_Amazon_Instant_Video.csv") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        userId = rows["user"]
        item = rows["item"]
        rating = rows["rating"]

        if userId in data:
            if float(rating) >3.0:
                data[userId]["likes"].append(item)
            else:
                data[userId]["dislikes"].append(item)
        else:
            data[userId] = {"likes":[],"dislikes":[item]}
            if float(rating) >3.0:
                data[userId]["likes"].append(item)
            else:
                data[userId]["dislikes"].append(item)
            
#read into ratings_Amazon_Instant_Video.json
with open("ratings_Amazon_Instant_Video.json","w") as jsonFile:
    jsonFile.write(json.dumps(data,indent=4))
        #'user1': {'likes': ['NJKNO', 'HHNONI', 'BNJBIO'], 'dislikes': ['HJKBK', 'NJUINIO']}