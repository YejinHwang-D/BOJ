n = int(input())
temp = n
cycle = 0
while True:
    cycle += 1
    n = (n%10*10)+((n//10+n%10)%10)
    if (n == temp):
        break
print(cycle)