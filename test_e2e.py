
from base.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_logging()
        homePage = HomePage(self.driver)
        checoutpage = homePage.shopItems()
        log.info("Getting all the card tiles")
        product_tiles = checoutpage.getCardTiles()
        for product in product_tiles:
            log.info(product.text)
            if product.text == "Nokia Edge":
                checoutpage.getCardFooter().click()
        checoutpage.getCheckoutButton().click()
        confirmpage = checoutpage.confirmCheckoutBtn()
        confirmpage.getSuggestion().send_keys("i")
        self.verifyLinkPresence("//div[@class='suggestions']")
        # By.XPATH, "//div[@class='suggestions']")))
        confirmpage.selectCountry().click()
        confirmpage.checkBoxSelect().click()
        confirmpage.purchaseButton().click()
        text_success = confirmpage.alertMessage().text
        assert "Success" in text_success
        print(text_success)
        print("Demmo Print")
