
# guess the secret Number
Secret_num = 9
guess_num = 0
guess_limit = 3
while guess_num < guess_limit:
    guess = int(input('guess the number from 0 - 9: ->'))
    guess_num += 1
    if guess == Secret_num:
        print('you win !')
        break

else:
    print('sorry you failed')
