import time
import random 

class SelectionSort:
    @staticmethod 
    def sort(arr:list, reverse:bool=False) -> list:
        for i in range(len(arr)-1):
            for j in range(i, len(arr)):
                if reverse:
                    if arr[i] < arr[j]:
                        temp = arr[j]
                        arr[j] = arr[i]
                        arr[i] = temp 
                else:
                    if arr[i] > arr[j]:
                        temp = arr[j]
                        arr[j] = arr[i]
                        arr[i] = temp 

        return arr 

if __name__ == '__main__':
    s = SelectionSort()
    start = time.time()
    arr1 = random.sample(range(0,100000), 10000)
    print(s.sort(arr1, True))
    end = time.time()
    print(f'Time elapsed: {end - start}s')