import sys

x = int(input("x:"))
y = int(input("x:"))

try:
    result = x/ y
except ZeroDivisionError:
    print("Wobalubdubduhb")
    sys.exit(1)
    
print(f"{x}/{y}= {result}")
