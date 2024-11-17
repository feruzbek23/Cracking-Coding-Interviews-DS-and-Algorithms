# Time O(n)
# Space O(1)


def searchMatrix(matrix, target: int) -> bool:
        def binary_search(nums, target):
            left, right = 0, len(nums)-1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
        for arr in matrix:
            print(binary_search(arr, target))
            if binary_search(arr, target):
                return True
        return False