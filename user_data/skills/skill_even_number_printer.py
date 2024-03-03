# filename: even_number_printer.py
from pydantic import BaseModel

class EvenNumberPrinter(BaseModel):
    @classmethod
    def print_even_numbers(cls):
        for number in range(1, 26):
            if number % 2 == 0:
                print(number)

if __name__ == "__main__":
    EvenNumberPrinter.print_even_numbers()