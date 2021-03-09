import pandas as pd


def concatenate_data(keyboard_instruments: pd.DataFrame, string_instruments: pd.DataFrame):
    return pd.concat([keyboard_instruments, string_instruments], ignore_index=True)
