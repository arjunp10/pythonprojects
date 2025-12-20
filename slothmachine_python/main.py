import random
rows = 3
cols = 3
symbols = {"A": 2, "B": 4, "C": 6, "D": 8}

def check_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet * 3
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        print()



def deposit():
    while True:
        amount = input("Enter the amount of deposit: ")
        if amount.isdigit() and int(amount) > 0:
            amount = int(amount)
            break
        else:
            print("Invalid amount.")
            continue
    return amount

def number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-3): ")
        if lines.isdigit() and 1 <= int(lines) <= 3:
            lines = int(lines)
            break
        else:
            print("Invalid number of lines.")
            continue
    return lines

def amount_on_each_line(balance, lines):
    
    while True:
        amount = input("Enter the amount to bet on each line: ")
        if amount.isdigit() and int(amount) > 0:
            amount = int(amount)
        else:
            print("Invalid amount.")
            continue
        if (amount*lines) > balance:
            print(f"You do not have enough to bet that amount, your current balance is: {balance}")
            continue
        break
    return amount

def main():
    balance = deposit()
    lines = number_of_lines()
    each_line = amount_on_each_line(balance, lines)
    print(f"You are betting {each_line} on {lines} lines. Total bet is {each_line * lines}")
    slot_machine_result = get_slot_machine_spin(rows, cols, symbols)
    print_slot_machine(slot_machine_result)
    winnings, winning_lines = check_winnings(slot_machine_result, lines, each_line)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)

main()