from time import sleep
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
#ages.main_page import (MainPage)


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    sleep(4)
    page.go_to_login_page()   # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    sleep(4)

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    sleep(1)
    page.should_be_login_link()
    sleep(1)

