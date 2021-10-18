
from Pages.SearchPage import SearchPage
from Tests.BaseTest import Test_Base
from Utilities.TestData import TestData


class Test_Calculator(Test_Base) :
    def test_eicher_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.eicher_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.eicher_count, TestData.eicher_price)
        log.info("Profit on Eicher Motors is " + str(profit))

    def test_itc_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.itc_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.itc_count, TestData.itc_price)
        log.info("Profit on ITC is " + str(profit))

    def test_reliance_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.reliance_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.reliance_count, TestData.reliance_price)
        log.info("Profit on Reliance is " + str(profit))

    def test_tatamotors_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.tatamotors_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.tatamotors_count, TestData.tatamotors_price)
        log.info("Profit on Tata Motors is " + str(profit))

    def test_vodafone_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.vodafone_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.vodafone_count, TestData.vodafone_price)
        log.info("Profit on Vodafone Idea is " + str(profit))

    def test_equitas_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.equitas_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.equitas_count, TestData.equitas_price)
        log.info("Profit on Equitas Holdings is " + str(profit))

    def test_federalbank_profit(self):
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.federalbank_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.federalbank_count, TestData.federalbank_price)
        print("Profit on Federal Bank is " + str(profit))

    def test_indoco_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.indoco_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.indoco_count, TestData.indoco_price)
        log.info("Profit on Indoco Remedies is " + str(profit))

    def test_irb_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.irb_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.irb_count, TestData.irb_price)
        log.info("Profit on IRB Infrastructure is " + str(profit))

    def test_kopran_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.kopran_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.kopran_count, TestData.kopran_price)
        log.info("Profit on Kopran is " + str(profit))

    def test_neuland_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.neuland_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.neuland_count, TestData.neuland_price)
        log.info("Profit on Neuland Pharma is " + str(profit))

    def test_praj_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.praj_search)
        searchpage.click_enter()
        searchpage.search_clear()
        profit = searchpage.find_present_price(TestData.praj_count, TestData.praj_price)
        log.info("Profit on Praj Industries is " + str(profit))

    def test_hcg_profit(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.send_share_name(TestData.hcg_search)
        searchpage.click_enter()
        profit = searchpage.find_present_price(TestData.hcg_count, TestData.hcg_price)
        log.info("Profit on HCG is " + str(profit))














