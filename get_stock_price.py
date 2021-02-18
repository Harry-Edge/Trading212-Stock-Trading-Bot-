from selenium import webdriver
import time
from bs4 import BeautifulSoup

PATH = "</YOUR PATH TO GECKO DRIVER>"
drive = webdriver.Firefox(executable_path=PATH)

driver1 = drive
time.sleep(2)


class GatherStockInformation:

    """ This class grabs stock information from Yahoo Finance """

    def clear_cookie_message(self):

        try:
            driver1.find_element_by_xpath("//button[@value='agree']").click()
            time.sleep(1)
        except Exception:
            pass

    def get_current_stock_price(self, ticker):

        driver1.get("https://uk.finance.yahoo.com/quote/" + str(ticker) + "?p=TSLA&.tsrc=fin-srch")
        self.clear_cookie_message()
        time.sleep(3)

        try_limit = 0

        """ Stock prices updates take a fraction of a second to display 
         so this tries 100 times to get the new price """

        while try_limit != 100:
            try:
                html = driver1.execute_script('return document.body.innerHTML;')
                soup = BeautifulSoup(html, features="html.parser")

                close_price = [entry.text for entry in
                               soup.find_all('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]

                return close_price[0]

            except Exception:
                pass
            time.sleep(0.02)
            try_limit += 1

    def get_yahoo_stock_page(self, ticker):

        driver1.get("https://uk.finance.yahoo.com/quote/" + str(ticker) + "?p=TSLA&.tsrc=fin-srch")
        time.sleep(1)
        self.clear_cookie_message()
        time.sleep(1)

    def constantly_return_stock_price_on_page(self):

        """ This will return the stock price on a given Yahoo Finance page as it changes """

        try_limit = 0

        """ Stock prices updates take a fraction of a second to display 
        so this tries 200 times to get the new price """

        while try_limit != 200:
            try:
                html = driver1.execute_script('return document.body.innerHTML;')
                soup = BeautifulSoup(html, features="html.parser")

                close_price = [entry.text for entry in
                               soup.find_all('span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]

                return close_price[0]

            except IndexError:
                pass
            time.sleep(0.02)
            try_limit += 1
