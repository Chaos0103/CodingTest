def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 + 1):
        pre = s[:step]
        now = ''
        count = 1
        for i in range(step, len(s), step):
            if pre == s[i:i+step]:
                count += 1
            else:
                if count > 1:
                    now += str(count)
                now += pre
                pre = s[i:i+step]
                count = 1
        if count > 1:
            now += str(count)
        now += pre
        answer = min(answer, len(now))
    return answer


# test case
print(solution('aabbaccc'))  # 7
print(solution('ababcdcdababcdcd'))  # 9
print(solution("abcabcdede"))  # 8
print(solution("abcabcabcabcdededededede"))  # 14
print(solution("xababcdcdababcdcd"))  # 17
