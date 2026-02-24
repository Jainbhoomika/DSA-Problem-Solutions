#Selection Sort Algorithm
def selection_sort(arr):
  n = len(arr)-1
  for i in range(n):
    min_item = min(arr[i:])
    if arr[i] > min_item:
      min_idx = arr.index(min_item)
      arr[i] , arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
  array = [2,34,5,3,6,17,28,37]
  print(f"Original Array: {array}")
  selection_sort(array)
  print("Sorted Array:", array)
