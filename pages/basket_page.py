from .base_page import BasePage
from .locators import BasketPagePageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPagePageLocators.ITEMS_IN_THE_BASKET), \
                    "Success message is presented, but should not be"

    def should_be_text_in_the_basket(self):
        assert self.is_element_present(*BasketPagePageLocators.TEXT_ABOUT_THE_EMPTY_BASKET), 'The basket is not empty'