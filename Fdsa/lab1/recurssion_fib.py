a=0
b=1
choice = int(input("Enter the number: "))
print("fibonacci series of {choice} is ",end="")
if choice == 0:
    print("0")
elif choice == 1:
    print("1")
    
for i in range(1,choice):
    a,b = b, a+b
    print(a,end="    ")
