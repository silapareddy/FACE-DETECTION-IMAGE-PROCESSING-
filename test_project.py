import pytest
from project import function_1, function_2, function_3, function_4, function_5
import os

def test_function_1():
    assert function_1("photo.jpg") == True
    assert function_1("document.pdf") == False
    assert function_1("image.png") == True
    assert function_1("photo.JPG") == True
    assert function_1("README.txt") == False

def test_function_2():
    assert function_2("cat.jpg") == True
    assert function_2("nonexistent.jpg") == False
    assert function_2("document.pdf") == False

def test_function_3():
    assert function_3("cat.jpg") == True
    assert function_3("noface.jpg") == True
    assert function_3("nonexistent.jpg") == False

def test_function_4():
    files = function_4()
    assert isinstance(files, list)
    for file in files:
        assert function_1(file) == True

def test_function_5():
    assert function_5("cat.jpg") == "grayscale_output.jpg"
    assert os.path.exists("grayscale_output.jpg") == True
    assert function_5("nonexistent.jpg") == False
