from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
chars = ''

num_pw = int(input('Укажите количество паролей для генерации:'))
lenght_pw = int(input('Укажите длину пароля:'))
numbers_pw = input('Включать в пароль цифры - "0123456789" ?').lower()
upper_pw = input('Включать в пароль буквы верхнего регистра - "ABCDEFGHIJKLMNOPQRSTUVWXYZ" ?').lower()   
lower_pw = input('Включать в пароль буквы нижнего регистра - "abcdefghijklmnopqrstuvwxyz" ?').lower()
symbols_pw = input('Включать в пароль символы - "!#$%&*+-=?@^_" ?').lower()
not_symbols_pw = input('Исключать неоднозначные символы - "il1Lo0O" ?').lower()  

if numbers_pw == 'да':
    chars = chars + digits
if upper_pw == 'да':
    chars = chars + uppercase_letter
if lower_pw == 'да':
    chars = chars + lowercase_letters
if symbols_pw == 'да':
    chars = chars + punctuation
if not_symbols_pw == 'да':
    chars = chars.replace('i', '')
    chars = chars.replace('l', '')
    chars = chars.replace('1', '')
    chars = chars.replace('L', '')
    chars = chars.replace('o', '')
    chars = chars.replace('0', '')
    chars = chars.replace('O', '')

#Генерация пароля
def generate_password(password):
    num2 = ''
    for i in range(lenght_pw):
        num = randrange(len(chars))
        num2 += chars[num] 
    return num2

for i in range(num_pw):
    print(generate_password(chars))

