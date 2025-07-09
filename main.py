import matplotlib.pyplot as plt
import numpy as np


IMAGINARY = ('i', 'j')
OPERATIONS = ('+', '-', '*', ':')


def get_number(which):
    while True:
        complex_number = input(f"Pass {which} number: ")
        if '+' in complex_number:
            x, y = complex_number.split('+')
            if IMAGINARY[0] in y or IMAGINARY[1] in y:
                y = y.replace(IMAGINARY[0], '').replace(IMAGINARY[1], '')
                if 0 == len(y):
                    y = 1
                try:
                    final_complex_number = complex(int(x),int(y))
                    return final_complex_number
                except ValueError:
                    print('Wrong number!')
                    pass
            elif IMAGINARY[0] in x or IMAGINARY[1] in x:
                x = x.replace(IMAGINARY[0], '').replace(IMAGINARY[1], '')
                if 0 == len(x):
                    x = 1
                try:
                    final_complex_number = complex(int(y),int(x))
                    return final_complex_number
                except ValueError:
                    print('Wrong number!')
                    pass
            else:
                print('Something went wrong!')
        elif '-' in complex_number:
            helper = complex_number.count('-')
            match helper:
                case 1:
                    x, y = complex_number.split('-')
                    if IMAGINARY[0] in y or IMAGINARY[1] in y:
                        y = y.replace(IMAGINARY[0], '').replace(IMAGINARY[1], '')
                        if 0 == len(y):
                            y = 1
                        if 0 == len(x):
                            x = 0
                        try:
                            final_complex_number = complex(int(x), -int(y))
                            return final_complex_number
                        except ValueError:
                            print('Wrong number!')
                            pass
                    elif IMAGINARY[0] in x or IMAGINARY[1] in x:
                        x = x.replace(IMAGINARY[0], '').replace(IMAGINARY[1], '')
                        if 0 == len(x):
                            x = 1
                        try:
                            final_complex_number = complex(-int(y), int(x))
                            return final_complex_number
                        except ValueError:
                            print('Wrong number!')
                            pass
                    else:
                        print('Something went wrong!')
                case 2:
                    _, x, y = complex_number.split('-')
                    if IMAGINARY[0] in y or IMAGINARY[1] in y:
                        y = y.replace(IMAGINARY[0], '').replace(IMAGINARY[1], '')
                        if 0 == len(y):
                            y = 1
                        try:
                            final_complex_number = complex(-int(x), -int(y))
                            return final_complex_number
                        except ValueError:
                            print('Wrong number!')
                            pass
                    elif IMAGINARY[0] in x or IMAGINARY[1] in x:
                        x = x.replace(IMAGINARY[0], '').replace(IMAGINARY[1], '')
                        if 0 == len(x):
                            x = 1
                        try:
                            final_complex_number = complex(-int(y), -int(x))
                            return final_complex_number
                        except ValueError:
                            print('Wrong number!')
                            pass
                    else:
                        print('Something went wrong!')
        else:
            if IMAGINARY[0] in complex_number or IMAGINARY[1] in complex_number:
                complex_number = complex_number.replace(IMAGINARY[0], '').replace(IMAGINARY[1], '')
                if 0 == len(complex_number):
                    complex_number = 1
                try:
                    final_complex_number = complex(0,int(complex_number))
                    return final_complex_number
                except ValueError:
                    print('Wrong number!')
                    pass
            else:
                try:
                    final_complex_number = complex(int(complex_number),0)
                    return final_complex_number
                except ValueError:
                    print('Wrong number!')


def choose_operation():
    while True:
        operation = input("Choose operation (+, -, *, :): ")
        if operation in OPERATIONS:
            return(operation)
        else:
            print('Wrong value!')
            pass


def calculate(first_complex_number, operation, second_complex_number):
    match operation:
        case '+':
            sum_of_given_numbers = (first_complex_number + second_complex_number)
            print(sum_of_given_numbers)
            return sum_of_given_numbers
        case '-':
            differance_of_given_numbers = first_complex_number - second_complex_number
            print(differance_of_given_numbers)
            return differance_of_given_numbers
        case '*':
            multiplication_of_given_numbers = first_complex_number * second_complex_number
            print(multiplication_of_given_numbers)
            return multiplication_of_given_numbers
        case ':':
            division_of_given_numbers = first_complex_number / second_complex_number
            print(division_of_given_numbers)
            return division_of_given_numbers



def plot(array_data):
    data = np.array(array_data)
    x = data.real
    y = data.imag
    plt.plot(x, y, 'bo')
    for i in range(len(x) - 1):
        dx = x[i+1] - x[i]
        dy = y[i+1] - y[i]
        plt.arrow(x[i], y[i], dx, dy, 
                  head_width=0.05, head_length=0.1, 
                  length_includes_head=True, color='blue')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    first_number = get_number('first')
    operation = choose_operation()
    second_number = get_number('second')
    result = calculate(first_number, operation, second_number)
    plot([first_number, second_number, result])