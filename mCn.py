def pick(n, picked, topick):
    if topick == 0:
        print(picked)
        return
    small = 0 if not picked else picked[-1]+1
    for next in range(small, n):
        picked.append(next)
        pick(n, picked, topick-1)
        picked.pop()


pick(5, [], 3)

