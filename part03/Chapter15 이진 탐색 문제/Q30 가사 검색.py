from bisect import bisect_left, bisect_right

def lenght(array, word):
    cnt = 0
    for c in word:
        if c == '?':
            break
        else:
            cnt += 1
    new_word1 = word[:cnt] + 'a' * (len(word)-cnt)
    new_word2 = word[:cnt] + 'z' * (len(word)-cnt)
    return bisect_left(array, new_word2) - bisect_right(array, new_word1)


def solution(words, queries):
    answer = []
    words_reverse = []
    new_words = [[] for _ in range(100001)]
    new_words_r = [[] for _ in range(100001)]
    words.sort()

    for word in words:
        new_words[len(word)].append(word)
        word = list(word)
        word.reverse()
        words_reverse.append(''.join(word))
    words_reverse.sort()
    for word in words_reverse:
        new_words_r[len(word)].append(word)
    for word in queries:
        if word[0] != '?':
            cnt = lenght(new_words[len(word)], word)
        else:
            word = list(word)
            word.reverse()
            word = ''.join(word)
            cnt = lenght(new_words_r[len(word)], word)
        answer.append(cnt)
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))