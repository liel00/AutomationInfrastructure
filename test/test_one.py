from page_objects.one_page import OneTest
from utilities import Base


class TestOne(Base.Base):
    def test_one(self):
        one = ObjectTest()
        one.click_gmail()
