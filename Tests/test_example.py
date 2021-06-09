import pytest

from PageObject.example_page import Example
from utilities.base_test import BaseTest
from utilities.data import Data


class TestLogin(BaseTest):

    def test_click(self, get_data):
        log = self.getLogger()
        log.info("This is example test ")
        self.login = Example(self.driver)
        self.login.send_key2(get_data["address"])
        self.login.search1()

    @pytest.fixture(params=Data.test_data_example)
    def get_data(self, request):
        return request.param
