from enum import Enum


class Symbols(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"


class TokenTypes(Enum):
    NUMBER = 1
    SYMBOL = 2
    OPEN_BRACKET = 3
    CLOSE_BRACKET = 4

SYMBOL_PRIORITY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}



class Expression:
    def evaluate(self):
        raise NotImplementedError("Метод не реализован")


class Value(Exception):
    def __init__(self, value: int = 0):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    def evaluate(self):
        return self.value


class Instance(Exception):
    def __init__(self, left_value: Expression, right_value: Expression, symbol: Expression):
        self.__left_value = left_value
        self.__right_value = right_value
        self.__symbol = symbol

    @property
    def left_value(self):
        return self.__left_value

    @left_value.setter
    def left_value(self, value: Expression):
        self.__left_value = value

    @property
    def right_value(self):
        return self.__right_value

    @right_value.setter
    def right_value(self, value: Expression):
        self.__right_value = value

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, value: Expression):
        self.__symbol = value

    def evaluate(self):
        if self.left_value is None or self.right_value is None or self.symbol is None:
            raise AttributeError("Не указан один из атрибутов выражения")

        if self.symbol == Symbols.ADD.value:
            return self.left_value.evaluate() + self.right_value.evaluate()
        elif self.symbol == Symbols.SUB.value:
            return self.left_value.evaluate() - self.right_value.evaluate()
        elif self.symbol == Symbols.MUL.value:
            return self.left_value.evaluate() * self.right_value.evaluate()
        elif self.symbol == Symbols.DIV.value:
            right_value = self.right_value.evaluate()
            if right_value == 0:
                raise ArithmeticError("Деление на 0")
            return self.left_value.evaluate() / right_value


class Token:
    def __init__(self, token_type: TokenTypes, value: str):
        self.__type = token_type
        self.__value = value

    @property
    def token_type(self):
        return self.__type

    @token_type.setter
    def token_type(self, t_type):
        self.__type = t_type

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


def process_token_array(tokens: list[:Token]) -> Expression:
    res = Expression()
    while len(tokens) > 0:
        token = tokens.pop(0)
        if token.value == TokenTypes.OPEN_BRACKET:
            return process_token_array(tokens)
        elif token.value == TokenTypes.CLOSE_BRACKET:
            return res
        elif token.value == TokenTypes.NUMBER:
            pass

    return res
