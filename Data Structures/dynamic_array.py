def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    res = []
    for query in queries:
        if query[0] == 1:
            index = (query[1] ^ lastAnswer) % n
            arr[index].append(query[2])
        else:
            index = (query[1] ^ lastAnswer) % n
            lastAnswer = arr[index][query[2] % len(arr[index])]
            res.append(lastAnswer)
    return res

print(dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]))
    