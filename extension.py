from random import randint, shuffle, sample
# create a binary string with size l
def create_random_binary_string(l_size):
    binary_string = ''
    for i in range(l_size):
        binary_string += str(randint(0, 1))
    return binary_string

def shuffle_list_randomly(list):
    shuffle(list)

def select_random(list):
    return sample(list, 1)[0]

def select_2_randoms(list):
    first_individuals = select_random(list)
    second_individuals = select_random(list)
    return first_individuals, second_individuals
