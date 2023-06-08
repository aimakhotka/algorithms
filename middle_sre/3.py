# def maximum_cups(n, h, heights):
#     heights = heights.sort() 
#     max_height = 0
#     total_height = 0

#     for i in range(n):
#         if total_height + heights[i] <= h:
#             total_height += heights[i]
#             max_height += 1
#         else:
#             break

#     return max_height

# n, h = map(int, input().split())
# heights = list(map(int, input().split()))

# result = maximum_cups(n, h, heights)
# print(result)

n, t = map(int, input().split())
cups = list(map(int, input().split()))

for i in range(0, n, 2):
    temp_max = max(cups[i], cups[i+1])
    if t < temp_max:
        if t >= cups[i]:
            print(i+1)
        elif t >= cups[i+1]:
            print(i+2)
        else:
            print(i)
        break

    t -= max(cups[i], cups[i+1])