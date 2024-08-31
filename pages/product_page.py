import math
from selenium.common import NoAlertPresentException
from .base_page import BasePage
from .locators import BooksPageLocators


class ProductPage(BasePage):

    def go_to_add_to_basket(self):
        add_to_basket = self.browser.find_element(*BooksPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_in_the_basket(self):
        title_of_the_book = self.browser.find_element(*BooksPageLocators.BOOK_TITLE).text
        assert self.is_element_present(*BooksPageLocators.BOOK_TITLE_IN_THE_BASKET), f"Book {title_of_the_book} is not in the basket"

    def should_be_the_book(self):
        title_of_the_book = self.browser.find_element(*BooksPageLocators.BOOK_TITLE).text
        title_of_the_book_in_the_basket = self.browser.find_element(*BooksPageLocators.BOOK_TITLE_IN_THE_BASKET).text
        assert title_of_the_book == title_of_the_book_in_the_basket, f"Book {title_of_the_book_in_the_basket} is in the basket, but it must be {title_of_the_book}"

    def should_be_basket_value_message(self):
        value_of_the_book = self.browser.find_element(*BooksPageLocators.BOOK_PRICE).text
        assert self.is_element_present(*BooksPageLocators.BOOK_PRICE_IN_THE_BASKET), f"It should be {value_of_the_book} price"

    def should_be_basket_value_price(self):
        value_of_the_book = self.browser.find_element(*BooksPageLocators.BOOK_PRICE).text
        value_of_the_book_in_the_basket = self.browser.find_element(*BooksPageLocators.BOOK_PRICE_IN_THE_BASKET).text
        assert value_of_the_book == value_of_the_book_in_the_basket, f"Price  {value_of_the_book_in_the_basket} should be equal {value_of_the_book}"
