# 自訂函數：count_primes() 函數
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

def count_primes(x, y):
    '''
    判斷介於輸入 x 與 y 之間的質數個數
    '''
    is_prime_lst = list(map(is_prime, range(x, y + 1)))
    primes_cnt = sum(is_prime_lst)
    return primes_cnt

print(count_primes(3, 7))
print(count_primes(3, 11))