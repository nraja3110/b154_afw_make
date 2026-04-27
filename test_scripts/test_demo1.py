import time

from generics.base_test import BaseTest
from generics.utility import Utility
from pages.login_page import LoginPage

class Test1(BaseTest):

    def test_1(self):
        print("test 1")
        print(self.page.title())
        xl_data=Utility.read_xl(self.xl_path,"test_1",2,1)
        print(xl_data)
        login_page=LoginPage(self.page)
        login_page.set_username(xl_data)
        print("end")
