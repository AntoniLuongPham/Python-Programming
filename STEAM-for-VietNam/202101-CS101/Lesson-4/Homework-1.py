import random


def get_random_item(items):
    # hoc sinh lam bai tai day
    return random.choice(items)


array = [1, 2, 3, 4, 5]
print(get_random_item(array))
