N = int(input())

numbers = input().split()  # bikolpo numbers = [int (x) for x in input().split()]
for i in range(N):
    numbers[i] = int(numbers[i])


count = 0
for i in numbers:
    if i % 2 == 0:
        count += 1
print(count)