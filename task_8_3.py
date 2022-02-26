from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrap(*args, **kwargs):
        arg_str = ', '.join(f'{str(i)} - {type(i)}' for i in args)
        karg_str = ', '.join(f'{str(i)}: {str(v)} - {type(v)}' for i, v in kwargs.items())
        print(f'{func.__name__}({arg_str})')
        print(f'{func.__name__}({karg_str})')
        return func(*args, **kwargs)

    return wrap


@type_logger
def calc_cube(x, *args, **kwargs):
    return x ** 3


a = calc_cube(5, 6, k='l', m='n')
# 5: <class 'int'>

a = calc_cube(5)
# calc_cube(5: <class 'int'>)