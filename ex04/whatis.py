
import sys


def check_odd_or_even(number):
    if number % 2 == 0:
        return "I'm Even."
    else:
        return "I'm Odd."


try:
    try:
        if len(sys.argv) < 2:
            exit()
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provied")

    result = check_odd_or_even(number)
    print(result)

except AssertionError as error:
    print(AssertionError.__name__ + ":", error)
