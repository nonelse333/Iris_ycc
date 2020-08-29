N = int(input())
A = set(map(int, input().split()))
M = int(input())
for i in range(M):
    S = input()
    S = S.split()
    othersets = set(map(int, input().split()))
    if S[0] == "intersection_update":
        A.intersection_update(othersets)
    elif S[0] == "update":
        A.update(othersets)
    elif S[0] == "symmetric_difference_update":
        A.symmetric_difference_update(othersets) 
    elif S[0] == "difference_update":
        A.difference_update(othersets)
print(sum(A))



