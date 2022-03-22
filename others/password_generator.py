# Password generator by Ricardo
import random

passwords_abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%*()"
passwords_num = "1234567890"

aux = 0

while aux == 0:
    password_len = int(input('\nQual será o tamanho da senha? '))
    password_abc = int(input('\nQual será o número de letras? '))
    password_num = int(input('\nQual será o número de números? '))

    if password_abc + password_num > password_len:
        print('\nO número de letras e números não pode ser maior'
              'que o tamanho da senha definido pelo usuário!')
        
    if password_abc + password_num < password_len:
        print('\nO número de letras e números não pode ser menor'
              'que o tamanho da senha definido pelo usuário!')

    else:
        aux = 1


p_abc = random.sample(passwords_abc, password_abc)
p_num = random.sample(passwords_num, password_num)

p = "".join(random.sample(p_abc + p_num, password_len))

print("\n", p)
