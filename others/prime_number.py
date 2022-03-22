def check_prime(n):
    if n < 2:
        return 'Not prime'
    else:
        for i in range(0, int(n**0.5)):
            if n % 2 == 0:
                return 'Not prime'
            else:
                return 'Prime'

print(check_prime(int(input())))
