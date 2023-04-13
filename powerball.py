
import random

def choose_numbers():
    numbers = []
    for _ in range(5):
        number = int(input(f"Choose a number between 1 and 69 (inclusive) for position {_ + 1}: "))
        while number < 1 or number > 69 or number in numbers:
            number = int(input(f"Invalid input. Choose a different number between 1 and 69 (inclusive) for position {_ + 1}: "))
        numbers.append(number)
    
    power_number = int(input("Choose a Power Number between 1 and 26 (inclusive): "))
    while power_number < 1 or power_number > 26:
        power_number = int(input("Invalid input. Choose a different Power Number between 1 and 26 (inclusive): "))
    
    return numbers, power_number

def quick_pick(num_of_plays):
    quick_picks = []
    for _ in range(num_of_plays):
        numbers = random.sample(range(1, 70), 5)
        power_number = random.randint(1, 26)
        quick_picks.append((numbers, power_number))
    return quick_picks

def check_prize(numbers, power_number, winning_numbers, winning_power_number):
    if numbers == winning_numbers and power_number == winning_power_number:
        return "You won the jackpot!"
    return "You didn't win the jackpot."

def main():
    print("Welcome to Powerball!")
    user_choice = input("Enter 'Q' for Quick Pick or 'C' to choose your own numbers: ").upper()
    while user_choice not in ('Q', 'C'):
        user_choice = input("Invalid input. Enter 'Q' for Quick Pick or 'C' to choose your own numbers: ").upper()
    
    if user_choice == 'Q':
        num_of_plays = int(input("How many Quick Pick plays would you like (up to 10)? "))
        while num_of_plays < 1 or num_of_plays > 10:
            num_of_plays = int(input("Invalid input. Enter a number between 1 and 10: "))
        quick_picks = quick_pick(num_of_plays)
        for i, (numbers, power_number) in enumerate(quick_picks, 1):
            print(f"Play {i}: Your numbers are: {numbers} and Power Number: {power_number}")
    else:
        numbers, power_number = choose_numbers()
        print(f"Your numbers are: {numbers} and Power Number: {power_number}")

    # Example winning numbers (replace with actual draw results)
    winning_numbers = [1, 2, 3, 4, 5]
    winning_power_number = 6

    if user_choice == 'Q':
        for i, (numbers, power_number) in enumerate(quick_picks, 1):
            result = check_prize(numbers, power_number, winning_numbers, winning_power_number)
            print(f"Play {i} result: {result}")
    else:
        result = check_prize(numbers, power_number, winning_numbers, winning_power_number)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
