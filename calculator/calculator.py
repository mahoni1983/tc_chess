"""
https://intra.turingcollege.com/hardskills/calculator
The main file should contain a class Calculator that can perform the following actions:

Addition / Subtraction.
Multiplication / Division.
Take (n) root of a number.
Reset memory. This means the calculator should perform actions using the value stored in its memory, with memory
starting at 0. For example, if the first operation performed is calculator.add(2), the result is 2. If calculator.add(2)
 is performed again, the result is 4. At this point the value stored in memory is 4. If the calculator memory is then
 reset, the value stored in memory returns to 0.
Writing tests and documentation
You should also write tests to ensure the basic functionality of the class is working correctly and that math
operations return the expected results. Document your calculator class using docstrings. Add an explanation of the
package to the README file. Try to be as specific as possible: include instructions on how to install the package and
how to use particular methods.
Present your newly created Python module:

Make a short introduction to the Calculator repository module.
Import your module into a Jupyter Notebook file.
Demonstrate the functionality of the module.
Project evaluation criteria
Calculator module has been created.
Calculator class performs the required actions.
Tests are written.
Code is written with PEP8 standards in mind.
Code is well-documented.
Project has an informative README file.
"""


def decorator(func):
    """
    Decorates a function: prints a result of the chosen method with mentioning the action itself if
    Calculator's print_result_after_each_action flag is True.
    Also prints a corresponding error (e.g. in case of division by zero).
    :param func: a function to decorate.
    :return: decorated specified function.
    """
    function_actions = {'add': 'adding', 'sub': 'subtracting', 'mul': 'multiplication', 'div': 'division',
                        'root_n': 'taking the root of power of n'}

    def function_wrapper(self, x):
        try:
            func(self, x)
            if self.print_result_after_each_action:
                action = function_actions[func.__name__] if func.__name__ in function_actions.keys() else func.__name__
                print("Result after " + action + f': {str(self.mem)}')
        except ZeroDivisionError:
            print('Error. Division by zero can not be performed.')
        except TypeError:
            print('Error. Only numbers can be input.')
        except ValueError:
            print('Error. Even power root of a negative number can not be calculated in real numbers.')
        except Exception as e:
            print(f'Error. Unknown error occurred:\n{e}')
    return function_wrapper


class Calculator:
    """
    Calculator that can perform a few math actions with stored value.
    Initial value is 0. A chosen action changes the value with specified value.
    Stored value can be reset to 0.
    For example, if the first operation performed is calculator.add(2), the result is 2. If calculator.add(2)
    is performed again, the result is 4. At this point the value stored in memory is 4. If the calculator memory is then
    reset, the value stored in memory returns to 0.
    :param
    print_result_after_each_action=True - flag determines whether to print or not result after each action.
    """
    mem = 0
    print_result_after_each_action = True

    def __init__(self, print_result_after_each_action=True):
        self.print_result_after_each_action = print_result_after_each_action

    def __str__(self):
        return str(self.mem)

    @decorator
    def add(self, number: float) -> float:
        """
        Add a number to the value stored in memory.
        :param number: a number to be added to the value stored in memory.
        :return: result of adding a number to the value stored in memory.
        """
        self.mem += number
        return self.mem

    @decorator
    def sub(self, number: float) -> float:
        """
        Subtract a number from the value stored in memory.
        :param number: a number to be subtracted from the value stored in memory.
        :return: result of subtracting a number from the value stored in memory.
        """
        self.mem += -number
        return self.mem

    @decorator
    def mult(self, number: float) -> float:
        """
        Multiplies the value stored in memory by the specified number.
        :param number: a number to multiply the value stored in memory by.
        :return: result of multiplication of the value stored in memory by the specified number.
        """
        self.mem = self.mem * number
        return self.mem

    @decorator
    def div(self, number: float) -> float:
        """
        Divides the value stored in memory by the specified number.
        :param number: a number to divide the value stored in memory by.
        :return: result of division of the value stored in memory by the specified number.
        """
        self.mem = self.mem / number
        return self.mem

    @decorator
    def root_n(self, number: float) -> float:
        """
        Takes the root of specified power of the value stored in memory.
        :param number: a power of the root to take.
        :return: result of taking the root of specified power of the value stored in memory.
        """
        if self.mem < 0 and number % 2 == 0:
            raise ValueError('Even power root of a negative number.')
        self.mem = self.mem ** (1 / number)
        return self.mem

    def reset(self):
        """
        Resets the value stored in memory to 0.
        """
        self.mem = 0

    def current_value(self):
        """
        Returns the currently store in memory value.
        :return: the currently store in memory value
        """
        return self.mem


def main():
    calc = Calculator(True)
    calc.add(2)
    calc.add('sdf')
    calc.mult(3)
    calc.root_n(0)
    calc.div(7)
    calc.div(0)
    calc.reset()
    calc.sub(2)
    calc.root_n(2)
    print(calc.current_value())


if __name__ == '__main__':
    main()
