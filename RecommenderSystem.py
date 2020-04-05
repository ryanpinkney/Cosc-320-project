import json

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


def algorithmAforProject(inputData):
        # define an empty array to store the similarity scores between all the users
    similarityScores = []

    # store the target user's likes and dislikes in variables
    tarUserLik = inputData[inputData["targetUser"]]["likes"]
    tarUserDislik = inputData[inputData["targetUser"]]["dislikes"]

    # iterate through all the users and compute the similarity of each user with the target user
    for key in inputData:
        if(key != "targetUser"):  # skip the first key
            otherUserLikes = inputData[key]["likes"]
            otherUserDislikes = inputData[key]["dislikes"]
            similarityScore = getSimilarityBetweenTwoUsersNaive(
                tarUserLik, tarUserLik, otherUserLikes, otherUserDislikes)
				


def algorithmBforProject(inputData):
    return  # to be implemented


def getSimilarityBetweenTwoUsersNaive(targetUserLikes, targetUserDislikes, otherUserLikes, otherUserDisklikes):
    return 2


def getSimilarityBetweenTwoUsersEfficient(targetUserLikes, targetUserDislikes, otherUserLikes, otherUserDisklikes):
    return 2


algorithmAforProject(basicTestData)
