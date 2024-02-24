import re


def repeat_element(input_str):
    """
    Возвращает строку с повторяющимися элементами,
    разделёнными запятыми, на основе входной строки
    формата 'элемент*количество'.
    A*3   ->   A,A,A
    """
    element, count = input_str.split('*')
    count = int(count)  # Преобразуем количество в число
    return ','.join([element] * count)


def expand_range(range_str):
    """
    Возвращает строку с указанным диапазоном и шагом,
    разделёнными запятыми, на основе входной строки
    формата 'первое_число-последнее_число'
    или 'первое_число-последнее_число-шаг'.
    3-7   ->   3,4,5,6,7
    1-10-3   ->   1,4,7,10
    """
    parts = list(map(int, range_str.split('-')))
    if len(parts) == 2:
        start, end = parts
        step = 1
    elif len(parts) == 3:
        start, end, step = parts
    else:
        raise ValueError("Неверный формат диапазона")
    return ','.join(str(x) for x in range(start, end + 1, step))


def replace_repeats_and_ranges(input_string):
    """Находит и заменяет выражения в формате 'элемент*количество'
    и диапазоны в заданной строке."""

    def replacer(match):
        text = match.group(0)
        if '*' in text:
            return repeat_element(text)
        elif '-' in text:
            return expand_range(text)
        return text

    pattern = r'(\b[A-Za-z]*\d*[\*\-]\d+([\-]\d+)?\b)'
    result = re.sub(pattern, replacer, input_string)
    return result


def has_element_before_bracket(input_str):
    """Определяет, содержит ли строка выражение со скобкой, где перед скобкой есть элемент."""
    pattern = r'[A-Za-z]+\([^)]+\)'
    return bool(re.search(pattern, input_str))


def expand_before_bracket(input_str):
    """Обрабатывает выражения, где элемент находится перед скобкой."""
    def expand(match):
        before = match.group(1)
        in_brackets = match.group(2).split(',')
        return ','.join(f"{before}{item}" for item in in_brackets)

    pattern = r'([A-Za-z]+)\(([^)]+)\)'
    return re.sub(pattern, expand, input_str)


def has_element_after_bracket(input_str):
    """Определяет, содержит ли строка выражение со скобкой, где после скобки есть элемент."""
    pattern = r'\([^)]+\)[A-Za-z0-9]+'
    return bool(re.search(pattern, input_str))


def expand_after_bracket(input_str):
    """Обрабатывает выражения, где элемент находится после скобки."""
    def expand(match):
        in_brackets = match.group(1).split(',')
        after = match.group(2)
        return ','.join(f"{item}{after}" for item in in_brackets)

    pattern = r'\(([^)]+)\)([A-Za-z0-9]+)'
    return re.sub(pattern, expand, input_str)


def expand_brackets(input_str):
    while has_element_before_bracket(input_str):
        input_str = expand_before_bracket(input_str)

    while has_element_after_bracket(input_str):
        input_str = expand_after_bracket(input_str)

    return input_str


def expand(input_str):
    input_str = input_str.replace(' ', '')
    input_str = replace_repeats_and_ranges(input_str)
    input_str = expand_brackets(input_str)
    return input_str


test_strs = [
    'A(2-5)',
    'B1*4',
    'B(2-5)'
]

for test_str in test_strs:
    print(f'{expand(test_str)}')

