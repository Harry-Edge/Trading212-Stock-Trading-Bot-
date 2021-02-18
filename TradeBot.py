from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import smtplib
import time
from stratergies import Strategy001, Strategy002, Strategy003

PATH = "</YOUR PATH TO GECKO DRIVER>"
tradebot = webdriver.Firefox(executable_path=PATH)
time.sleep(2)


class Trading212WebBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.uniqName = "uniqName_0_"

    def login(self):
        print("//---------------------------//")
        print("Staring TRADING212 BOT....")

        tradebot.get("https://www.trading212.com/en/login")
        time.sleep(2)

        # Clears the cookie message if there is one
        try:
            tradebot.find_element_by_xpath("//button[@value='agree']").click()
            time.sleep(1)
        except Exception:
            pass

        print("Logging into Trading212 Account...\n")

        email = tradebot.find_element_by_id("username-real")
        password = tradebot.find_element_by_id("pass-real")

        email.clear()
        password.clear()
        time.sleep(1)

        email.send_keys(self.username)
        password.send_keys(self.password)

        try:
            password.send_keys(Keys.RETURN)
        except Exception:
            print("[-] Failed to Login\n")

        time.sleep(2)
        if tradebot.current_url == "https://demo.trading212.com/":
            print("[+] Successfully Logged in")
        else:
            print("[-] Failed to Login")

        time.sleep(5)

    def buy_stock(self, ticker_name, amount_of_shares):

        """ This function will not work is Trading212 search returns more than one ticker """

        # MAKE AN IF STATEMENT TO REJECT MORE THAN ONE SEARCH RESULT
        print("\n-----BUY------")
        print("Attempting to Buy " + str(amount_of_shares) + " Share/s of: " + ticker_name.upper())

        # Searches for the ticker
        tradebot.find_element_by_id("navigation-search-button").click()
        time.sleep(2)

        search = tradebot.find_element_by_class_name("search-input")
        search.clear()
        search.send_keys(ticker_name)
        search.send_keys(Keys.RETURN)
        time.sleep(3)

        # clicks on search result by finding the UniquenameID
        unique_name_id = 194
        run = True
        press = False
        while unique_name_id != 700 and run:
            try:
                element_try = self.uniqName + str(unique_name_id)
                unique_name_id += 1
                press = tradebot.find_element_by_id(str(element_try))
                if press:
                    press.click()
                    run = False
            except Exception:
                pass
        if press is False:
            print("[-] Failed to click on the search option when buying the stock")

        print("after firstclicl " + unique_name_id)
        # Presses the buy button (finds it buy adding 14 to the previous id)
        time.sleep(3)
        unique_name_id += 16
        print("buy " + unique_name_id)
        # ^^^^ THIS COULD BE 13 OR 14
        try:
            tradebot.find_element_by_id(self.uniqName + str(unique_name_id)).click()
        except Exception:
            print("failed")
            print("Failed to Buy Stock, Attempting Again")
            time.sleep(3)
            unique_name_id -= 1

            try:
                tradebot.find_element_by_id(self.uniqName + str(unique_name_id)).click()
            except Exception:
                print("[-] Failed to Press Buy Second Time")

        # Inputs amount of shares to buy
        time.sleep(2)
        unique_name_id += 18
        try:
            enter_share_amount = tradebot.find_element_by_id(self.uniqName + str(unique_name_id))
            enter_share_amount.send_keys(amount_of_shares)
        except Exception:
            print("[-] Failed to Enter the Amount of Shares to Buy")

        # Reviews the order
        time.sleep(2)
        unique_name_id += 2
        try:
            tradebot.find_element_by_id(self.uniqName + str(unique_name_id)).click()
            print("Reviewing the Order...")
        except Exception:
            print("[-] Failed to Review the Buy Order")

        # Sends buy order
        time.sleep(2)
        unique_name_id += 38
        successfully_purchased = False
        try:
            tradebot.find_element_by_id(self.uniqName + str(unique_name_id)).click()
            print("[+] The Order to Buy " + str(amount_of_shares) + " Share/s of " + ticker_name.upper()
                  + " Has Been Fulfilled")
            # RETURN ORDER TRUE VARIABLE
            successfully_purchased = True
        except Exception:
            print("[-] Failed to Buy The Stock")

        # Returns to the dashboard page

        time.sleep(2)
        tradebot.get("https://demo.trading212.com/")

        print("------BUY OVER------\n")

        if successfully_purchased:
            return True
        else:
            return False

    def sell_stock(self, ticker_name, amount_of_shares):

        """ This function will not work is Trading212 search returns more than one ticker """

        print("\n-----SELL------")
        print("Attemping to Sell " + str(amount_of_shares) + " share/s of: " + ticker_name.upper())

        # Searches for the ticker
        time.sleep(3)
        tradebot.find_element_by_id("navigation-search-button").click()
        time.sleep(3)

        search = tradebot.find_element_by_class_name("search-input")
        search.clear()
        search.send_keys(ticker_name)
        search.send_keys(Keys.RETURN)
        time.sleep(3)

        # Clicks the stock search result
        unique_name_id = 195
        run = True
        press = False
        while unique_name_id != 700 and run:
            try:
                element_try = self.uniqName + str(unique_name_id)
                unique_name_id += 1
                # print(element_try)
                press = tradebot.find_element_by_id(str(element_try))
                tradebot.f
                if press:
                    press.click()
                    run = False
            except Exception:
                pass

        if press is False:
            print("[-] Failed to Click on the Search Option When Selling the Stock")

        # --- Presses the Sell Button ---
        time.sleep(2)
        unique_name_id += 14
        # ^^^^ THIS COULD BE 13 OR 14
        try:
            sellbutton = tradebot.find_element_by_id(self.uniqName + str(unique_name_id))
            sellbutton.find_element_by_class_name("sell-button").click()
        except Exception:
            print("[-] Failed to Press the Sell Button")
            time.sleep(3)
            unique_name_id -= 1
            try:
                tradebot.find_element_by_id(self.uniqName + str(unique_name_id)).click()
            except Exception:
                print("[-] Failed to Press Sell a Second Time")


        # --- ENTERS AMOUNT OF SHARES TO SELL ---
        time.sleep(2)
        unique_name_id += 18
        try:
            enter_share_amount = tradebot.find_element_by_id(self.uniqName + str(unique_name_id))
            enter_share_amount.send_keys(amount_of_shares)
        except Exception:
            print("[-] Failed to Enter the Amount of Shares to buy when trying to sell the stock")

        # --- REVIEWS THE ORDER ---
        time.sleep(2)
        unique_name_id += 2
        try:
            tradebot.find_element_by_id(self.uniqName + str(unique_name_id)).click()
            print("Reviewing the Order...")
        except Exception:
            print("[-] Failed to Review the Order When Selling")

        # --- SENDS SELL ORDER ---
        time.sleep(2)
        unique_name_id += 38
        successfully_sold = False
        try:
            tradebot.find_element_by_id(self.uniqName + str(unique_name_id)).click()
            print("[+] The Order to Sell " + str(amount_of_shares) + " share/s of: " + ticker_name.upper()
                  + " has been fulfilled")
            successfully_sold = True
        except Exception:
            print("[-] Failed To Send Final Sell Order")

        # --- Returns to Home ---

        time.sleep(2)
        tradebot.get("https://demo.trading212.com/")

        print("------SELL OVER------\n")

        if successfully_sold:
            return True
        else:
            return False

    def get_account_value(self):
        time.sleep(1)
        try:
            account_value1 = tradebot.find_element_by_id("equity-total")
            processed_value = account_value1.find_element_by_class_name("equity-item-value").text

            processed_value = processed_value[1:3] + processed_value[4:10]

            return str(processed_value)
        except Exception:
            return False


class TradingBot:

    def __init__(self, t212username, t212password, strategy=None, risk_category=None, stock_list=None,
                email_reports=False, from_email=None, from_email_password=None, to_email=None):

        self.tradebot1 = Trading212WebBot(t212username, t212password)
        self.current_open_positions = {}
        self.current_open_positions_share_amount = {}
        self.amount_of_completed_trades = 0
        self.risk_category = risk_category
        self.strategy = strategy
        self.input_stock_list = stock_list



        if strategy is None:
            print("[-] Please Specify a Strategy When Creating the Class")
            exit()

        if email_reports:
            if from_email is None or from_email_password is None or to_email is None:
                print("[-] Email Parameter Missing, Please Check the Credentials ")
            else:
                self.from_email = from_email
                self.to_email = to_email
                self.from_email_password = from_email_password

        if self.strategy == 1:
            if len(stock_list) != 1:
                print("[-] Strategy001 Requires 1 Stock")
                exit()
            strategy = Strategy001(self.input_stock_list)
        elif self.strategy == 2:
            if len(stock_list) != 3:
                print("[-] Strategy002 Requires 3 Stocks")
                exit()
            strategy = Strategy002(self.input_stock_list)
        elif self.strategy == 3:
            if len(stock_list) != 8:
                print("[-] Strategy003 Requires 8 Stocks")
                exit()
            strategy = Strategy003(self.input_stock_list)

        if self.check_if_market_is_open() is False:
            exit()

        # Starts the Bot if all the initialisation conditions have been met
        else:
            self.tradebot1.login()

            self.account_value_on_login = self.tradebot1.get_account_value()
            print("Account Value on Login: £" + self.account_value_on_login, "\n")

            self.start_trading(strategy)

    def check_if_market_is_open(self):

        """ Checks if the US stock market is open. Currently it is from GMT 2:30PM
         - 9PM. This function will wait until 2:40PM due to the volatility during market open"""

        # Checks if it is Weekend
        day_of_week = datetime.today().weekday()

        # Checks What Current Time it is
        current_time = datetime.now()
        current_time = int((current_time.strftime("%H%M")))

        error_message = "\n [-] US Stock Market is Not Open Until Monday at GMT 2:30PM, Quitting Program..."

        if day_of_week < 5:

            if current_time >= int(1440) and current_time <= int(2050):
                return True
            elif current_time <= int(1440):
                print("\n[-] US Stock Market is Closed Until 2:30PM")
                wait = input("\n 1. Wait Until Stock Market Opens \n 2. Quit\n")
                if wait == "1":
                    while current_time < 1440:
                        current_time = datetime.now()
                        current_time = int((current_time.strftime("%H%M")))
                        print("\r Waiting Until 14:40... " + "Current Time: " + str(current_time), end="")
                        time.sleep(60)

                    return True
                elif wait == "2":
                    exit()
            elif current_time >= int(2055):
                print("\n[-] US Stock Market is Closed Until 2:30PM")
                return False

        elif day_of_week > 4 and current_time >= int(2050):
            print(error_message)
            return False
        else:
            print(error_message)
            return False

    def process_risk_category(self, ticker_price):

        """ This function chooses how much of you portfolio to gamble
            by deciding how many share to buy of a given stock

            1. The whole portfolio is using in trading
            2. Half of the portfolio is used
            3. One third is used """

        account_value = float(self.tradebot1.get_account_value())

        if self.risk_category == 1:
            account_value = account_value * float(0.95)
        elif self.risk_category == 2:
            account_value = account_value * float(0.5)
        elif self.risk_category == 3:
            account_value = account_value * float(0.33)

        if self.strategy == 1:
            return round(account_value / float(ticker_price))
        elif self.strategy == 2:
            account_value = account_value / 3
            return round(account_value / float(ticker_price))
        elif self.strategy == 3:
            account_value = account_value / 8
            return round(account_value / float(ticker_price))

    def evaluate_bot_performance_on_exit(self):

        """ This function evaluated the profit/loss the Bot made after it
        has completed its trade/crashed """


        account_value_after_exiting = self.tradebot1.get_account_value()
        time.sleep(2)

        print("\n\n _______ BOT PERFORMANCE _______")

        if account_value_after_exiting < self.account_value_on_login:
            print("Account Value After Trading: £" + account_value_after_exiting)
            print("The BOT Made a Loss of: £", (float(self.account_value_on_login)
                                                - float(account_value_after_exiting)))
        elif account_value_after_exiting > self.account_value_on_login:
            print("Account Value After Trading: £" + account_value_after_exiting)
            print("The BOT Made a Profit of: £", (float(account_value_after_exiting)
                                                  - float(self.account_value_on_login)))
        elif account_value_after_exiting == self.account_value_on_login:
            print("BOT Broke Even")

        print("Amount of Completed Trades Done: " + str(self.amount_of_completed_trades))

    def evaluate_bot_performance_during(self):

        """ This function evaluated the profit/loss the Bot made during
        the running of the program """

        get_current_account_value = self.tradebot1.get_account_value()

        if get_current_account_value < self.account_value_on_login:
            print("Current Loss: £" + str((float(self.account_value_on_login) - float(get_current_account_value))))
        elif get_current_account_value > self.account_value_on_login:
            print("Current Profit: £" + str((float(get_current_account_value) - float(self.account_value_on_login))))

    def send_buy_order(self, ticker, buying_price, share_amount):

        if ticker not in self.current_open_positions:
            try:
                buy = self.tradebot1.buy_stock(ticker, share_amount)

                if buy is True:
                    print(ticker, "Added to Portfolio")
                    self.current_open_positions.update({ticker: buying_price})
                    self.current_open_positions_share_amount.update({ticker: share_amount})
                    return True

            except Exception:
                print("[-] Failed To Initialise Buy Order of: " + ticker)
        else:
            print("[-] Failed to Initialise Buy Order as " + str(ticker) + " is Already in the Portfolio")

        return False

    def send_sell_order(self, ticker, share_amount):

        if ticker in self.current_open_positions:
            try:
                sell = self.tradebot1.sell_stock(ticker, share_amount)
                if sell is True:
                    print("Stock Removed From Portfolio")
                    del self.current_open_positions[ticker]
                    del self.current_open_positions_share_amount[ticker]
                    self.amount_of_completed_trades += 1
                    return True

            except Exception:
                print("[-] Failed to Sell " + ticker)
        else:
            print("[-] Cannot Sell " + str(ticker) + " Because its not an Open Position in Current Portfolio")

        return False

    def print_current_portfolio(self):

        print("\n______Current Portfolio_______")
        print("\nTicker --- Buy Price ---- Share Amount")
        for stock in self.current_open_positions:
            print(stock, "\t", str(self.current_open_positions[stock]), "\t",
                  self.current_open_positions_share_amount[stock])
        print("Successful trades: " + str(self.amount_of_completed_trades))
        self.evaluate_bot_performance_during()

        print("------------------------\n")

    def start_trading(self, strategy):

        """ This is the main buying/selling loop of the Bot program"""

        try:
            while True:

                for ticker in strategy.stock_list:

                    if ticker not in self.current_open_positions:

                        try:
                            worth_buying, buying_price = strategy.evaluate_buying_potential(ticker)

                            if worth_buying is True:
                                share_amount = self.process_risk_category(buying_price)
                                buy_stock = self.send_buy_order(ticker, buying_price, share_amount)

                                if buy_stock is True:
                                    self.print_current_portfolio()

                                # Tries to buy the stock again it it fails the first time
                                elif buy_stock is False:
                                    time.sleep(2)
                                    print("Attempting to Buy Again")
                                    second_buy = self.send_buy_order(ticker, buying_price, share_amount)
                                    if second_buy is False:
                                        print("[-] Bot Error, Failed to Buy", ticker, ", Stopping Attempt...")
                        except TypeError:
                            pass

                try:
                    for ticker in self.current_open_positions:
                        worth_selling = strategy.evaluate_selling_potential(ticker, self.current_open_positions[ticker])

                        if worth_selling is True:
                            sell_stock = self.send_sell_order(ticker, self.current_open_positions_share_amount[ticker])
                            if sell_stock is False:
                                time.sleep(2)
                                print()

                                # Tries to sell the stock again it it fails the first time
                                second_sell = self.send_sell_order(ticker,
                                                                   self.current_open_positions_share_amount[ticker])

                                # If it can't sell again the stock is kept as an open position
                                if second_sell is False:
                                    print("[-] Bot Error, Failed to Sell", ticker, ", Stopping Trading of Ticker")
                                    strategy.stock_list.remove(ticker)

                            elif sell_stock is True:
                                self.evaluate_bot_performance_during()

                except RuntimeError:
                    pass

                # Check if the US stock market is about to close and will subsequently ene all current position
                if self.check_if_market_is_open() is False:
                    print("[-] Market is About to Close. Ending all Positions. ")
                    self.close_all_positions()

        except KeyboardInterrupt:
            print("[-] Detected Control + C, Closing all Current Positions")
            self.close_all_positions()
            exit()

    def close_all_positions(self):

        try:
            for ticker in self.current_open_positions:
                self.send_sell_order(ticker, self.current_open_positions_share_amount[ticker])
            self.evaluate_bot_performance_on_exit()
        except RuntimeError:
            pass