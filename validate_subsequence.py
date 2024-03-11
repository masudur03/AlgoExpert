# O(n)
def isValidSubsequence(array, sequence):
    # Write your code here.
    # check is the num in sequence also in array
    prevIndex = -1
    for i in range(len(sequence)):
        output = False
        for j in range(len(array)):
            if sequence[i] == array[j] and j > prevIndex:
                output = True
                prevIndex = j
                break
        if output == False:
            return False

    return True
