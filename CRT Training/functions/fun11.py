#write a rec fun to count the no of digits of  a num


def countDigit(n):
    if n//10 == 0:
        return 0
    return (1 + countDigit(n // 10))
        
print(countDigit(123456))


