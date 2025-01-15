# Time: O(1)
# Space: O(1)


class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        start = t - 3000
        self.requests.append(t)
        n = len(self.requests)
        while n != 0:
            if self.requests[0] < start:
                self.requests.pop(0)
            n -= 1

        return len(self.requests)
      


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)