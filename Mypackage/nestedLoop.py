

#easy solution is printing f
'''
numbers = [5,2,5,2,2]
for x in numbers:
    print(x * 'x')
'''
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

print('-' * 20)
    #print L

numbers = [2, 2, 2, 2, 6]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'

    print(output)