a, b = input().split()
a = list(a)
b = list(b)
num1 = ''
num2 = ''

for i in a:
    num1 = i+num1
for i in b:
    num2 = i+num2
    
num1 = int(num1)
num2 = int(num2)

if num1>num2:
    print(num1)
else:
    print(num2)