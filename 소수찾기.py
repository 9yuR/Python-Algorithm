##
#   출석인정과제 : 소수찾기
#   201821052_김규래
#
N_PRIMES = 50
number = 2
count = 0

while count < N_PRIMES:
    divisor = 2
    prime = True
    while prime:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1
    if divisor == number: 
        print(number, end=' ')
        count += 1
    number += 1 