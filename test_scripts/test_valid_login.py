from generics.base_test import BaseTest
from pages.login_page import LoginPage
from pages.home_page import HomePage


class Test_ValidLogin(BaseTest):
    def test_valid_login(self):
        # 1. enter valid username
        login_page=LoginPage(self.page)
        login_page.set_username("student123")
        # 2. enter valid password
        login_page.set_password("akshara123")
        # 3. click on go button
        login_page.click_go_button()
        # 4. verify that home page is displayed
        home_page=HomePage(self.page)
        result=home_page.verify_homepage_is_displayed()
        assert result