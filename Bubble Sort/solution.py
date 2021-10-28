# Implementation of the Bubble Sort algorithm 
class BubbleSort:
    @staticmethod
    def sort(arr, order = "ascending"):
        """
            Sorts an array in ascending or descending order
        """
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if order == "ascending":
                    if arr[j] > arr[j+1]:
                        # Swap the variables 
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
                elif order == "descending":
                    if arr[j] < arr[j+1]:
                        # Swap the variables 
                        temp = arr[j]
                        arr[j] = arr[j+1]
                        arr[j+1] = temp
        return arr

if __name__ == "__main__":
    bubble = BubbleSort()
    print(bubble.sort([50,20,10,40,30], "descending")) # Returns [50,40,30,20,10]
    print(bubble.sort([50,20,10,40,30])) # Returns [10,20,30,40,50]


