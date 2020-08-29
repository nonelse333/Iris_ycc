n = int(input())
for i in range(n):
    a = int(input())
    set_a = set(input().split())
    b = int(input())
    set_b = set(input().split())
    if len(set_a - set_b) == 0:
        print("True")
    else:
        print("False")

