import re
import os
import enchant


PACKAGE_PATH = os.path.dirname(__file__)

def load_words():
    words = []
    with open(f"{PACKAGE_PATH}/word_lists/alpha_words.txt") as f:
        words.extend(f.readlines())
    return words


def process_word(string, words_db):
    matches = [e.strip() for e in words_db if string.startswith(e.strip())]
    real_word_matches = detect_real_words(matches)
    best_match = max(real_word_matches, key=lambda word: len(word))
    if not best_match:
        best_match = max(matches)
    return best_match


def normalize_string(string):
    string = string.replace(" ", "")
    string = string.strip()
    string = string.lower()
    return string


def detect_real_words(word_list):
    english_dict = enchant.Dict("en_US")
    real_words = [word for word in word_list if english_dict.check(word)]
    return real_words


def has_seperator(string):
    pattern = r'[A-Z_-]'
    matches = re.findall(pattern, string)
    if matches:
        sorted_matches = sorted(matches, key=lambda x: (not x.isalpha(), x))
        return sorted_matches[0] if sorted_matches else False
    return False


def split_camel_case(string):
    return re.findall('[A-Z][a-z]*', string)


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




def make_notation(string, max_iteration=30, mode="camel_case", separator=None):
    if not separator:
        separator = has_seperator(string)

    if separator:
        if separator.isalpha():
            string = string.capitalize()
            words = split_camel_case(string)
        else:
            words = string.split(separator)
        return format_string(words, mode.lower())


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
def make_camel_case(string, separator=None):
    return make_notation(string, mode="camel_case", separator=separator)

def make_lower_camel_case(string, separator=None):
    return make_notation(string, mode="lower_camel_case", separator=separator)

def make_snake_case(string, separator=None):
    return make_notation(string, mode="snake_case", separator=separator)

def make_upper_snake_case(string, separator=None):
    return make_notation(string, mode="upper_snake_case", separator=separator)

def make_kebab_case(string, separator=None):
    return make_notation(string, mode="kebab_case", separator=separator)

def make_upper_kebab_case(string, separator=None):
    return make_notation(string, mode="upper_kebab_case", separator=separator)

