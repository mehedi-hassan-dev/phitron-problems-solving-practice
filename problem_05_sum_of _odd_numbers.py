N = int(input())
sum = 0

for i in range(1, N + 1):
    if i % 2 == 0:
        continue
    sum += i
print(sum)