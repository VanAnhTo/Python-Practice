while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Pls enter a number for your age.')
while True:
    print('Select a new password (letters and number only): ')
    password = input()
    if password.isalnum():
        break
    print('Password can only have letters and numbers.')
print('Done.')