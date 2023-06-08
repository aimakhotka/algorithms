n = int(input())
numbers = list(map(int, input().split()))

approaches = 1
pulls = []
pulls_count = 1

for i in range(1, n):
    if numbers[i] > numbers[i-1]:
        pulls_count += 1
    else:
        pulls.append(pulls_count)
        pulls_count = 1
        approaches += 1

pulls.append(pulls_count)

print(approaches)
print(' '.join(map(str, pulls)))
