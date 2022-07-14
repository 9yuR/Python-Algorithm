A = int(input())
B = int(input())
C = int(input())

l = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

for i in str(A * B * C):
    l[int(i)] += 1

for i in l:
    print(i)