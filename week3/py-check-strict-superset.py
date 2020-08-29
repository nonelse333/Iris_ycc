A = set(input().split())
N = int(input())
total = []
for i in range(N):
    othersets = set(input().split())
    if (othersets & A) == othersets and len(A - othersets) > 0:
        result = "True"
    else:
        result = "False"
    total.append(result)
if "False" in total:
    print("False")
else:
    print("True")
    

