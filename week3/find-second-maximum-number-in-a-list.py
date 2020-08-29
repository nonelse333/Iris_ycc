if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = list(arr)
    b = list(set(a))
    b.reverse()
    b.remove(max())
    print(max(b))
