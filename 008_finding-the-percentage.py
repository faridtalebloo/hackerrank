# link: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = 0 
    for i in student_marks[query_name]:
        result += i
    result /= len(student_marks[query_name])
    print(format(result,".2f"))