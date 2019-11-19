cases = int(input())
results = []
for case in range(cases):
    numbers = input().split()
    friends = input().split()
    pairs = [(friends[i], friends[i+1]) for i in range(0, len(friends), 2)]

    results.append(pairs)

for result in results:
    print(result)

