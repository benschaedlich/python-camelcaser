import os

PACKAGE_PATH = os.path.dirname(__file__)


def load_words():
    words = []
    with open(f"{PACKAGE_PATH}/word_lists/alpha_words.txt") as f:
        words.extend(f.readlines())
    return words


def process_word(string, words_db):
    matches = [e.strip() for e in words_db if string.startswith(e.strip())]
    best_match = max(matches, key=lambda word: len(word))
    return best_match


def normalize_string(string):
    string = string.replace(" ", "")
    string = string.strip()
    string = string.lower()
    return string


def format_string(words_list, mode):
    if mode == "camel_case":
        camel_case = ''.join(word.capitalize() for word in words_list)
        return camel_case
    
    elif (mode == "lower_camel_case"):
        camel_case = ''.join(word.capitalize() for word in words_list)
        return camel_case[0].lower() + camel_case[1:]
    
    elif (mode == "snake_case"):
        snake_case = '_'.join(word for word in words_list)
        return snake_case
    
    elif (mode == "upper_snake_case"):
        snake_case = '_'.join(word.capitalize() for word in words_list)
        return snake_case

    elif (mode == "kebab_case"):
        kebab_case = '-'.join(word for word in words_list)
        return kebab_case

    elif (mode == "upper_kebab_case"):
        kebab_case = '-'.join(word.capitalize() for word in words_list)
        return kebab_case

    else:
        raise Exception("Unknown mode.")


def make_notation(string, max_iteration=30, mode="camel_case"):
    string = normalize_string(string)
    words_db = load_words()

    i = 0
    words = []
    while (not len(string) == 0) or (i == max_iteration):
        word = process_word(string, words_db)
        string = string.replace(word, "")
        words.append(word)
        i+=1

    if i == 50:
        raise Exception("Max iterations exceeded")
    return format_string(words, mode.lower())



# Wrapper Functions
#-----------------------------------------#
def make_camel_case(string):
    return make_notation(string, mode="camel_case")

def make_lower_camel_case(string):
    return make_notation(string, mode="lower_camel_case")

def make_snake_case(string):
    return make_notation(string, mode="snake_case")

def make_upper_snake_case(string):
    return make_notation(string, mode="upper_snake_case")

def make_kebab_case(string):
    return make_notation(string, mode="kebab_case")

def make_upper_kebab_case(string):
    return make_notation(string, mode="upper_kebab_case")

