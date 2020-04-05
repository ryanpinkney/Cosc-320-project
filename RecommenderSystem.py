# imports
import json
import random

# data definition
basicTestData = {
    "targetUser": "userNameOfTargetUser",
    "user1": {
        "likes": ["item0", "item2", "item3"],
        "dislikes": ["item7", "item5"]
    },
    "userNameOfTargetUser": {
        "likes": ["item0", "item4", "item6"],
        "dislikes": ["item7", "item5", "item1"]
    },
    "user2": {
        "likes": ["item3", "item7"],
        "dislikes": ["item4", "item2", "item1"]
    },
    "user3": {
        "likes": ["item6", "item4", "item2", "item0"],
        "dislikes": ["item1", "item3", "item5", "item7"]
    },
    "user4": {
        "likes": ["item1", "item5", "item7"],
        "dislikes": ["item6", "item4", "item0"]
    },
    "user5": {
        "likes": ["item2"],
        "dislikes": ["item3"]
    }
}

# methods definition


def algorithmAforProject(inputData):
    # define an empty array to store the similarity scores between all the users
    similarityScores = dict()

    # get the name of the target user
    targetName = inputData["targetUser"]

    # iterate through all the users
    for key in inputData:
        # skip the first key and the target user
        if(key != "targetUser" and key != targetName):
            # compute the similarity score between both users
            similarityScore = getSimilarityEfficient(inputData[targetName], inputData[key])
            # append to the similarityScores dictionary a {otherUsername: score} pair
            similarityScores[key] = similarityScore
    
    print(similarityScores)

    # sort similarityScores by score, descending. Sorting code from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sortedScores = {k: v for k, v in sorted(
        similarityScores.items(), key=lambda item: item[1], reverse=True)}
    
    #this value denotes the arbitrary number of users that will add to the recommended list
    max_users = 2
    #recommendation array defined
    recommendation = []
    
    #setup the targets data
    target = inputData[targetName]
    target_likes = target["likes"]
    target_dislikes = target["dislikes"]
    
    #for loop checks the max_users number of highest similarity 
    for i in list(sortedScores)[0:max_users]:
        #load the user data
        user = inputData[i]
        user_likes = user["likes"]
        #ensure this element has not already been seen by the target
        for j in user_likes:
            if(j not in target_likes and j not in target_dislikes):
                #ensures the recommendation list does not get multiples
                if(j not in recommendation):
                    recommendation.append(j)
                    
    #finally returns the recommendation list
    print(recommendation)
    return recommendation

def algorithmBforProject(inputData):
    return  # to be implemented


def getSimilarityNaive(user1, user2):
    return random.randrange(1, 10)  # to be implemented


def getSimilarityEfficient(user1, user2):
    # get the intersections and unions required for the similarity formula
    ill = intersectionEfficient(user1["likes"], user2["likes"])
    idd = intersectionEfficient(user1["dislikes"], user2["dislikes"])
    ild = intersectionEfficient(user1["likes"], user2["dislikes"])
    idl = intersectionEfficient(user1["dislikes"], user2["likes"])
    ull = unionEfficient(user1["likes"], user2["likes"])
    udd = unionEfficient(user1["dislikes"], user2["dislikes"])

    # return the computed similarity from the formula
    return (len(ill) + len(idd) - len(ild) - len(idl)) / len(unionEfficient(ull, udd))


def intersectionEfficient(arr1, arr2):
    # result is the elements that intersect
    result = []

    # put both lists into the dictionary
    map = {}
    for a in arr1:
        map[a] = map.get(a, 0) + 1
    for a in arr2:
        map[a] = map.get(a, 0) + 1

    # get all keys with a value > 1 aka intersecting
    for key in map:
        if (map[key] > 1):
            result.append(key)

    return result


def unionEfficient(arr1, arr2):
    # put both lists into the dictionary
    map = {}
    for a in arr1:
        map[a] = map.get(a, 0) + 1
    for a in arr2:
        map[a] = map.get(a, 0) + 1

    # return the list of keys
    return list(map.keys())



# methods calling
algorithmAforProject(basicTestData)
