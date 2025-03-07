number=[22,33,44,12,6,8,2]
min_num=number[0]

max_num=number[0]

for i in range(len(number)):
    if number[i]>max_num:
        max_num=number[i]
    elif number[i]<min_num:
        min_num=number[i]
print("max",max_num)
print("min",min_num)