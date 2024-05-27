"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    get_favorite_vegetable = input ("What's your favorite vegetable? ")
    start = "Interesting! I also love "
    end = "!"
    output_message = start + get_favorite_vegetable + end
    print(output_message)


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    get_favorite_number =  input ("What's your favorite number? ")
    start = "Interesting! I also love "
    end = "!"
    output_message = start + get_favorite_number + end
    print (output_message)


def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    get_name = input ("What's your name? ")
    get_zodiac_sign = input ("What is your zodiac sign? ")
    start = "Interesting! My name is also "
    middle = ", and I'm also a "
    end = "!"
    output_message = start + get_name + middle + get_zodiac_sign + end
    print (output_message)


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    get_name = input ("What's your name? ")
    get_age = input ("How old are you? ")
    start = "Interesting! My name is also "
    middle = ", and I'm also "
    end = " years old!"
    output_message = start + get_name + middle + get_age + end
    print (output_message)

