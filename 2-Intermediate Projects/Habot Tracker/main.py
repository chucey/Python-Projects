import pandas as pd
from tabulate import tabulate
from datetime import datetime
from Habit_tracker import track_habit, Habit

def main():
    habits: list[Habit]= [
        track_habit('Coffee',datetime(2023,6,6,8), cost = 3, minutes_used = 5),
        track_habit('Wasting Time', datetime(2023,5,5,6), cost = 10, minutes_used=60),
        track_habit('Smoking', datetime(2023, 1, 5, 6), cost=8, minutes_used=10)

    ]

    df = pd.DataFrame(habits)
    print(tabulate(df, headers='keys', tablefmt='pqsl'))

if __name__ == '__main__':
    main()
