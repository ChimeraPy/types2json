import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        return tmpdir.chdir()

    def test_get_params_from_function(self):
        assert True
