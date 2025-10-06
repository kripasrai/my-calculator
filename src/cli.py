import sys
import click
from .calculator import add, subtract, multiply, divide, power, square_root

def format_result(result):
    if isinstance(result, float) and result.is_integer():
        return str(int(result))
    return str(result)

@click.command()
@click.argument('operation')
@click.argument('num1', type=float)
@click.argument('num2', type=float, required=False)
def calculate(operation, num1, num2=None):
    try:
        if operation == "add":
            if num2 is None:
                raise ValueError("Addition requires two numbers")
            result = add(num1, num2)
        elif operation == "subtract":
            if num2 is None:
                raise ValueError("Subtraction requires two numbers")
            result = subtract(num1, num2)
        elif operation == "multiply":
            if num2 is None:
                raise ValueError("Multiplication requires two numbers")
            result = multiply(num1, num2)
        elif operation == "divide":
            if num2 is None:
                raise ValueError("Division requires two numbers")
            result = divide(num1, num2)
        elif operation == "power":
            if num2 is None:
                raise ValueError("Power requires two numbers")
            result = power(num1, num2)
        elif operation in ["square_root", "sqrt"]:
            result = square_root(num1)
        else:
            click.echo("Unknown operation")
            sys.exit(1)

        click.echo(format_result(result))

    except ValueError as e:
        click.echo(e)
        sys.exit(1)
    except ZeroDivisionError:
        click.echo("Cannot divide by zero")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    calculate()
