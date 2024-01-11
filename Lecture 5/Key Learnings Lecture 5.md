# Python Programming: Packages and Personal Libraries

This transcript captures a lecture on Python programming, focusing on the use of packages and the creation of personal libraries. The speaker begins by discussing the 'cowsay' package, which generates ASCII art, and uses it as an example to illustrate the concept of packages. The conversation then transitions to the creation of personal libraries, highlighting the benefits of bundling frequently used code into a Python module or package. The speaker demonstrates this by creating a 'sayings.py' module with two functions, 'hello' and 'goodbye'. The speaker then shows how to use these functions in another program, and addresses a common issue where the main function in a module is called whenever the module is imported. The speaker resolves this by introducing Python's `__name__` variable and demonstrating its use. The lecture concludes with a demonstration of the corrected 'sayings' module, where the 'goodbye' function is imported into a new program and used to print a farewell message.

# Key Learnings

## Cowsay Package
The cowsay package is capable of generating ASCII art of various animals, including cows and Tyrannosaurus rex. However, it's not commonly used in real-world applications and serves as an example of the types of packages that can be installed.

## Creating Own Libraries
Python allows you to create your own libraries. This is useful when you find yourself implementing the same functions repeatedly or copying and pasting code from old programs into new ones. You can bundle up this frequently used code into a Python module or package, which can be kept locally or shared with others through platforms like PyPI.

## Creating a Sayings Module
The speaker creates a new Python module called "sayings.py". This module contains two functions, `hello` and `goodbye`, both of which take a name as input and print a greeting or farewell message, respectively. A main function is also defined for testing purposes.

## Using the Sayings Module
The speaker demonstrates how to use the functions from the sayings module in another program. They import the `hello` function from the sayings module into a new program and use it to print a greeting.

## Understanding Python's `__name__` Variable
The speaker encounters an issue where the main function in the sayings module is called whenever the module is imported. They explain that this is due to the unconditional call to main at the end of the module. To resolve this, they introduce Python's `__name__` variable and demonstrate how to use it to prevent the main function from being called when the module is imported.

## Final Demonstration
The speaker concludes by demonstrating the corrected sayings module. They import the `goodbye` function into a new program and use it to print a farewell message. This serves as a practical demonstration of creating and using a personal Python module.


System Documentation
- docs.python.org/3/library/sys.html
- pypi.org
- pypi.org/project/cowsay
- pip - package manager for python
- pypi.org/project/requests