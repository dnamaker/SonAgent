# filename: number_printer.py
from pydantic import BaseModel

class NumberPrinter(BaseModel):
    def print_numbers(self):
        for number in range(1, 26):
            print(number)

if __name__ == "__main__":
    printer = NumberPrinter()
    printer.print_numbers()