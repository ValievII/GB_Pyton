from functools import wraps


def check_arg(*argv):
    if len(argv) != 1:
        msg = f'wrong val {argv}'
        raise ValueError(msg)
    if not isinstance(argv[0], int) or argv[0] <= 0:
        msg = f'wrong val {argv[0]}'
        raise ValueError(msg)


def val_checker(func):
    def _val_checker(main_func):
        @wraps(main_func)
        def wrapper(*args):
            func(*args)
            result = main_func(*args)
            return result
        return wrapper
    return _val_checker


@val_checker(check_arg)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))