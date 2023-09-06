from enum import Enum
from typing import Dict, List, Literal, Optional, Union

from types2json import AttributeType

"""
A dummy test object
"""


class Object(object):
    def __eq__(self, other):
        if isinstance(other, Object):
            return True
        return False

    def __hash__(self):
        return 42


"""
A nested Enum Class
"""


class NestedEnum(Enum):
    NESTED = "NESTED"
    TYPE = AttributeType


"""
A dummy test class for all currently supported types
both with/without default values
"""


class ClassAll:
    def __init__(
        self,
        str: str,
        int: int,
        flt: float,
        bool: bool,
        obj: dict,
        unknown: Object,
        tup: tuple,
        lst: list,
        union: Union[str, int],
        enum: AttributeType,
        literal: Literal["a", "b"],
        str_val: str = "string",
        int_val: int = 0,
        flt_val: float = 0.0,
        bool_val: bool = True,
        obj_val: Dict = {"dict": "val"},  # noqa: B006
        unknown_val: Object = None,
        tup_val: tuple = (1, "hello"),
        lst_val: List[int] = [1, 2, 3],  # noqa: B006
        union_val: Union[str, int] = "string",
        enum_val: AttributeType = AttributeType.ENUM,
        literal_val: Literal["a", "b"] = "a",
    ) -> None:
        pass


"""
A dummy test class for string parameters
"""


class ClassStr:
    def __init__(
        self,
        name: str,
        text: str = "text",
    ) -> None:
        pass


"""
A dummy class that inherits from another class
"""


class SubClass(ClassStr):
    def __init__(
        self,
        subname: str,
        subtext: str = "subtext",
    ) -> None:
        pass


class SubSubClass(SubClass):
    def __init__(
        self,
        subsubname: str,
        subsubtext: str = "subsubtext",
    ) -> None:
        pass


"""
A dummy test class for nested types
with/without default values
"""


class ClassNested:
    def __init__(
        self,
        tuple: tuple[tuple[int, str], tuple[float, bool]],
        lst: List[List[int]],
        union: Union[int, Union[str, float]],
        dict: Dict[str, Dict[int, float]],
        enum: NestedEnum,
        option: Optional[Optional[int]],
        tuple_val: tuple[tuple[int, str], tuple[float, bool]] = (
            (0, "string"),
            (0.0, False),
        ),
        lst_val: List[List[int]] = [[1, 2, 3], [4, 5, 6]],  # noqa: B006
        union_val: Union[int, Union[str, float]] = "string",
        dict_val: Dict[str, Dict[int, float]] = {"key": {0: 0.0}},  # noqa: B006
        enum_val: NestedEnum = NestedEnum.TYPE.value.STRING,
        option_val: Optional[Optional[int]] = 0,
    ) -> None:
        pass
