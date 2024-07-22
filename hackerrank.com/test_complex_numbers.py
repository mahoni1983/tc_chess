from complex_numbers import Complex


def test_add1():
    assert Complex(2, 1) + Complex(5, 6) == Complex(7, 7)


def test_add2():
    assert Complex(2, 1) + Complex(5, -6) == Complex(7, -5)


def test_add3():
    assert Complex(-2, 1) + Complex(5, -6) == Complex(3, -5)


def test_sub1():
    assert Complex(2, 1) - Complex(5, 6) == Complex(-3, -5)


def test_sub2():
    assert Complex(2, 1) - Complex(5, -6) == Complex(-3, 7)


def test_sub3():
    assert Complex(-2, 1) - Complex(5, -6) == Complex(-7, 7)


def test_mult1():
    assert Complex(2, 1) * Complex(5, 6) == Complex(4, 17)


def test_mult2():
    assert Complex(2, 1) * Complex(5, -6) == Complex(16, -7)


def test_mult3():
    assert Complex(-2, 1) * Complex(5, -6) == Complex(-4, 17)


def test_division1():
    assert Complex(2, 1) / Complex(5, 6) == Complex(16/61, -7/61)


def test_division2():
    assert Complex(2, 1) / Complex(5, -6) == Complex(4/61, 17/61)


def test_mod1():
    assert Complex(2, 1).mod() == 5**0.5

