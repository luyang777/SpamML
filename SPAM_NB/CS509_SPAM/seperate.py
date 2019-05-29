
fh = open( 'SPAMTrain.label')         

i=0
j=0
compter= 0
account=0
listline = []

for line in fh.readlines():
    listline.append(line.split(" ")[0])

while j < 139:
    compter += int(listline[j])
    j += 1
print(compter)

while i < 202:
    account += int(listline[i])
    i += 1
print(account)


