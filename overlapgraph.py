fin = open('graph.txt', 'r')
fout = open('graphop.txt', 'w')

DNAreads=[]

for line in fin.readlines():
    DNAreads.append(line.replace('\n',''))
DNAreads.sort()
for i in DNAreads:
    for j in DNAreads:
        if i[1:]==j[:len(i)-1]:
            fout.write(i+' -> '+j+"\n")

fin.close()
fout.close()