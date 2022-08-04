from datetime import datetime


def logger(some_func):
    def logger_funcs(*args, **kwargs):
        time = datetime.now().strftime('%Y-%m-%d | %H:%M:%S')
        name = some_func.__name__
        result = some_func(*args, **kwargs)
        with open('logs.txt', 'a', encoding='utf-8') as logs:
            logs.write(f'\nВремя вызова функции: {time}\n'
                       f'Название функции: {name}\n'
                       f'Аргументы функции: {args, kwargs}\n'
                       f'Функция вернула значение: {result}\n'
                       )
        return result
    return logger_funcs
