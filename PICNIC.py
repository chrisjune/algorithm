# # cases = int(input())
# cases = 1
# results = []
# for case in range(cases):
#     # numbers = input().split()
#     numbers = "2 1".split()
#     # friends = input().split()
#     friends = "0 1".split()
#     # friends = "0 1 1 2 2 3 3 0 0 2 1 3".split()
#     pairs = [sorted((friends[i], friends[i+1])) for i in range(0, len(friends), 2)]
#
#     results.append(pairs)
#
# for result in results:
#     print(result)

from copy import deepcopy

n = [0, 1, 2, 3]
n = [0, 1]
n = [0,1,2,3,4,5]
results = []


def perm(n, pocket):
    if not n:
        results.append(deepcopy(pocket))
    new = deepcopy(n)
    for i in new:
        pocket.append(i)
        n.remove(i)
        perm(n, pocket)
        n.append(i)
        pocket.remove(i)

friends = [0, 1, 1, 2, 2, 3, 3, 0, 0, 2, 1, 3]
friends = [0 ,1]
firends =

def check_duplicate(pairs, friends):
    count = 0
    for pair in range(0, len(pairs)):
        for friend in range(0, len(friends), 2):
            if pairs[pair] in [[friends[friend], friends[friend+1]], [friends[friend+1], friends[friend]]]:
                break
        count += 1
    return count

perm(n, [])
print(results, sep='\r\n')
print(int(check_duplicate(results, friends)/2))



