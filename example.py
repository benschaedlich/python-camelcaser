import camelcaser as cc
from terminaltables import AsciiTable


def print_table(title, data, headers=['Mode', 'Input', 'Output']):
    table_data = [headers] + data
    table = AsciiTable(table_data, title)
    table.inner_row_border = True
    print(table.table)
    print("\n")


# -------------------------------------------------
# Real Word examples without separators
# -------------------------------------------------
data = []
input_word = "verylongtestexample"

# Camel Case
camel_case = cc.make_camel_case(input_word)
data.append(["camel_case", input_word, camel_case])

# Lower Camel Case
lower_camel_case = cc.make_lower_camel_case(input_word)
data.append(["lower_camel_case", input_word, lower_camel_case])

# Snake Case
snake_case = cc.make_snake_case(input_word)
data.append(["snake_case", input_word, snake_case])

# Upper Snake Case
upper_snake_case = cc.make_upper_snake_case(input_word)
data.append(["upper_snake_case", input_word, upper_snake_case])

# Kebab Case
kebab_case = cc.make_kebab_case(input_word)
data.append(["kebab_case", input_word, kebab_case])

# Upper Kebab Case
upper_kebab_case = cc.make_upper_kebab_case(input_word)
data.append(["upper_kebab_case", input_word, upper_kebab_case])


print_table(title="Real Word examples without separators", data=data)



# -------------------------------------------------
# Examples with separators
# -------------------------------------------------

inputs = [
    'very_long_test_example',
    'very-long-test-example',
    'VeryLongTestExample',
    'veryLongTestExample',
]

data = []
for input_word in inputs:
    # Camel Case
    camel_case = cc.make_camel_case(input_word)
    data.append(["camel_case", input_word, camel_case])

    # Lower Camel Case
    lower_camel_case = cc.make_lower_camel_case(input_word)
    data.append(["lower_camel_case", input_word, lower_camel_case])

    # Snake Case
    snake_case = cc.make_snake_case(input_word)
    data.append(["lower_snake_case", input_word, snake_case])

    # Upper Snake Case
    upper_snake_case = cc.make_upper_snake_case(input_word)
    data.append(["upper_snake_case", input_word, upper_snake_case])

    # Kebab Case
    kebab_case = cc.make_kebab_case(input_word)
    data.append(["kebab_case", input_word, kebab_case])

    # Upper Kebab Case
    upper_kebab_case = cc.make_upper_kebab_case(input_word)
    data.append(["upper_kebab_case", input_word, upper_kebab_case])


print_table(title="Examples with separators", data=data)



# -------------------------------------------------
# Examples with custom separator [;]
# -------------------------------------------------

separator = ";"
inputs = [
    'very;long;test;example',
    'Very;Long;Test;Example',
]


data = []

for input_word in inputs:

    # Camel Case
    camel_case = cc.make_camel_case(input_word, separator=separator)
    data.append(["camel_case", input_word, camel_case])

    # Lower Camel Case
    lower_camel_case = cc.make_lower_camel_case(input_word, separator=separator)
    data.append(["lower_camel_case", input_word, lower_camel_case])

    # Snake Case
    snake_case = cc.make_snake_case(input_word, separator=separator)
    data.append(["lower_snake_case", input_word, snake_case])

    # Upper Snake Case
    upper_snake_case = cc.make_upper_snake_case(input_word, separator=separator)
    data.append(["upper_snake_case", input_word, upper_snake_case])

    # Kebab Case
    kebab_case = cc.make_kebab_case(input_word, separator=separator)
    data.append(["kebab_case", input_word, kebab_case])

    # Upper Kebab Case
    upper_kebab_case = cc.make_upper_kebab_case(input_word, separator=separator)
    data.append(["upper_kebab_case", input_word, upper_kebab_case])

print_table(title=f"Examples with custom separator [{separator}]", data=data)




# -------------------------------------------------
# Examples with custom separator [ ]
# -------------------------------------------------

separator = " "
inputs = [
    'very long test example',
    'Very Long Test Example',
]


data = []

for input_word in inputs:

    # Camel Case
    camel_case = cc.make_camel_case(input_word, separator=separator)
    data.append(["camel_case", input_word, camel_case])

    # Lower Camel Case
    lower_camel_case = cc.make_lower_camel_case(input_word, separator=separator)
    data.append(["lower_camel_case", input_word, lower_camel_case])

    # Snake Case
    snake_case = cc.make_snake_case(input_word, separator=separator)
    data.append(["lower_snake_case", input_word, snake_case])

    # Upper Snake Case
    upper_snake_case = cc.make_upper_snake_case(input_word, separator=separator)
    data.append(["upper_snake_case", input_word, upper_snake_case])

    # Kebab Case
    kebab_case = cc.make_kebab_case(input_word, separator=separator)
    data.append(["kebab_case", input_word, kebab_case])

    # Upper Kebab Case
    upper_kebab_case = cc.make_upper_kebab_case(input_word, separator=separator)
    data.append(["upper_kebab_case", input_word, upper_kebab_case])

print_table(title=f"Examples with custom separator [{separator}]", data=data)