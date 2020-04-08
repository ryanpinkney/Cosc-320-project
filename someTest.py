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

basicTestData2 = '{"targetUser": "userNameOfTargetUser"}'

print(basicTestData.keys())
print(basicTestData)