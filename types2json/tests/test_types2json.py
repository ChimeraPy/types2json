from types2json import AttributeMeta
from types2json.tests.base_test import BaseTest


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
