from playwright.sync_api._generated import  Page

class HomePage:
    __home:str

    def __init__(self,page:Page):
        self.page = page
        self.__home="//a[text()='Home']"

    def verify_homepage_is_displayed(self)->bool:
        try:
            self.page.locator( self.__home).wait_for()
            print("Home Page is Displayed")
            return True
        except:
            print("Home Page is Not Displayed")
            return False
