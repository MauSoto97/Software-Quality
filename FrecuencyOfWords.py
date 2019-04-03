import sys

ans = "g e5g41e5g1 g5 5e1e5 er5r1g er5er5 35 41541 654 s6f5sd 3135 1"
array1 = ans.split(" ")
numbers=[]
words=[]
new=[]

for a in array1:
    try:
        float(a)
    except:
        words.append(a)
    else:
        numbers.append(a)

for i in range(0, len(numbers)):
    if numbers[i] not in new:
        new.append(numbers[i])

for i in range(0, len(new)):
    print('Frequency of ', new[i], ' is :', numbers.count(new[i]))

