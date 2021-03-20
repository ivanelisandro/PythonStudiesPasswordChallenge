def morning(func):
    def wrapper(func_args):
        func(func_args)
        print(f"Good morning, {func_args}")

    return wrapper
