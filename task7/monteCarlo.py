import random
import pandas as pd


def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1

    probabilities = {sum_: (count / num_rolls) * 100 for sum_, count in sums_count.items()}
    return probabilities


def display_probabilities_table(probabilities):
    df = pd.DataFrame(list(probabilities.items()), columns=['Сума чисел на кубиках', 'Ймовірність (%)'])
    print(df)


# Виконання симуляції
num_rolls = 100000
probabilities = simulate_dice_rolls(num_rolls)

# Відображення результатів
display_probabilities_table(probabilities)
