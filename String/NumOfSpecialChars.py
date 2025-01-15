# Time complexity O(n)
# Space complexity O(n)


def numberOfSpecialChars(self, word: str) -> int:
        low = {}
        up = []
        for i in word:
            if i.islower():
                low[i] = i
            if i.isupper():
                up.append(i)
        answer = 0
        for i in low.keys():
            if i.upper() in up:
                answer += 1
        return answer