n, t = map(int, input().split())
floors = list(map(int, input().split()))
leaving = floors[int(input())-1]

first_floor = floors[0]
last_floor = floors[-1]

if not floors or t == 0 or n == 0:
    print("Ошибка ввода")
elif len(set(floors)) == 1:
    print(0)
else:
    upper_is_faster = (last_floor - leaving) < (leaving - first_floor)
    if upper_is_faster:
        min_diff = last_floor - leaving
    else:
        min_diff = leaving - first_floor

    if min_diff > t:
        print(min_diff + last_floor - first_floor)
    else:
        print(last_floor - first_floor)


# # input part
# employee_count, exit_time = map(int, input().split())
# levels = [_ for _ in map(int, input().split())]
# exit_employee = int(input())

# # logic part
# last_level = levels[employee_count - 1]
# first_level = levels[0]
# time_level = levels[exit_employee - 1]

# upper_is_faster = (last_level - time_level) < (time_level - first_level)
# if upper_is_faster:
#     min_diff = last_level - time_level
# else:
#     min_diff = time_level - first_level

# if time_have_sense := min_diff > exit_time:
#     result = min_diff + last_level - first_level
# else:
#     result = last_level - first_level

# print(result)


# n, t = list(map(int, input().split()))
# floors = list(map(int, input().split()))
# leaving = floors[int(input())-1]

# if not floors or t == 0 or n == 0:
#     print("Ошибка ввода")

# diff = floors[-1] - floors[0]

# if n == 1:
#     print(0)
# elif len(set(floors)) == 1:
#     print(0)
# elif t < n:
#     print(min((diff + floors[-1] - leaving), (diff + leaving - floors[0])))
# else:
#     print(max(floors) - min (floors))