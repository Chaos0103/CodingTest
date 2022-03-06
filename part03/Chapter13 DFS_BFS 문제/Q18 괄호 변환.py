# '균형잡힌 괄호 문자열'의 인덱스를 반환하는 함수
def getIndex(data):
    cnt = 0
    for idx in range(len(data)):
        if data[idx] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return idx
    return len(data)-1


# 특정한 '균형잡힌 괄호 문자열'이 '올바른 괄호 문자열'인지 판단하는 함수
def check(data):
    cnt = 0
    for c in data:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        return True
    return False


def solution(p):
    answer = ''
    if len(p) == 0:
        return p
    if p[0] == '"':
        data = p[1:len(p)-1]
    else:
        data = p
    idx = getIndex(data)
    u = data[:idx+1]
    v = data[idx+1:]
    if check(u):
        answer += u
        answer += solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1: -1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer


test1 = '"(()())()"'
test2 = '")("'
test3 = '"()))((()"'

print(solution(test1))  # "(()())()"
print(solution(test2))  # "()"
print(solution(test3))  # "()(())()"
