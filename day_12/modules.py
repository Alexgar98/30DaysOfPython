import string
from random import randint

#Level 1
def random_user_id(length):
    possible_chars = string.ascii_letters + string.digits
    to_return = ''
    count = 0
    while count < length:
        to_return += possible_chars[randint(0, len(possible_chars) - 1)]
        count += 1
    return to_return

def user_id_gen_by_user():
    length = (int) (input("Length: "))
    ids = (int) (input("Number of IDs: "))
    id_list = []
    count = 0
    while count < ids:
        id_list.append(random_user_id(length))
        count += 1
    return id_list

def rgb_color_gen():
    return "rgb({},{},{})".format(randint(0, 255), randint(0, 255), randint(0, 255))

#Level 2
#Which one is task 6? There is no task 6
def list_of_hexa_colors(nbr):
    possible_chars = string.hexdigits
    to_return = []
    count = 0
    while count < nbr:
        red = randint(0,255)
        red_hex = possible_chars[(int)(red / 16)] + possible_chars[red % 10]
        green = randint(0,255)
        green_hex = possible_chars[(int)(green / 16)] + possible_chars[green % 10]
        blue = randint(0,255)
        blue_hex = possible_chars[(int)(blue / 16)] + possible_chars[blue % 10]
        to_return.append("#{}{}{}".format(red_hex, green_hex, blue_hex))
        count += 1
    return to_return

def list_of_rgb_colors(nbr):
    count = 0
    to_return = []
    while count < nbr:
        to_return.append(rgb_color_gen())
        count += 1
    return to_return

def generate_colors(mode, nbr):
    if mode == 'hexa':
        return list_of_hexa_colors(nbr)
    elif mode == 'rgb':
        return list_of_rgb_colors(nbr)
    else:
        return "Invalid mode"
    
#Level 3
def shuffle_list(list):
    to_return = [] #Should I keep the original? idk, I'm just putting this out
    while len(list) > 0:
        element = list[randint(0, len(list) - 1)]
        to_return.append(element)
        list.remove(element)
    return to_return

def random_numbers():
    possible_picks = list(range(0, 10))
    to_return = []
    count = 0
    while count < 7:
        pick = possible_picks[randint(0, len(possible_picks) - 1)]
        to_return.append(pick)
        possible_picks.remove(pick)
        count += 1
    return to_return
    
print(random_numbers())