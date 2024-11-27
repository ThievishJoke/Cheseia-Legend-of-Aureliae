import random
import time
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def roll_dice_animation(sides=6, rolls=10, base_speed=0.1, increment=0.5):
    """
    Simulates an animated dice roll with speed adjustments and a suspenseful pause before the final roll.

    Args:
        sides (int): The number of sides on the dice.
        rolls (int): The number of rolls in the animation.
        base_speed (float): The initial delay between rolls, in seconds.
        increment (float): The additional delay added every 5 rolls and before the final roll.
    """
    clear_screen()
    print("Rolling the dice...")
    current_speed = base_speed

    for i in range(1, rolls):
        number = random.randint(1, sides)
        clear_screen()
        print(f"Rolling... {number}")
        time.sleep(current_speed)

        # Increase speed every 5 rolls
        if i % 5 == 0:
            current_speed += increment

    # Add suspense before the final roll
    time.sleep(current_speed + increment)
    clear_screen()
    final_roll = random.randint(1, sides)
    print(f"Final roll: {final_roll}")

# Example usage
if __name__ == "__main__":
    sides = int(input("Enter the number of sides on the dice (e.g., 6 for a d6): "))
    rolls = int(input("Enter the number of animation rolls (before suspenseful final roll): "))
    base_speed = float(input("Enter the base speed of animation (in seconds): "))
    increment = float(input("Enter the speed increment every 5 rolls (and before the final roll, in seconds): "))
    roll_dice_animation(sides=sides, rolls=rolls, base_speed=base_speed, increment=increment)

# 20
# 16
# .125
# .125

#can increment the max dice roll with upgrades