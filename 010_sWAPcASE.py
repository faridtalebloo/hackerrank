# link = https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result = ""
    for c in s:
        if str.upper(c) == c:
            result += str.lower(c)
        else:
            result += str.upper(c)
    
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)