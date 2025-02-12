# Time O(n * m)
# Space O(n * m)

def rotateTheBox(self, boxGrid: str) -> str:

        new_matrix = [[0] * len(boxGrid) for _ in range(len(boxGrid[0]))]
        print(new_matrix)        
        for box in boxGrid:
            slow, right = 0, 1
            while right <= len(boxGrid[0])-1:
                if box[slow] == "#" and  box[right] == ".":
                    box[slow], box[right] = box[right], box[slow]
                    slow += 1
                    right += 1
                elif box[right] == "*":
                    slow = right + 1
                    right += 1
                elif box[right] == "#" and box[slow] != "#":
                    slow = right
                    right += 1 
                else:
                    right += 1
        
        for row in range(len(boxGrid)):
            for col in range(len(boxGrid[row])):        
                new_matrix[col][len(boxGrid) - row - 1] = boxGrid[row][col]
                
        return new_matrix