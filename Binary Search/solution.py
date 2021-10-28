# Implementation of Binary search algorithm in python

class BinarySearch:
    def search_recursively(self, arr, target, low, high):
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
    def search_iteratively(arr, target, low, high):
        while low <= high:
            mid = low + (high - low)//2

            if arr[mid] == target:
                return mid
            else:
                if arr[mid] > target:
                    high = mid -1
                elif arr[mid] < target:
                    low = mid + 1

if __name__ == "__main__":
    binarysearch = BinarySearch()
    arr = [1,2,3,4,5,7,9,12,0]
    low, high = 0, len(arr) - 1
    print(binarysearch.search_recursively(arr, 7, low, high))
    print(binarysearch.search_iteratively(arr, 7, low, high))
        