# Python-CamelCaser

Python-CamelCaser is a Python package that provides functionality for finding real-world words in a string and reformatting strings into various standardized notations. It offers different modes to suit your specific formatting needs, including Camel case, Lower camel case, Snake case, Upper snake case, Kebab case, and Upper kebab case.

## Features

- Word Detection: The package includes a word detection mechanism that can identify real-world words within a given string.
- Notation Transformation: Python-CamelCaser allows you to easily transform strings into various standardized notations, such as Camel case, Lower camel case, Snake case, Upper snake case, Kebab case, and Upper kebab case.
- Flexibility: The package provides different modes to cater to a wide range of formatting requirements, allowing you to choose the notation style that best suits your project or coding style.


# Modes
| Mode               | Input                 | Output                |
|--------------------|-----------------------|-----------------------|
| camel_case         | verylongtestexample   | VeryLongTestExample   |
| lower_camel_case   | verylongtestexample   | veryLongTestExample   |
| snake_case         | verylongtestexample   | very_long_test_example |
| upper_snake_case   | verylongtestexample   | Very_Long_Test_Example |
| kebab_case         | verylongtestexample   | very-long-test-example |
| upper_kebab_case   | verylongtestexample   | Very-Long-Test-Example |



## Usage

### Import
```python
import camelcaser as cc
```

### Usage with real world words without separators
```python
input_word = "verylongtestexample"

# Camel case
camel_case = cc.make_camel_case(input_word)
print(f"Camel case: {camel_case}")

# Snake case
snake_case = cc.make_snake_case(input_word)
print(f"Snake case: {snake_case}")
```

### Usage with separators
```python
input_word =  "very_long_test_example"

# Camel Case
camel_case = cc.make_camel_case(input_word)

# Snake Case
snake_case = cc.make_snake_case(input_word)
```

### Usage with custom separator [;]
```python
input_word = "Very;Long;Test;Example"

# Camel Case
camel_case = cc.make_camel_case(input_word, separator=separator)

# Snake Case
snake_case = cc.make_snake_case(input_word, separator=separator)
```



## Examples

### Examples with real world words without separators
| Mode             | Input                  | Output                 |
|------------------|------------------------|------------------------|
| camel_case       | verylongtestexample     | VeryLongTestExample    |
| lower_camel_case | verylongtestexample     | veryLongTestExample    |
| snake_case       | verylongtestexample     | very_long_test_example |
| upper_snake_case | verylongtestexample     | Very_Long_Test_Example |
| kebab_case       | verylongtestexample     | very-long-test-example |
| upper_kebab_case | verylongtestexample     | Very-Long-Test-Example |


### Examples with separators
| Mode             | Input                  | Output                 |
|------------------|------------------------|------------------------|
| camel_case       | very_long_test_example | VeryLongTestExample    |
| lower_camel_case | very_long_test_example | veryLongTestExample    |
| lower_snake_case | very_long_test_example | very_long_test_example |
| upper_snake_case | very_long_test_example | Very_Long_Test_Example |
| kebab_case       | very_long_test_example | very-long-test-example |
| upper_kebab_case | very_long_test_example | Very-Long-Test-Example |
| camel_case       | very-long-test-example  | VeryLongTestExample    |
| lower_camel_case | very-long-test-example  | veryLongTestExample    |
| lower_snake_case | very-long-test-example  | very_long_test_example |
| upper_snake_case | very-long-test-example  | Very_Long_Test_Example |
| kebab_case       | very-long-test-example  | very-long-test-example |
| upper_kebab_case | very-long-test-example  | Very-Long-Test-Example |
| camel_case       | VeryLongTestExample     | Verylongtestexample    |
| lower_camel_case | VeryLongTestExample     | verylongtestexample    |
| lower_snake_case | VeryLongTestExample     | Verylongtestexample    |
| upper_snake_case | VeryLongTestExample     | Verylongtestexample    |
| kebab_case       | VeryLongTestExample     | Verylongtestexample    |
| upper_kebab_case | VeryLongTestExample     | Verylongtestexample    |
| camel_case       | veryLongTestExample     | Verylongtestexample    |
| lower_camel_case | veryLongTestExample     | verylongtestexample    |
| lower_snake_case | veryLongTestExample     | Verylongtestexample    |
| upper_snake_case | veryLongTestExample     | Verylongtestexample    |
| kebab_case       | veryLongTestExample     | Verylongtestexample    |
| upper_kebab_case | veryLongTestExample     | Verylongtestexample    |


### Examples with custom separator [;]
| Mode             | Input                  | Output                 |
|------------------|------------------------|------------------------|
| camel_case       | very;long;test;example | VeryLongTestExample    |
| lower_camel_case | very;long;test;example | veryLongTestExample    |
| lower_snake_case | very;long;test;example | very_long_test_example |
| upper_snake_case | very;long;test;example | Very_Long_Test_Example |
| kebab_case       | very;long;test;example | very-long-test-example |
| upper_kebab_case | very;long;test;example | Very-Long-Test-Example |
| camel_case       | Very;Long;Test;Example | VeryLongTestExample    |
| lower_camel_case | Very;Long;Test;Example | veryLongTestExample   



# Thank you

https://github.com/dwyl/english-words


