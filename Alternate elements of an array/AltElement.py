# Given an array arr[], the task is to print every alternate element of the array starting from the first element.
#  nput: arr[] = [10, 20, 30, 40, 50]
# Output: 10 30 50
# Explanation: Print the first element (10), skip the second element (20), print the third element (30), skip the fourth element(40) and print the fifth element(50).

# Input: arr[] = [-5, 1, 4, 2, 12]
# Output: -5 4 12

def getAlternates(arr):
    result = []
    arrsize = len(arr)
    for i in range(0,arrsize,2):
        result.append(arr[i])
    return result

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    result = getAlternates(arr)
    print("Output:", result)
        
        