# Space O(1)
# Time O(n)

def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        """
        0 = red
        1 = blue
        """
        count = 0
        for curr in range(len(colors)):
            left, right = curr - 1, curr + 1
            if curr == len(colors)-1:
                right = 0
                if colors[curr] == 0 and colors[left] and colors[right] == 1: 
                    count += 1
                elif colors[curr] == 1 and colors[left] == 0 and colors[right] == 0: 
                    count += 1
            elif (colors[curr] == 1 and colors[left] == 0 and colors[right] == 0) or (colors[curr] == 0 and colors[left] == 1 and colors[right] == 1):
                count += 1

        return count