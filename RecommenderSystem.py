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
    similarityScores = []
    targetUserLikes = inputData[inputData["targetUser"]]["likes"]
    targetUserDislikes = inputData[inputData["targetUser"]]["dislikes"]
    # for i in range(0, len(inputData)):
    #     int similarityScore = getSimilarityBetweenTwoUsersNaive()


def algorithmBforProject(inputData):
    return  # to be implemented


def getSimilarityBetweenTwoUsersNaive(targetUserLikes, targetUserDislikes, otherUserLikes, otherUserDisklikes):
    return  # to be implemented (parameters will be figured out)


def getSimilarityBetweenTwoUsersEfficient(targetUserLikes, targetUserDislikes, otherUserLikes, otherUserDisklikes):
    return  # to be implemented (parameters will be figured out)


algorithmAforProject(basicTestData)
