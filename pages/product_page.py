from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def go_to_add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()


    def should_be_in_the_basket(self):
        title_of_the_book = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), f"Book {title_of_the_book} is not in the basket"

    def should_be_the_book(self):
        title_of_the_book = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        title_of_the_book_in_the_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert title_of_the_book == title_of_the_book_in_the_basket, f"Book {title_of_the_book_in_the_basket} is in the basket, but it must be {title_of_the_book}"

    def should_be_basket_value_message(self):
        value_of_the_book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_IN_THE_BASKET), f"It should be {value_of_the_book} price"

    def should_be_basket_value_price(self):
        value_of_the_book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        value_of_the_book_in_the_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_THE_BASKET).text
        assert value_of_the_book == value_of_the_book_in_the_basket, f"Price  {value_of_the_book_in_the_basket} should be equal {value_of_the_book}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "message is not disappeared"