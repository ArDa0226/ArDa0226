
def tets(a, b=4, *args, **kwargs):
    print('test')
    print('a & b', a, b)
    print('type args: ', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('position params:', i, arg)
    print('type kwargs: ', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('named params: ', key, '=', value)

tets(5,6,7, 8, cat='Myu')
tets(6, b=7, dog='Ah!')
tets(7, cat='Myau!', address='NU')


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1)
    return n * factorial_n_minus_1

print(factorial(9))