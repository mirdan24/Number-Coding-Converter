process = True
import os


def binary(number):
    array = []
    correct_code = ''
    copy_of_number = number
    while copy_of_number != 0:
        array.append(copy_of_number % 2)
        copy_of_number = copy_of_number // 2
    for bit in range(len(array)):
        correct_code = correct_code + str(array[len(array)-(bit + 1)])
    return correct_code


def octal_code(number):
    result = ''
    this_number = binary(number)
    if len(this_number) % 3 != 0:
        miss_words = (len(this_number) % 3)
        additional_part = '0' * (3 - miss_words)
        this_number = additional_part + this_number
    process = True
    hexa_set = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
    while process:
        if len(this_number) == 0:
            process = False
        temporare_number = this_number[0:3]
        this_number = this_number[3:]
        if temporare_number in hexa_set.keys():
            result = result + str(hexa_set.get(temporare_number))
    return result


def hexadecimal_code(number):
    result = ''
    this_number = binary(number)
    if (len(this_number) % 4 != 0):
        miss_words = (len(this_number) % 4)
        additional_part = '0' * (4 - miss_words)
        this_number = additional_part + this_number
    process = True
    hexa_set = {'0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5', '0110':'6', '0111':'7',
                '1000':'8', '1001':'9','1010':'A', '1011':'B', '1100':'C', '1101':'D', '1110':'E','1111':'F'}
    while process:
        if len(this_number) == 0:
            process = False
        temporare_number = this_number[0:4]
        this_number = this_number[4:]
        if temporare_number in hexa_set.keys():
            result = result + str(hexa_set.get(temporare_number))
    return result


def decimal_type():
    value = int(input('Wprowadź wartość:'))
    print('1. Podana liczba na kod binarny')
    print('2. Podana liczba na kod ósemkowy')
    print('3. Podana liczba na kod szesnastkowy')
    print('4. Zakończ program')
    action = int(input('Którą akcję wybierasz? :'))
    if action == 1:
        result = binary(value)
        print('Liczba {} w postaci binarnej: {}'.format(value, result))
        return True
    elif action == 2:
        result = octal_code(value)
        print('Liczba {} w postaci ósemkowej: {}'.format(value, result))
        return True
    elif action == 3:
        result = hexadecimal_code(value)
        print('Liczba {} w postaci szesnastkowej: {}'.format(value, result))
        return True
    elif action == 4:
        return False
    print('\n' * 20)


def from_binary_to_decimal(binary):
    value = 0
    index = 1
    word_len = len(binary)
    for bit in binary:
        value += int(bit)*2**(word_len - index)
        index += 1
    return value


def binary_type():
    value = input('Wprowadź wartość:')
    print('1. Podana liczba na kod dziesiętny')
    print('2. Podana liczba na kod ósemkowy')
    print('3. Podana liczba na kod szesnastkowy')
    print('4. Zakończ program')
    action = int(input('Którą akcję wybierasz? :'))
    if action == 1:
        result = from_binary_to_decimal(value)
        print('Liczba {} w postaci dziesiętnej: {}'.format(value, result))
        return True
    elif action == 2:
        print("Narazie niedostępne. Pracujemy nad tą opcją :)")
        return True
    elif action == 3:
        print("Narazie niedostępne. Pracujemy nad tą opcją :)")
        return True
    elif action == 4:
        return False
    print('\n' * 20)




def which_type_input(type):
    process = True
    if type == "1":
        process = decimal_type()
    elif type == "2":
        process = binary_type()
    elif type == "3":
        print("Narazie niedostępne. Pracujemy nad tą opcją :)")
    elif type == "4":
        print("Narazie niedostępne. Pracujemy nad tą opcją :)")
    elif type == "5":
        process = False
    return process


while process:
    print('1. Decymalnym')
    print('2. Binarnym')
    print('3. Ósemkowy')
    print('4. Szesnastkowym')
    print('5. Zakończ program')
    type = input('W jakim kodzie wprowadzisz liczbę? :')
    print('\n' * 20)
    process = which_type_input(type)
