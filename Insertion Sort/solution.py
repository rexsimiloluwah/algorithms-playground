import time 
import random 

class InsertionSort:
    @staticmethod 
    def sort(arr, reverse:bool=False):
        for i in range(1,len(arr)):
            temp = arr[i]
            j = i-1 
            while j >= 0 and arr[i] < arr[j]:
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = temp 
        if reverse:
            return list(reversed(arr))
        return arr 

if __name__ == '__main__':
    i =InsertionSort()
    arr1 = random.sample(range(1,1000), 100)
    print(i.sort([1,0,2,4,3,7,5], True))