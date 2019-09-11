Area = input('please enter your area: ')
Products = input('enter your products:')


amount_EU1 = float(input('Please enter a amount1 for EU cig:'))
amount_EU2 = float(input('Please enter a amount2 for EU alc:'))
amount_EU3 = float(input('Please enter a amount3 for EU others:'))

amount_UK4 = float(input('Please enter a amount4 for UK alc:'))
amount5_UK = float(input('Please enter a amount5 for UK others:'))

amount_Germ6 = float(input('Please enter a amount6 for Germ cig:'))
amount_Germ7 = float(input('Please enter a amount7 for Germ others:'))

amount_France8 = float(input('Please enter a amount8 for France cig:'))
amount_France9 = float(input('Please enter a amount9 for France alc:'))

amount_Spain10 = float(input('Please enter a amount10 for Spain cig:'))
amount_Spain11 = float(input('Please enter a amount10 for Spain alc:'))
amount_Spain12 = float(input('Please enter a amount10 for Spain others:'))

amount_Poland13 = float(input('Please enter a amount10 for Poland others:'))


amount_EU1 *= 0.30
amount_EU2 *= 0.20
amount_EU3 *= 0.15

amount_UK4 *= 0.25
amount_UK5 = 2.00

amount_Germ6 *= 0.30
amount_Germ7 = 2.00

amount_France8 *= 0.40
amount_France9 *= 0.25

amount_Spain10 *= 0.10
amount_Spain11 *= 0.10
amount_Spain12 *= 0.10

amount_Poland13 *= 0.10



if (Area =='EU') and Products == ('cig') :
    print("You have  30 percent tax for cig: $" + format(amount_EU1, ",.2f"))
elif (Area == 'EU') and Products == ('alc'):
    print("You have  20 percent tax for alc: $" + format(amount_EU2, ",.2f"))
elif (Area == 'EU') and Products == ('cig'):
 print("You have  15 percent tax for others: $" + format(amount_EU3, ",.2f"))
else:
    print('not acceptable')

if (Area == 'UK') and Products == ('cig') :
    print("You have  25 percent tax for cig: $" + format(amount_UK4, ",.2f"))
elif (Area == 'UK') and Products == ('others'):
    print("You have  tax for 75 cl wine : $" + format(amount_UK5, ",.2f"))
else:
    print('You have  tax for 75 cl wine: $ 2.00 ')

if (Area =='Germ') and Products == ('cig') :
    print("You have  30 percent tax for  : $" + format(amount_Germ6, ",.2f"))
elif (Area == 'Germ') and Products == ('others'):
    print("You have  tax for after first 2$ in all products : $" + format(amount_Germ7, ",.2f"))
else:
    print('first 2$ on all products is not taxable')

if (Area =='France') and Products == ('cig') :
    print("You have  40 percent tax for  : $" + format(amount_France8, ",.2f"))
elif (Area == 'France') and Products == ('alc'):
    print("You have  25 percent tax for  : $" + format(amount_France9, ",.2f"))
else:
    print("not acceptable")

if (Area =='Spain') and Products == ('cig') :
    print("You have  10 percent tax for  : $" + format(amount_Spain10, ",.2f"))
elif (Area =='Spain') and Products == ('alc') :
    print("You have  10 percent tax for  : $" + format(amount_Spain11, ",.2f"))
elif (Area =='Spain') and Products == ('others') :
    print("first 4$ of all products are not payable  : $" + format(amount_Spain12, ",.2f"))
else:
    print('first 4$ of all products are not taxable')

if (Area =='Poland') and Products == ('others') :
    print("first 0.23$ of all products are not taxable: $" + format(amount_Poland13, ",.2f"))
else:
    print('not taxable')








