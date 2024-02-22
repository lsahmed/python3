# Make a program to find the largest number from an array
a = input("enter first number: ")
b = input("enter second number: ")
c = input("enter the third number: ")
arr = [a,b,c]
max = arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]
    
print(max)
 