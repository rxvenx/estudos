number = int(input('choose a number between 0 and 14: '))

if number < 7 :
    level = 'acidic'
elif number > 7:
    level = 'basic'
else :
    level = 'neutral'


print('you choose', number, 'and this is', level)