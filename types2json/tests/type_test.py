from typing import (
    Dict,
    List,
    Literal,
    Union,
)

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
        obj_val: Dict = None,
        unknown_val: TestObject = None,
        tup_val: tuple = (1, "hello"),
        lst_val: List[int] = None,
        union_val: Union[str, int] = "string",
        enum_val: AttributeType = AttributeType.ENUM,
        literal_val: Literal["a", "b"] = "a",
    ) -> None:
        self.str = str


"""
A dummy test class for string parameters
"""


class TestClassStr:
    def __init__(
        self,
        name: str,
        text: str = "text",
    ) -> None:
        self.name = name
        self.text = text


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
            value=TestObject(),
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


#  ---- testing mmlapipe nodes ----
# from chimerapy.pipelines.yolov8.multi_vid_pose import YoloV8Node
# from chimerapy.pipelines.yolov8.multi_save import MultiSaveNode

# def test_nodes():
#     # yolo node
#     yolo_param = get_class_init_params(YoloV8Node)
#     yolo_param_asr = {}
#     print("\n".join(str(param.model_dump()) for _, param in yolo_param.items()))

#     # save node
#     save_param = get_class_init_params(MultiSaveNode)
#     save_param_asr = {}
#     print("\n".join(str(param.model_dump()) for _, param in save_param.items()))