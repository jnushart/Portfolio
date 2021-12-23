#!/usr/bin/python3.4

#Using given times between buildings, find the fastest path for the mail carrier to deliver to each building, starting with building 1.


import threading
from itertools import permutations

#read in file
with open("input2.txt") as fp:
    names =[]
    times =[]
    line = fp.readline()
    count = 1
    while line:
        line2 = line.replace("\n", "")
        line2 = line2.split(" : ")
        names.append(line2[0])
        times.append(line2[1])
        count += 1
        line = fp.readline()
end = []
end.append(names[0])
filtered = []
names2 = names + end

#get list of every order to go
perms = list(itertools.permutations(names2, len(names2)))
totals = []    

#filter perms to only get ones that start and and with building 1
for perm in perms:
    first = perm[0]
    last = perm[len(names2)-1]
    if first == names2[0] and last == names2[len(names2)-1] and perm not in filtered:
        filtered.append(perm)

#function to calculate time
def timeFunction(perm):
    my_lock.acquire()
    subtotalTime = 0
    for i in range(0,len(perm)-1):
        start = perm[i]
        end = perm[i+1]
        sectionNo = names.index(start)
        endSectionNo = names.index(end)
        time = times[sectionNo]
        time22 = str(time).split(" ")
        timeMove = time22[endSectionNo]
        subtotalTime = subtotalTime + int(timeMove)
    totals.append(subtotalTime)
    my_lock.release()
    
#creating threads to calculate time for each permutation    
threads = list()

for perm in filtered:
    threads.append(threading.Thread(target=timeFunction, args =(perm,)))

my_lock = threading.Lock()  
  
for current_thread in threads:
    current_thread.start()
    
for current_thread in threads:
    current_thread.join()    


    
time2 = []
for time in times:
    timestoappend = time.split(" ")
    time2.append(timestoappend)

shortest = totals.index(min(totals))
output = ""
for i in filtered[shortest]:
    addition = str(i)
    output = output + " " + addition
output = output + " " + str(totals[shortest])

with open("output2.txt", 'w') as f:
    f.write(output)