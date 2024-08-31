from time import sleep
from .pages.product_page import ProductPage

from selenium.common.exceptions import NoAlertPresentException # в начале файла



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_in_the_basket()
    page.should_be_the_book()
    page.should_be_basket_value_message()
    page.should_be_basket_value_price()
