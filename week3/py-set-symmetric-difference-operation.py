e, estudents = int(input()), set(input().split())
f, fStudents = int(input()), set(input().split())
a = eStudents.union(fStudents) - eStudents.intersection(fStudents)
print(len(a))

