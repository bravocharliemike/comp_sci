import random


def random_list(quantity, minimum, maximum):
    """
    Sets a random list ....
    :param quantity:
    :param minimum:
    :param maximum:
    :return: list with quantity random integers between minimum and maximum
    """
    final_list = [random.randint(minimum, maximum) for number in range(quantity)]
    return final_list

# TODO implement all the code from the Linux machine