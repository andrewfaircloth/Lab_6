# Name: Andrew Faircloth Collaborator: Pablo Sabogal
def encode(password):
    int_list = []
    final_string = ''
    for i in password:
        num = int(i) + 3
        if num > 9:
            num -= 10
        int_list.append(num)
    for i in int_list:
        final_string += str(i)
    return final_string

def decode(new_password):
    final_number = []
    for number in new_password:
        if int(number) < 3:
            number = int(number) +7
        else:
            number = int(number) - 3
        final_number.append(str(number))
    new_password = ''.join(final_number)
    return new_password

def main():
    loop_go = True
    while loop_go:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            password = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            print()
            new_password = encode(password)
        elif menu_option == 2:
            decoded_password = decode(new_password)
            print(f'The encoded password is {new_password}, and the original password is {decoded_password}.')
            print()
        elif menu_option == 3:
            loop_go = False


if __name__ == "__main__":
    main()