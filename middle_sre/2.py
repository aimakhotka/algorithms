n = int(input())
costs = list(map(int, input().split()))
m = int(input())
friends = [tuple(map(int, input().split())) for _ in range(m)]
sum_costs = 0

def search_min(company, costs):
    min_cost = max(costs)
    for cost in company:
        if min_cost > costs[cost-1]:
            min_cost = costs[cost-1]
    return min_cost

last = 0
company = [*friends[0]]
while last != m - 1:
    for i in range(1, len(friends)):
        if friends[i][0] in company and friends[i][1] not in company:
            company.append(friends[i][1])
        last = i
    sum_costs += search_min(company, costs)
    company = [*friends[last]]

for i in range(1, len(friends)):
    if friends[i][0] in company and friends[i][1] not in company:
        company.append(friends[i][1])
    last = i
sum_costs += search_min(company, costs)
company = [*friends[last]]

print(sum_costs)