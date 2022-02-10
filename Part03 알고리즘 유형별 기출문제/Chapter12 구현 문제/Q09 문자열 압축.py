def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 + 1):
        previous = s[:step]
        count = 1
        renew = ''
        for i in range(step, len(s), step):
            if previous == s[i:i+step]:
                count += 1
            else:
                if count > 1:
                    renew += str(count)
                renew += previous
                previous = s[i:i+step]
                count = 1
        if count > 1:
            renew += str(count)
        renew += previous
        answer = min(answer, len(renew))
    return answer


# test case
print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
