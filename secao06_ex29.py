total = 0
som = 0
a = 0
s=0
for i in range(2,11,2):
    for t in range(1,i):
        i = i*t
    a +=1
    s = s + a/i
print(s)