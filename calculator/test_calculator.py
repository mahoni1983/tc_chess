import pytest

from calculator import *


def test_init_value_is_zero():
    calc = Calculator()
    assert calc.current_value() == 0


def test_add1():
    calc = Calculator()
    calc.add(2)
    assert calc.current_value() == 2


def test_add2():
    calc = Calculator()
    calc.add(2)
    calc.add(3)
    assert calc.current_value() == 5


def test_sub1():
    calc = Calculator()
    calc.sub(2)
    assert calc.current_value() == -2


def test_sub2():
    calc = Calculator()
    calc.sub(2)
    calc.sub(3)
    assert calc.current_value() == -5


def test_mult1():
    calc = Calculator()
    calc.mult(2)
    assert calc.current_value() == 0


def test_mult2():
    calc = Calculator()
    calc.add(1)
    calc.mult(-3)
    assert calc.current_value() == -3


def test_div1():
    calc = Calculator()
    calc.div(2)
    assert calc.current_value() == 0


def test_div2():
    calc = Calculator()
    calc.add(1)
    calc.div(2)
    assert calc.current_value() == 0.5


def test_root1():
    calc = Calculator()
    calc.add(8)
    calc.root_n(3)
    assert calc.current_value() == 2.0


def test_root2():
    calc = Calculator()
    calc.add(8)
    calc.root_n(-3)
    assert calc.current_value() == 0.5


def test_root3():
    calc = Calculator()
    calc.sub(8)
    calc.root_n(2)
    # the value has not been changed as square root of a negative number can not be calculated in real numbers
    assert calc.current_value() == -8


def test_reset():
    calc = Calculator()
    calc.sub(8)
    assert calc.current_value() == -8
    calc.reset()
    assert calc.current_value() == 0

