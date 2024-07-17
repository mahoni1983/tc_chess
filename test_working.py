import sys
import pytest
from working import *


def test_convert1():
    assert convert_two_times('11:31 am to 6:52 pm') == '11:31 to 18:52'


def test_convert2():
    assert convert_two_times('11:31 pm to 6:52 am') == '23:31 to 06:52'


def test_convert3():
    assert convert_two_times('1:31 am to 11:52 pm') == '01:31 to 23:52'


def test_convert4():
    with pytest.raises(ValueError):
        convert_two_times('1:71 am to 11:52 pm')


def test_convert5():
    with pytest.raises(ValueError):
        convert_two_times('1:71 am 11:52 pm')
