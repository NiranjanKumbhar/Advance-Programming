# Your goal in this assignment is to change each function in order to make all of the doctests to pass.
# To grade your code, I will run all the tests, if they fail, you won't get the complete marks for the question, even
# if your code/logic seems right. So take time to make sure that all the tests are passing.
# You can check on BB announcements how to run the tests on your .py file.
# This assignment worth 5% of your grade.

# 1. Given an "out" string length 4, such as "<<>>", and a word, print a new string where the word is in the middle
# of the out string, e.g. "<<word>>".
def make_out_word(out, word):
    """
    :param out: string with len 4
    :param word: string
    :return: prints a new string where the word is in the middle of the out string
    >>> make_out_word('<<>>', 'Yay')
    <<Yay>>
    >>> make_out_word('<<>>', 'WooHoo')
    <<WooHoo>>
    >>> make_out_word('[[]]', 'my word')
    [[my word]]
    """
    complete = out[0:2] + word + out[2:]
    print(complete)


# 2. Given a string, return a version without the first and last char, so "Hello" yields "ell".
# The input string length must be at least 3.
def without_end(word):
    """
    :param word: string with at least 3 chars.
    :return: prints the input string without the first and the last char.
    >>> without_end('Hello')
    ell
    >>> without_end('coding')
    odin
    >>> without_end('Business')
    usines
    """
    output = word[1:-1]
    print(output)


# 3. When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the
# number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper
# bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
def cigar_party(cigars_number, is_weekend):
    """
    :param cigars_number: integer - number of cigars
    :param is_weekend: boolean - if is weekend or not
    :return: boolean - representing if the party was a success or not
    >>> cigar_party(30, False)
    False
    >>> cigar_party(50, False)
    True
    >>> cigar_party(70, True)
    True
    """
    if is_weekend and cigars_number >= 40:
        return True
    elif not is_weekend and (40 <= cigars_number <= 60):
        return True
    return False


# 4. Given a string, return a string where for every char in the original, there are two chars.
def double_char(word):
    """
    :param word: string
    :return: prints a string where for every char in the original, there are two chars
    >>> double_char('The')
    TThhee
    >>> double_char('AAbb')
    AAAAbbbb
    >>> double_char('Hi-There')
    HHii--TThheerree
    """
    output = ""

    for x in word:
        output += x + x

    print(output)


# 5. Return the number of even ints in the given list.
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(list):
    """
    :param list: list with integer numbers
    :return: integer with the number of even ints in the given list
    >>> count_evens([2, 1, 2, 3, 4])
    3
    >>> count_evens([2, 2, 0])
    3
    >>> count_evens([1, 3, 5])
    0
    """
    count = 0
    for x in list:
        if x % 2 == 0:
            count += 1

    return count


# 6. Given an array length 1 or more of ints, return the difference between the largest and smallest values in the list.
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(list):
    """
    :param list: list with integer numbers
    :return: integer with the difference between the largest and smallest values in the input list
    >>> big_diff([10, 3, 5, 6])
    7
    >>> big_diff([7, 2, 10, 9])
    8
    >>> big_diff([7, 2, 10, 9])
    8
    """
    small = large = list[0]
    for x in list:
        small = min(x, small)
        large = max(x, large)

    return large-small


# 7. Little John wants to calculate and show the amount of spent fuel liters on a trip,
# using a car that does 12 Km/L. For this, he would like you to help him through a simple program.
# To perform the calculation, you have to read spent time (in hours) and the same average speed (km/h).
# In this way, you can get distance and then, calculate how many liters would be needed.
# Show the value with three decimal places after the point.

def spent_fuel(spent_time, average_speed):
    """
    Function to calculate and show the amount of spent fuel liters on a trip.

    :param spent_time: integer representing the spent time in the trip (in hours)
    :param average_speed: integer representing the average speed during the trip (in Km/h)
    :return: float: how many liters would be needed to do this trip, with three digits after the decimal point

    >>> spent_fuel(10, 85)
    70.833
    >>> spent_fuel(2, 92)
    15.333
    >>> spent_fuel(22, 67)
    122.833
    """
    return round((spent_time * average_speed)/12, 3)


# 8. The company ABC decided to give a salary increase to its employees, according to the following table:
#
# Salary	                   Readjustment Rate
# 0 - 400.00                   15%
# 400.01 - 800.00              12%
# 800.01 - 1200.00             10%
# 1200.01 - 2000.00            7%
# Above 2000.00                4%
#
# Create a function that receives the employee's salary, calculate and return the new employee's salary, as well the
# money earned and the increase percent obtained by the employee, with corresponding messages as the below examples (on
# docstring).


def salary_increase(salary):
    """
    Receives the employee's salary, calculate and PRINT the new employee's salary, as well the
    money earned and the increase percent obtained by the employee
    :param salary: float with 2 digits after the decimal point.
    :return: prints a string with information on New Salary, Money earned and Readjustment rate
    >>> salary_increase(400.00)
    New Salary: 460.00
    Money earned: 60.00
    Readjustment rate: 15%
    >>> salary_increase(800.01)
    New Salary: 880.01
    Money earned: 80.00
    Readjustment rate: 10%
    >>> salary_increase(2000.00)
    New Salary: 2140.00
    Money earned: 140.00
    Readjustment rate: 7%
    """
    if 0 < salary <= 400:
        rate = 15
    elif 400 < salary <= 800:
        rate = 12
    elif 800 < salary <= 1200:
        rate = 10
    elif 1200 < salary <= 2000:
        rate = 7
    else:
        rate = 4

    increment = salary * rate / 100

    # Example on how you can print the results to match the expected format
    print(f'New Salary: {increment+salary:.2f}')
    print(f'Money earned: {increment:.2f}')
    print("Readjustment rate: "+str(rate)+"%")


# 9. Implement the function foo_bar_qix which implements the following rules.
# If the number is divisible by 3, print “Foo” instead of the number
# If the number is divisible by 5, add “Bar”
# If the number is divisible by 7, add “Qix”
# For each digit 3, 5, 7, add “Foo”, “Bar”, “Qix” in the digits order.
def foo_bar_qix(number):
    """
    :param number: integer
    :return: prints a string following the rules of the function
    >>> foo_bar_qix(1)
    1
    >>> foo_bar_qix(2)
    2
    >>> foo_bar_qix(3)
    FooFoo
    >>> foo_bar_qix(4)
    4
    >>> foo_bar_qix(5)
    BarBar
    >>> foo_bar_qix(6)
    Foo
    >>> foo_bar_qix(7)
    QixQix
    >>> foo_bar_qix(8)
    8
    >>> foo_bar_qix(9)
    Foo
    >>> foo_bar_qix(10)
    Bar
    >>> foo_bar_qix(13)
    Foo
    >>> foo_bar_qix(15)
    FooBarBar
    >>> foo_bar_qix(21)
    FooQix
    >>> foo_bar_qix(33)
    FooFooFoo
    >>> foo_bar_qix(51)
    FooBar
    >>> foo_bar_qix(53)
    BarFoo
    """
    final_string = ''
    if number % 3 == 0:
        final_string += 'Foo'
    if number % 5 == 0:
        final_string += 'Bar'
    if number % 7 == 0:
        final_string += 'Qix'

    for x in str(number):
        if x == '3':
            final_string += 'Foo'
        elif x == '5':
            final_string += 'Bar'
        elif x == '7':
            final_string += 'Qix'

    if final_string == '':
        print(number)
    else:
        print(final_string)


# 10. The previous problem has a new request:
# we must keep a trace of 0 in numbers, each 0 must be replaced by char “*“.
def foo_bar_qix_2(number):
    """
    :param number: integer
    :return: prints a string following the rules of the function
    >>> foo_bar_qix_2(101)
    1*1
    >>> foo_bar_qix_2(303)
    FooFoo*Foo
    >>> foo_bar_qix_2(105)
    FooBarQix*Bar
    >>> foo_bar_qix_2(10101)
    FooQix**
    """

    final_string = ''
    special_case = False
    if number % 3 == 0:
        final_string += 'Foo'
        special_case = True
    if number % 5 == 0:
        final_string += 'Bar'
        special_case = True
    if number % 7 == 0:
        final_string += 'Qix'
        special_case = True

    for x in str(number):
        if x == '3':
            final_string += 'Foo'
        elif x == '5':
            final_string += 'Bar'
        elif x == '7':
            final_string += 'Qix'
        elif x == '0':
            final_string += '*'
        else:
            if special_case:
                continue
            else:
                final_string += x

    if final_string == '':
        print(number)
    else:
        print(final_string)
