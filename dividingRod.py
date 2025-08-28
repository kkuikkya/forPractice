def dividingRod(length):

    price = [0, 1, 5, 8, 9, 10, 17, 17, 20] # price[i] 는 판매하는 길이가 i 일때 받을 수 있는 금액
    maxPrice = [0 for _ in range(length + 1)] # maxPrice[i] 는 길이가 i 일때 rod 를 자를 수 있는 경우 받을 수 있는 최대 금액

    for i in range(1, length + 1):
        
        for j in range(0, min(i + 1, len(price))):
           tmp = price[j] + maxPrice[i-j]
           if tmp > maxPrice[i]:
               maxPrice[i] = tmp

    return maxPrice[length]

print(dividingRod(10))       