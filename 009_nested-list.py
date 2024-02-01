# link : https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score
    sorted_students = list(set(sorted(students.values())))
    queried_value = sorted_students[1]
    queried_students = [key for key, val in students.items() if val == queried_value]
    for s in sorted(queried_students):
        print(s)
