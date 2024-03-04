class OddNumbersPrinter:
    """
    A class to print all odd numbers from 1 to 100.
    """
    
    def print_odd_numbers(self):
        """
        Prints all odd numbers from 1 to 100.
        """
        for number in range(1, 101):
            if number % 2 != 0:
                print(number)

# Create an instance of OddNumbersPrinter
printer = OddNumbersPrinter()

# Call the method to print odd numbers
printer.print_odd_numbers()