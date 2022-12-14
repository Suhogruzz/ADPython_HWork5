import pathlib
from LoggerWPath import logger_w_path
from Logger import logger


# Генератор возвращающий плоское представление списка списков
@logger
def flat_generator(_list):
    for part in _list:
        for element in part:
            yield element


# Генератор для списков с любым уровнем вложенности
@logger_w_path(pathlib.Path(r'Вставить сюда путь из проводника'))
def flat_generator_any(_list):
    for part in _list:
        if type(part) == list:
            for element in flat_generator_any(part):
                yield element
        else:
            yield part


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    print(list(flat_generator(nested_list)))

    nested_list_any = [[
        ['a', 'b', 'c'],
        ['d', [['e'], 'f', 'h'], False],
        [1, 2, None],
        [[[['ttt']]]]
    ]]
    print(list(flat_generator_any(nested_list_any)))