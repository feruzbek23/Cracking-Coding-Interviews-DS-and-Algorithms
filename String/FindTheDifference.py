# Time Complexity O(n)
# Space Complexity O(n)
# Difficulty : Easy

def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        for e in t:
            if e in hashmap:
                hashmap[e] += 1
            else:
                hashmap[e] = 1

        for id, count in hashmap.items():
            if count % 2 == 1:
                return id