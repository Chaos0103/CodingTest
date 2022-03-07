def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        part = s[:step]
        cnt = 1
        total = ''
        for i in range(step, len(s), step):
            if part == s[i:i+step]:
                cnt += 1
            else:
                if cnt > 1:
                    total += str(cnt)
                total += part
                part = s[i:i+step]
                cnt = 1
        if cnt > 1:
            total += str(cnt)
        total += part
        answer = min(answer, len(total))
    return answer


# test case
print(solution('aabbaccc'))  # 7
print(solution('ababcdcdababcdcd'))  # 9
print(solution("abcabcdede"))  # 8
print(solution("abcabcabcabcdededededede"))  # 14
print(solution("xababcdcdababcdcd"))  # 17
