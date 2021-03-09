import pandas as pd


def create_series(foods, calories):
    return pd.Series(calories, index=foods, name='Calorie content')
