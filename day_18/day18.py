import dataclasses
import functools
from math import ceil, floor
import copy
import json
@dataclasses.dataclass
class Number:
    value: int
    nesting: int


def read(number : str) -> list[Number]:
    depth = -1
    num = []
    for char in number:
        match char:
            case '[':
                depth += 1
            case ']':
                depth -= 1
            case ',' | '\n' | ' ' | '"':
                pass
            case n:
                num.append(Number(int(n), depth))
    return num

def is_full(ls):
    if isinstance(ls, list):
        if isinstance(ls[0], Number):
            ls = turn_to_list(ls)
        return len(ls) == 2 and all(is_full(value) for value in ls)
    return isinstance(ls, int)

def place_cursor(depth, ls: list):
    cursor = ls
    for _ in range(depth):
        if len(cursor) == 0 or is_full(cursor[-1]):
            cursor.append([])
        cursor = cursor[-1]
    return cursor

def turn_to_list(number : list[Number]):
    ls = []
    cursor = ls
    for num in number:
        cursor = place_cursor(num.nesting, ls)
        cursor.append(num.value)
    return ls

def split(index, number: list[Number]) -> list[Number]:
    number_c = copy.deepcopy(number)
    num = number_c.pop(index)
    number_c.insert(index, Number(ceil(num.value / 2), num.nesting + 1))
    number_c.insert(index, Number(floor(num.value / 2), num.nesting + 1))
    return number_c

def exploded(index, number: list[Number]) -> list[Number]:
    number_c = copy.deepcopy(number)
    if index != len(number) - 2:
        number_c[index + 2] = Number(number[index + 2].value + number[index + 1].value, number[index + 2].nesting)
    if index != 0:
        number_c[index - 1] = Number(number[index - 1].value + number[index].value, number[index - 1].nesting)

    number_c[index] = Number(0, number[index].nesting - 1)
    del number_c[index + 1]
    return number_c

def reduce(number: list[Number]) -> list[Number]:
    assert is_full(number), f"{turn_to_list(number)} not full"
    for index, value in enumerate(number):
        if value.nesting > 3 and number[index + 1].nesting == value.nesting:
            return reduce(exploded(index, number))
        if value.value > 9:
            return reduce(split(index, number))
    return copy.deepcopy(number)

def value(ls):
    if isinstance(ls, int):
        return ls
    return 3 * value(ls[0]) + 2 * value(ls[1])

if __name__ == '__main__':
    with open('example.in') as f:
        total = json.loads(
            functools.reduce(
                lambda a, b: json.dumps(turn_to_list(reduce(read(json.dumps([json.loads(a), json.loads(b)]))))),
                f
            )
        )
    print(total)
    print(value(total))
