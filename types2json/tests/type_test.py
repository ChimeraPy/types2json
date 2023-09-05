from enum import Enum
from typing import Dict, List, Literal, Optional, Union

from types2json.main import AttributeMeta, AttributeType, get_class_init_params

"""
A dummy test object
"""


class TestObject(object):
    def __eq__(self, other):
        if isinstance(other, TestObject):
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


class TestClassAll:
    def __init__(
        self,
        str: str,
        int: int,
        flt: float,
        bool: bool,
        obj: dict,
        unknown: TestObject,
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
        unknown_val: TestObject = None,
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


class TestClassStr:
    def __init__(
        self,
        name: str,
        text: str = "text",
    ) -> None:
        pass


"""
A dummy class that inherits from another class
"""


class TestSubClass(TestClassStr):
    def __init__(
        self,
        subname: str,
        subtext: str = "subtext",
    ) -> None:
        pass


class TestSubSubClass(TestSubClass):
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


class TestClassNested:
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


"""
Simple test with dummy test classes
Hardcoded the expected result
"""


def test_all_cls():
    # String with and without default value
    str_param = get_class_init_params(TestClassStr)
    str_param_asr = {
        "name": AttributeMeta(
            name="name",
            value=None,
            type=AttributeType.STRING,
            choices=[],
            required=True,
        ),
        "text": AttributeMeta(
            name="text",
            value="text",
            type=AttributeType.STRING,
            choices=[],
            required=False,
        ),
    }

    # include all implemented types with/without default value
    all_param = get_class_init_params(TestClassAll)
    all_param_asr = {
        "str": AttributeMeta(
            name="str",
            value=None,
            type=AttributeType.STRING,
            choices=[],
            required=True,
        ),
        "int": AttributeMeta(
            name="int",
            value=None,
            type=AttributeType.INTEGER,
            choices=[],
            required=True,
        ),
        "flt": AttributeMeta(
            name="flt",
            value=None,
            type=AttributeType.FLOAT,
            choices=[],
            required=True,
        ),
        "bool": AttributeMeta(
            name="bool",
            value=None,
            type=AttributeType.BOOLEAN,
            choices=[True, False],
            required=True,
        ),
        "obj": AttributeMeta(
            name="obj",
            value=None,
            type=AttributeType.OBJECT,
            choices=[],
            required=True,
        ),
        "unknown": AttributeMeta(
            name="unknown",
            value=None,
            type=AttributeType.UNKNOWN,
            choices=[],
            required=True,
        ),
        "tup": AttributeMeta(
            name="tup",
            value=None,
            type=AttributeType.TUPLE,
            choices=[],
            required=True,
        ),
        "lst": AttributeMeta(
            name="lst",
            value=None,
            type=AttributeType.ARRAY,
            choices=[],
            required=True,
        ),
        "union": AttributeMeta(
            name="union",
            value=None,
            type=AttributeType.STRING,
            choices=[],
            required=True,
        ),
        "enum": AttributeMeta(
            name="enum",
            value=None,
            type=AttributeType.ENUM,
            choices=[
                "STRING",
                "INTEGER",
                "FLOAT",
                "BOOLEAN",
                "ARRAY",
                "TUPLE",
                "OBJECT",
                "ENUM",
                "LITERAL",
                "UNKNOWN",
            ],
            required=True,
        ),
        "literal": AttributeMeta(
            name="literal",
            value=None,
            type=AttributeType.LITERAL,
            choices=["a", "b"],
            required=True,
        ),
        "str_val": AttributeMeta(
            name="str_val",
            value="string",
            type=AttributeType.STRING,
            choices=[],
            required=False,
        ),
        "int_val": AttributeMeta(
            name="int_val",
            value=0,
            type=AttributeType.INTEGER,
            choices=[],
            required=False,
        ),
        "flt_val": AttributeMeta(
            name="flt_val",
            value=0.0,
            type=AttributeType.FLOAT,
            choices=[],
            required=False,
        ),
        "bool_val": AttributeMeta(
            name="bool_val",
            value=True,
            type=AttributeType.BOOLEAN,
            choices=[True, False],
            required=False,
        ),
        "obj_val": AttributeMeta(
            name="obj_val",
            value={"dict": "val"},
            type=AttributeType.OBJECT,
            choices=[],
            required=False,
        ),
        "unknown_val": AttributeMeta(
            name="unknown_val",
            value=None,
            type=AttributeType.UNKNOWN,
            choices=[],
            required=False,
        ),
        "tup_val": AttributeMeta(
            name="tup_val",
            value=(1, "hello"),
            type=AttributeType.TUPLE,
            choices=[],
            required=False,
        ),
        "lst_val": AttributeMeta(
            name="lst_val",
            value=[1, 2, 3],
            type=AttributeType.ARRAY,
            choices=[],
            required=False,
        ),
        "union_val": AttributeMeta(
            name="union_val",
            value="string",
            type=AttributeType.STRING,
            choices=[],
            required=False,
        ),
        "enum_val": AttributeMeta(
            name="enum_val",
            value=AttributeType.ENUM,
            type=AttributeType.ENUM,
            choices=[
                "STRING",
                "INTEGER",
                "FLOAT",
                "BOOLEAN",
                "ARRAY",
                "TUPLE",
                "OBJECT",
                "ENUM",
                "LITERAL",
                "UNKNOWN",
            ],
            required=False,
        ),
        "literal_val": AttributeMeta(
            name="literal_val",
            value="a",
            type=AttributeType.LITERAL,
            choices=["a", "b"],
            required=False,
        ),
    }

    assert (
        str_param == str_param_asr
    ), f"Expected {str_param_asr},\n but got {str_param}"
    assert (
        all_param == all_param_asr
    ), f"Expected {all_param_asr},\n but got {all_param}"


"""
Testing embedded items
"""


def test_nested():
    # nested types with & wihtout value
    nested_param = get_class_init_params(TestClassNested)
    nested_param_asr = {
        "tuple": AttributeMeta(
            name="tuple",
            value=None,
            type=AttributeType.TUPLE,
            choices=[],
            required=True,
        ),
        "lst": AttributeMeta(
            name="lst",
            value=None,
            type=AttributeType.ARRAY,
            choices=[],
            required=True,
        ),
        "union": AttributeMeta(
            name="union",
            value=None,
            type=AttributeType.STRING,
            choices=[],
            required=True,
        ),
        "dict": AttributeMeta(
            name="dict",
            value=None,
            type=AttributeType.OBJECT,
            choices=[],
            required=True,
        ),
        "enum": AttributeMeta(
            name="enum",
            value=None,
            type=AttributeType.ENUM,
            choices=["NESTED", AttributeType],
            required=True,
        ),
        "option": AttributeMeta(
            name="option",
            value=None,
            type=AttributeType.INTEGER,
            choices=[],
            required=True,
        ),
        "tuple_val": AttributeMeta(
            name="tuple_val",
            value=((0, "string"), (0.0, False)),
            type=AttributeType.TUPLE,
            choices=[],
            required=False,
        ),
        "lst_val": AttributeMeta(
            name="lst_val",
            value=[[1, 2, 3], [4, 5, 6]],
            type=AttributeType.ARRAY,
            choices=[],
            required=False,
        ),
        "union_val": AttributeMeta(
            name="union_val",
            value="string",
            type=AttributeType.STRING,
            choices=[],
            required=False,
        ),
        "dict_val": AttributeMeta(
            name="dict_val",
            value={"key": {0: 0.0}},
            type=AttributeType.OBJECT,
            choices=[],
            required=False,
        ),
        "enum_val": AttributeMeta(
            name="enum_val",
            value=AttributeType.STRING,
            type=AttributeType.ENUM,
            choices=["NESTED", AttributeType],
            required=False,
        ),
        "option_val": AttributeMeta(
            name="option_val",
            value=0,
            type=AttributeType.INTEGER,
            choices=[],
            required=False,
        ),
    }

    assert (
        nested_param == nested_param_asr
    ), f"Expected {nested_param_asr},\n but got {nested_param}"


"""
Testing subclass
"""


def test_subclass():
    # getting params from subclass
    sub_param = get_class_init_params(TestSubSubClass)
    sub_param_asr = {
        "name": AttributeMeta(
            name="name",
            value=None,
            type=AttributeType.STRING,
            choices=[],
            required=True,
        ),
        "text": AttributeMeta(
            name="text",
            value="text",
            type=AttributeType.STRING,
            choices=[],
            required=False,
        ),
        "subname": AttributeMeta(
            name="subname",
            value=None,
            type=AttributeType.STRING,
            choices=[],
            required=True,
        ),
        "subtext": AttributeMeta(
            name="subtext",
            value="subtext",
            type=AttributeType.STRING,
            choices=[],
            required=False,
        ),
        "subsubname": AttributeMeta(
            name="subsubname",
            value=None,
            type=AttributeType.STRING,
            choices=[],
            required=True,
        ),
        "subsubtext": AttributeMeta(
            name="subsubtext",
            value="subsubtext",
            type=AttributeType.STRING,
            choices=[],
            required=False,
        ),
    }

    assert (
        sub_param == sub_param_asr
    ), f"Expected {sub_param_asr},\n but got {sub_param}"
