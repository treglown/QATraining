# Testing - for errors in code
# Writing tests is a cheaper solution to find errors in prod. 

# Types of testing:
# Function testing:
# unit testing
# Integration Testing
# User Acceptance testing

# Non-Functional Testing:
# Performance testing
# Scalability Testing
# Usability testing
# Maintenance Testing

import pytest
import math

def func(num):
    return num * 2

def test_answer():
    assert func(6) == 12 # This will pass but if the value was 10 it would fail. 

def test_count_integers():
    assert count([1, 2, 3, 4, 5, 5, 5, 9]) == 3
    assert count([-1, 0, 109, 992, 99]) == 1

def test_word_count():
    assert count("Jack", "John", "James")
    assert count("Jack", "jacky", "Joe")





