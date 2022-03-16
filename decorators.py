def my_dec(func):
    def wrapper(*args, **kwargs):
        print('öncesi işler')

        for key, value in kwargs.items():
            if key == 'message':
                kwargs[key] = str(value).upper()
        

        return_val = func(*args, **kwargs)

        if type(return_val) == str:
            return return_val.upper()

        print('sonrası işler')
        return return_val
    return wrapper

@my_dec
def sample(a, b, end):
    print('Merhabalar!', a, b)
    return 'Naber?'


@my_dec
def samp2(message):
    print('sample fonksiyon 2', message)
    return 2

print(sample(15, 50, end=' '))
print(samp2(message='Deneme'))