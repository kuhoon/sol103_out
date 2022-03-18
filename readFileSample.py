with open("nodes.dat") as datFile:
    xValueList = [data.split()[1] for data in datFile]
with open("nodes.dat") as datFile:
    yValueList = [data.split()[2] for data in datFile]
with open("nodes.dat") as datFile:
    zValueList = [data.split()[3] for data in datFile]

# delete column name
del xValueList[0]
del yValueList[0]
del zValueList[0]

valueList = []
for x, y, z in zip(xValueList, yValueList, zValueList):
    valueList.append([x, y, z])
