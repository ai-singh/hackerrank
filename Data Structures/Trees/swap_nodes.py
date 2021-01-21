#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def inOrder(root, arr):
    if root:
        current = root
        stack = []
        done = 0
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                arr.append(current.info)
                current = current.right
            else:
                break

def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    tree = []
    root = Node(1)
    tree.append(root)
    index = 0
    if len(indexes) > 1:
        for children in indexes:
            if children[0] != -1:
                node = Node(children[0])
                tree[index].left = node
                tree.append(node)
            if children[1] != -1:
                node = Node(children[1])
                tree[index].right = node
                tree.append(node)
            index += 1
        ref = []
        ref.append(root)
        temp = []
        index = 0
        max_height = 1
        while True:
                if index < len(ref):
                    if ref[index].left:
                        temp.append(ref[index].left)
                    if ref[index].right:
                        temp.append(ref[index].right)
                    ref.remove(ref[index])
                elif len(temp) == 0:
                    break
                else:
                    ref = temp
                    temp = []
                    max_height += 1
        quer = []
        for query in queries:
            q = []
            q.append(query)
            for num in range(2, 10000):
                if num * query <= max_height:
                    q.append(num * query)
                else:
                    break
            quer.append(q)
        res = []
        for q in quer:
            for query in q:
                height = 1
                ref = []
                ref.append(root)
                temp = []
                index = 0
                while height != query:
                    if index < len(ref):
                        if ref[index].left:
                            temp.append(ref[index].left)
                        if ref[index].right:
                            temp.append(ref[index].right)
                        ref.remove(ref[index])
                    else:
                        ref = temp
                        temp = []
                        height += 1
                for r in ref:
                    r.left, r.right = r.right, r.left
            arr = []
            inOrder(root, arr)
            res.append(arr)
        return res
        
                


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    f = open("sample.txt", "w")
    f.write('\n'.join([' '.join(map(str, x)) for x in result]))
    f.close()

    #fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    #fptr.write('\n')

    #fptr.close()


"""
3
2 3
-1 -1
-1 -1
1
1


5
2 3
-1 4
-1 5
-1 -1
-1 -1
1
2


11
2 3
4 -1
5 -1
6 -1
7 8
-1 9
-1 -1
10 11
-1 -1
-1 -1
-1 -1
2
2
4
"""