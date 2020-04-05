# imports
import json
import random

# data definition
basicTestData = {
    "targetUser": "userNameOfTargetUser",
    "user1": {
        "likes": ["NJKNO", "HHNONI", "BNJBIO"],
        "dislikes": ["HJKBK", "NJUINIO"]
    },
    "userNameOfTargetUser": {
        "likes": ["DNLNIL", "NJNJS", "DSQDQSD", "DSQDSQDQS"],
        "dislikes": ["DQSDQS", "DSQDSQ", "DSQDQS", "DSQDQ"]
    },
    "user2": {
        "likes": ["IIJJKNL", "FDNLNIL"],
        "dislikes": ["IIJJKNL", "FDNLNIL", "NNIKNI"]
    }
}

# methods definition


def algorithmAforProject(inputData):
    # define an empty array to store the similarity scores between all the users
    similarityScores = dict()

    # iterate through all the users
    for key in inputData:
        # skip the first key and the target user
        if(key != "targetUser" and key != inputData["targetUser"]):
            # compute the similarity score between both users
            similarityScore = getSimilarityBetweenTwoUsersNaive(
                inputData["targetUser"], inputData[key])

            # append to the similarityScores dictionary a {otherUsername: score} pair
            similarityScores[key] = similarityScore

    # sort similarityScores by score, descending. Sorting code from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sortedScores = {k: v for k, v in sorted(
        similarityScores.items(), key=lambda item: item[1], reverse=True)}


def algorithmBforProject(inputData):
    return  # to be implemented


def getSimilarityBetweenTwoUsersNaive(user1, user2):
    return random.randrange(1, 10)  # to be implemented


def getSimilarityBetweenTwoUsersEfficient(user1, user2):
    return random.randrange(1, 10)  # to be implemented


# methods calling
algorithmAforProject(basicTestData)
