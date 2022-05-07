def check_prime(n):
    if n < 2:
        return 'Not prime'
    else:
        for i in range(2, n):
            if (n % i) == 0:
                return 'Not prime'

    return 'Prime'
                
print(check_prime(int(input())))