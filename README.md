# Python-CamelCaser

Python-CamelCaser is a Python package that provides functionality for finding real-world words in a string and reformatting strings into various standardized notations. It offers different modes to suit your specific formatting needs, including Camel case, Lower camel case, Snake case, Upper snake case, Kebab case, and Upper kebab case.

## Features

- Word Detection: The package includes a word detection mechanism that can identify real-world words within a given string.
- Notation Transformation: Python-CamelCaser allows you to easily transform strings into various standardized notations, such as Camel case, Lower camel case, Snake case, Upper snake case, Kebab case, and Upper kebab case.
- Flexibility: The package provides different modes to cater to a wide range of formatting requirements, allowing you to choose the notation style that best suits your project or coding style.


# Modes
| Case            | Example Input    | Output         |
|-----------------|-----------------|----------------|
| Camel case      | handlingunits   | HandlingUnits  |
| Lower camel case| handlingunits   | handlingUnits  |
| Snake case      | handlingunits   | handling_units |
| Upper snake case| handlingunits   | Handling_Units |
| Kebab case      | handlingunits   | handling-units |
| Upper kebab case| handlingunits   | Handling-Units |


## Usage

### Example
```python
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

```

### Output 

```
Camel case: HandlingUnits
Lower camel case: handlingUnits
Snake case: handling_units
Upper snake case: Handling_Units
Kebab case: handling-units
Upper kebab case: Handling-Units
```

# Contributions

https://github.com/dwyl/english-words


