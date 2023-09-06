from types2json import AttributeMeta, AttributeType, get_class_init_params
from types2json.tests.base_test import BaseTest
from types2json.tests.classes import (
    ClassAll,
    ClassNested,
    ClassStr,
    SubSubClass,
)


class TestModelClasses(BaseTest):
    def test_attribute_meta(self):
        meta = AttributeMeta(
            name="param1",
            value="value1",
            choices=[],
            required=True,
        )

        assert meta.name == "param1"
        assert meta.value == "value1"
        assert meta.choices == []
        assert meta.required


class TestAttributeParser(BaseTest):
    """
    Simple test with dummy test classes
    Hardcoded the expected result
    """

    def test_all_cls(self):
        # String with and without default value
        str_param = get_class_init_params(ClassStr)
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
        all_param = get_class_init_params(ClassAll)
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

    def test_nested(self):
        # nested types with & wihtout value
        nested_param = get_class_init_params(ClassNested)
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

    def test_subclass(self):
        # getting params from subclass
        sub_param = get_class_init_params(SubSubClass)
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
