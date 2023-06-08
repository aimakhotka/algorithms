def ivan_office_time(n, m, x, y, k, train_home, train_office):
    max_time = 0
    train_home.sort()
    train_office.sort()

    for i in range(k+1):
        if i >= n or (i < m and train_office[m-i-1] - train_home[i] <= x):
            max_time = max(max_time, train_office[m-i-1] + y)

    return max_time if max_time > 0 else -1

n, m = map(int, input().split())
x, y = map(int, input().split())
k = int(input())
train_home = list(map(int, input().split()))
train_office = list(map(int, input().split()))


result = ivan_office_time(n, m, x, y, k, train_home, train_office)
print(result)
