outputList = []
for a in range(0,11):
    for b in range(0,11):
        for c in range(0,11):
            for d in range(0,11):

                if a**3 + b**3 + c**3 + d**3 == 1000:
                    outputList.append([a,b,c,d])
print(outputList)