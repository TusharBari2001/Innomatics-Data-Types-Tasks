def findPercentage(students, query_name):
    if query_name not in students:
        return "Student not found."
    else:
        total = sum(students[query_name])
        average = total / len(students[query_name])
        return '{:.2f}'.format(average)

if __name__ == '__main__':
    n = int(input().strip())
    students = {}
    for i in range(n):
        line = input().rstrip().split()
        name = line[0]
        scores = list(map(float, line[1:]))
        students[name] = scores
    query_name = input().strip()
    result = findPercentage(students, query_name)
    print(result)
