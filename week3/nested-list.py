if __name__ == '__main__':
    studentslist = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students = [name, score]
        studentslist.append(students)
        scores.append(score)
    studentslist.sort()
    a = sorted(set(scores))[1]
    for i in studentslist:
        name = i[0]
        score = i[1]
        if score == a:
            print(name)
