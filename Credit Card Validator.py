ccno = input(
    'Welcome to Credit Card Validator.\nEnter your credit/debit card number: ')
bad_chars = [' ', '-']

for i in bad_chars:
    ccno = ccno.replace(i, '')
if len(ccno) < 13 or len(ccno) > 16:
    print('Enter a valid card number.')
else:
    if ccno[0] == '4':
        card = 'Visa'
    elif ccno[0] == '5':
        card = 'Master'
    elif ccno[0] == '6':
        card = 'Discover'
    elif ccno[0] == '3' and ccno[1] == '7':
        card = 'American Express'

    total = 0
    ccno_list = []

    for num in ccno:
        ccno_list.append(int(num))

    ccno_list.reverse()

    for i in range(1, len(ccno_list), 2):
        ccno_list[i] *= 2

    for num in ccno_list:
        if num > 9:
            for digit in str(num):
                total += int(digit)
        else:
            total += num

    print()
    if total % 10 == 0:
        print(f"It is a valid {card} card number.")
    else:
        print('It is an invalid card number.')
print('Validity above means that the number has the correct structure.\nIt does not mean that the number has actually been issued or is in good standing.')
