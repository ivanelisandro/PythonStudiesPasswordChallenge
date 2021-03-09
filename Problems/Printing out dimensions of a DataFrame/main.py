import pandas as pd


def print_dim(df: pd.DataFrame):
    size = df.shape
    print(f'This DataFrame contains {size[0]} rows and {size[1]} columns')
