# User messages for prompts, errors, and feedback
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

# Calculator memory (stores last result if user chooses to)
memory = 0

# Determines whether a float is a one-digit integer
def is_one_digit(v):
    return v.is_integer() and -10 < v < 10

# Checks for "lazy" patterns and prints appropriate feedback
def check(x, y, oper):
    message = ""
    if is_one_digit(x) and is_one_digit(y):
        message += msg_6  # Both operands are one-digit
    if x == 1 or y == 1:
        message += msg_7  # One of the operands is 1
    if (x == 0 or y == 0) and oper == "*":
        message += msg_8  # Multiplying by zero
    if message:
        print(msg_9 + message)  # Combine prefix with laziness messages

# Core calculator loop
def calculate():
    global memory

    while True:
        print(msg_0)
        calc = input()
        x, oper, y = calc.split()

        # Replace 'M' with memory value
        if x == "M":
            x = memory
        if y == "M":
            y = memory

        # Attempt to convert operands to numbers
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_1)
            continue  # Restart loop if input is invalid

        # Check for supported operators
        if oper not in ("+", "-", "*", "/"):
            print(msg_2)
            continue

        # Evaluate laziness and print messages if applicable
        check(x, y, oper)

        # Check for division by zero
        if oper == "/" and y == 0:
            print(msg_3)
            continue

        # Perform the requested operation
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif oper == "/":
            result = x / y

        # Output the result
        print(result)

        # Prompt to store result in memory
        print(msg_4)
        answer = input()
        if answer == "y":
            # If result is a one-digit integer, ask for multiple confirmations
            if is_one_digit(result):
                msg_index = 10
                while msg_index < 13:
                    m = 'msg_' + str(msg_index)
                    print(globals()[m])  # Dynamically access message by name
                    answer = input()
                    if answer == "y":
                        msg_index += 1
                    else:
                        break
                else:
                    memory = result  # Store result only if all confirmations were "y"
            else:
                memory = result  # Store directly if not a one-digit integer

        # Prompt to continue or exit the calculator
        print(msg_5)
        answer = input()
        if answer == "y":
            continue
        else:
            break

# Start the calculator
calculate()
