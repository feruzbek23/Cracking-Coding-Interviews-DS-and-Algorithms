# Time O(n)
# Space O(1)


def minimumSteps(self, s: str) -> int:
    """
    black = 1
    white = 0
    """
    s = list(s)
    slow, fast = 0, 1
    result = 0
    while fast < len(s):
        if s[slow] == "1" and s[fast] == "0":
            s[slow], s[fast] = s[fast], s[slow]
            result += (fast - slow)
            slow += 1
        elif s[slow] == "0":
            fast += 1
            slow += 1
        else:
            fast += 1
    return result