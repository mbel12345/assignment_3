from app.operations import Operations

class Calculator:

    @staticmethod
    def run():

        print('Welcome to the REPL calculator!')

        # Keep prompting the user for calculations until they type 'exit'
        while True:

            user_input = input('Enter an operation (add, subtract, multiply, divide), followed by two numbers. Enter "exit" to quit: ').strip().lower()

            if user_input == 'exit':
                print('exiting calculator')
                break

            try:

                # Extract the parts of the user input (operation and 2 numbers)
                parts = user_input.split()
                if len(parts) != 3:
                    print('Invalid input. Please follow the format: <operation> <number> <number>')
                    continue
                operation = parts[0]
                num_1 = float(parts[1])
                num_2 = float(parts[2])

                # Do the operation
                if operation == 'add':
                    result = Operations.addition(num_1, num_2)
                elif operation == 'subtract':
                    result = Operations.subtraction(num_1, num_2)
                elif operation == 'multiply':
                    result = Operations.multiplication(num_1, num_2)
                elif operation == 'divide':
                    try:
                        result = Operations.division(num_1, num_2)
                    except ValueError as e:
                        print(e)
                        continue
                else:
                    print('Unknown operation: Please enter: add, subtract, multiply, or divide')
                    continue

            except Exception as e:
                print('Invalid input. Please follow the format: <operation> <number> <number>')
                continue

            print(f'Result: {result}')
