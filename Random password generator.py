import secrets
import string

print('--------YOU CAN GENERATE YOUR PASSWORD HERE-------')

a=str('alphabets')

n=str('numbers')

s=str('symbols')

alphabets = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

combination = alphabets + numbers + symbols


length = int(input('Enter your length of the password :'))


password = ''
for i in range(length):
    password += ''.join(secrets.choice(combination))

print('this is your password :',password)
print('******your password successfully generated******')