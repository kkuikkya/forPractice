def bitonic(arr):

    memoI = [1 for i in range(len(arr))]
    memoD = [1 for i in range(len(arr))]


    for i in range(len(arr)):
        for j in range(i):
            if arr[i] >= arr[j] and memoI[i] < memoI[j] + 1:
                memoI[i] = memoI[j] + 1
                
               
    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr)-1, i, -1):
            if arr[i] >= arr[j] and memoD[i] < memoD[j] + 1:
                memoD[i] = memoD[j] + 1

    memoB = []
    for i in range(len(arr)):
        memoB.append(memoI[i] + memoD[i] - 1)
                

    
    maxVal = max(memoB)
    maxidx = memoB.index(maxVal)
    result = [arr[maxidx]]
    recent = maxidx

    for i in range(maxidx - 1 ,-1, -1):
        if arr[i] <= arr[recent] and memoI[i] == memoI[recent] - 1:
            result = [arr[i]] + result
            recent = i

    recent = maxidx
    for i in range(maxidx + 1 , len(arr)):
        if arr[i] <= arr[recent] and memoD[i] == memoD[recent] - 1:
            result = result + [arr[i]]
            recent = i


    print(result)

    


    return max(memoB)

arr = [1, 100, 2, 5, 70, 30, 40]
print(bitonic(arr))


