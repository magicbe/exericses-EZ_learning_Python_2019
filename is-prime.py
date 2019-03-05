# 自訂函數：is_prime() 函數
def is_prime(x):
    '''
    判斷輸入的正整數是否為質數，是則回傳 True，否則回傳 False
    '''
    factorials = []
    for i in range(1, x + 1):
        if x % i == 0:
            factorials.append(i)
    if len(factorials) == 2:
        return True
    else:
        return False

print(is_prime(87))
print(is_prime(89))