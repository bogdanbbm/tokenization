import random
import json

names = ['Bogdan', 'Iuliana', 'Daniel', "cineva", 'da', 'nu']
alphabetOfToken = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
lenghtOfToken = 6
numberOfTokens = pow(len(alphabetOfToken), lenghtOfToken)

def createToken():
    token = ''
    for _ in range(lenghtOfToken):
        token += random.choice(alphabetOfToken)
    return token

tokenDict = dict()
tokenDict["tokens"] = dict()
tokenDict["notokens"] = dict()

for name in names:
    if name not in tokenDict['tokens']:
        
        if len(tokenDict['tokens'].values()) == numberOfTokens:
            print("No more tokens available for name '" + name + "'")
            tokenDict['notokens'][name] = '!'
            continue

        token = createToken()
        
        while token in tokenDict['tokens'].values():
            token = createToken()
        
        if name in tokenDict['notokens']:
            del tokenDict['notokens'][name]

        tokenDict['tokens'][name] = token


with open("tokenNames.json", "w") as outfile:
    json.dump(tokenDict, outfile)

print(len(alphabetOfToken))