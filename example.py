import camelcaser as cc

input = "handlingunits"


# Camel Case
# -------------------------------------------------#
camel_case = cc.make_camel_case(input)
print(f"Camel case: {camel_case}")


# Lower Camel Case
# -------------------------------------------------#
lower_camel_case = cc.make_lower_camel_case(input)
print(f"Lower camel case: {lower_camel_case}")


# Snake Case
# -------------------------------------------------#
snake_case = cc.make_snake_case(input)
print(f"Snake case: {snake_case}")


# Upper Snake Case
# -------------------------------------------------#
upper_snake_case = cc.make_upper_snake_case(input)
print(f"Upper snake case: {upper_snake_case}")


# Kebab Case
# -------------------------------------------------#
kebab_case = cc.make_kebab_case(input)
print(f"Kebab case: {kebab_case}")


# Upper Kebab Case
# -------------------------------------------------#
upper_kebab_case = cc.make_upper_kebab_case(input)
print(f"Upper kebab case: {upper_kebab_case}")
