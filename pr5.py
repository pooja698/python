import sys
f = open("text.txt", "r")
with open('text.txt') as f:
    b=[word for line in f for word in line.split()]
a = list( dict.fromkeys(b) )
sys.stdout = open('text.txt','wt')
for i in range(len(a)) :
    print(a[i])
    print(b.count(b[i]))


