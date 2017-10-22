birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (or blank to cancel) ')
    name = input()
    if name =='':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of '+name)
    else:
        print('I do not have birthday information for '+ name)
        print('What is their birthday?')
        birthday = input()
        birthdays[name] = birthday
        print('Birthday DB is updated')