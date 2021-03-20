def tagged(func):
    def wrapper(func_args):
        return f"<title>{func(func_args)}</title>"

    return wrapper
