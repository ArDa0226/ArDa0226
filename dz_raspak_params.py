#Функция с параметрами
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()

print_params(b=25)
print_params(c=[1,2,3])

#Распаковка параметров
values_list = [1, 'a', {'art':123}]
values_dict = {'a': 123, 'b':[345], 'c': 'scare'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [[1,2,3],('qwe')]
print_params(*values_list_2, 42)
