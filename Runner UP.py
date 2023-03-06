def findSecondMaximum(arr):
    maxNum = float('-inf')
    secondMax = float('-inf')
    for num in arr:
        if num > maxNum:
            secondMax = maxNum
            maxNum = num
        elif num > secondMax and num != maxNum:
            secondMax = num
    return secondMax

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = findSecondMaximum(arr)
    print(result)
