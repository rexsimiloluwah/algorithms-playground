# Implementation of Binary search algorithm in python

class BinarySearch:
    def searchRecursively(self, arr, target, low, high):
        """
            Returns the index of a target element in a specific array
        """
        if high >= low:
            # arr.sort()
            mid = low + (high - low)//2

            if arr[mid] == target:
                return mid
            else:
                if arr[mid] > target:
                    return self.search(arr, target, low, mid-1)
                elif arr[mid] < target:
                    return self.search(arr, target, mid+1, high)

    @staticmethod
    def searchUsingLoops(arr, target, low, high):
        
        while low <= high:
            mid = low + (high - low)//2

            if arr[mid] == target:
                return mid
                break
            else:
                if arr[mid] > target:
                    high = mid -1
                elif arr[mid] < target:
                    low = mid + 1

if __name__ == "__main__":
    binarysearch = BinarySearch()
    arr = [1,2,3,4,5,7,9,12,0]
    low, high = 0, len(arr) - 1
    print(binarysearch.searchRecursively(arr, 7, low, high))
    print(binarysearch.searchUsingLoops(arr, 7, low, high))
        