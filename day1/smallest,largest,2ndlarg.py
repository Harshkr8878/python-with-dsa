n=int(input("enter the total element inside the list:"))
l=[]
for i in range(n):
    el=int(input("enter the element: "))
    l.append(el)
print("my list ",l)
sorted_list=l.sort()
print("sort list: ",l)

minimum_element=l[0]
print("smallest element is: ",minimum_element)
max_element=l[-1]
print("largest element is: ",max_element)
second_largest_element=l[-2]
print("second_largest element is: ",second_largest_element)