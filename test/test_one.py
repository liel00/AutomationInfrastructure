from page_objects.one_page import OneTest
from utilities import Base


class TestOne(Base):
    def test_one(self):
        one = OneTest(self.driver)
        one.click_search()
