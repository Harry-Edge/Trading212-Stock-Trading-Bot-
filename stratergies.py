from get_stock_price import GatherStockInformation
import time


class Strategy001:

    """ Strategy001 is only buying and selling one specific stock """

    def __init__(self, stock_list):
        self.get_stock_info = GatherStockInformation()
        self.previous_stock_prices = []
        self.stock_list = stock_list

    def evaluate_buying_potential(self, ticker):

        """ This will evaluate if the stock price has increased by 1% compared to when the function started,
        the function will only compare against the last 120 stock prices until it returns true """

        comparison_stock_price = 0

        self.get_stock_info.get_yahoo_stock_page(ticker)

        current_stock_price = self.get_stock_info.constantly_return_stock_price_on_page()
        self.previous_stock_prices.append(current_stock_price)

        # Checks to see if more than 120 comparisons has been made
        if len(self.previous_stock_prices) < 120:
            comparison_stock_price = self.previous_stock_prices[0]
        elif len(self.previous_stock_prices) >= 120:
            comparison_stock_price = self.previous_stock_prices[-115]

        print("\r//BUY// - Analysing:", str(ticker), " Current Price: $" + str(current_stock_price),
              "\t//CP: $" + str(comparison_stock_price), end="")

        try:
            if float(current_stock_price) >= float(comparison_stock_price) * float(1.00003):
                print("\n", str(ticker), "is Worth Buying")
                self.previous_stock_prices.clear()
                return True, current_stock_price
        except TypeError:
            pass

        #1.01

        time.sleep(1)

    def evaluate_selling_potential(self, ticker, buying_price):

        """ This will sell if the stock has gone up by 0.6%. It will also sell
        if the stock has gone down by 0.5% to stop losses"""

        self.get_stock_info.get_yahoo_stock_page(ticker)

        current_stock_price = self.get_stock_info.constantly_return_stock_price_on_page()
        print("\r//SELL// - Analysing:", str(ticker), "Current Price: $" + str(current_stock_price),
              "\t/BP: $", str(buying_price), end="")

        try:
            if float(current_stock_price) >= float(buying_price) * float(1.00003):
                print("Stock is Made Enough Profit. Selling...")
                return True
            elif float(current_stock_price) <= float(buying_price) * float(0.995):
                print(str(ticker), "Had Dropped. Selling to Stop Losses...")
                return True
        except TypeError:
            pass

        time.sleep(3)
        #1.006


class Strategy002:

    """ Strategy002 will analyse a collection of 3 stock """

    def __init__(self, stock_list):
        self.get_stock_info = GatherStockInformation()
        self.stock_list = stock_list

        self.tick1_previous_stock_prices = []
        self.tick2_previous_stock_prices = []
        self.tick3_previous_stock_prices = []

    def evaluate_buying_potential(self, ticker):

        """ This will evaluate if the stock price has increased by 0.75% compared to when the function started,
                the function will only compare against the last 60 stock prices until it returns true """

        comparison_stock_price = 0

        self.get_stock_info.get_yahoo_stock_page(ticker)
        current_stock_price = self.get_stock_info.constantly_return_stock_price_on_page()

        if ticker == self.stock_list[0]:
            self.tick1_previous_stock_prices.append(current_stock_price)
            if len(self.tick1_previous_stock_prices) < 60:
                comparison_stock_price = self.tick1_previous_stock_prices[0]
            elif len(self.tick1_previous_stock_prices) >= 60:
                comparison_stock_price = self.tick1_previous_stock_prices[-55]
        elif ticker == self.stock_list[1]:
            self.tick2_previous_stock_prices.append(current_stock_price)
            if len(self.tick2_previous_stock_prices) < 60:
                comparison_stock_price = self.tick2_previous_stock_prices[0]
            elif len(self.tick2_previous_stock_prices) >= 60:
                comparison_stock_price = self.tick2_previous_stock_prices[-55]
        elif ticker == self.stock_list[2]:
            self.tick3_previous_stock_prices.append(current_stock_price)
            if len(self.tick3_previous_stock_prices) < 60:
                comparison_stock_price = self.tick3_previous_stock_prices[0]
            elif len(self.tick3_previous_stock_prices) >= 60:
                comparison_stock_price = self.tick3_previous_stock_prices[-55]

        print("\r//BUY// - Analysing:", str(ticker), " Current Price: $" + str(current_stock_price),
              "\t//CP: $" + str(comparison_stock_price), end="")

        try:
            if float(current_stock_price) >= float(comparison_stock_price) * float(1.0075):
                print("\n", str(ticker), " is Worth Buying ")

                if ticker == self.stock_list[0]:
                    self.tick1_previous_stock_prices.clear()
                elif ticker == self.stock_list[1]:
                    self.tick2_previous_stock_prices.clear()
                elif ticker == self.stock_list[2]:
                    self.tick3_previous_stock_prices.clear()

                return True, current_stock_price

        except TypeError:
            pass

    def evaluate_selling_potential(self, ticker, buying_price):

        """ This will sell if the stock has gone up by 0.5%. It will also sell
               if the stock has gone down by 0.5% to stop losses"""

        self.get_stock_info.get_yahoo_stock_page(ticker)

        current_stock_price = self.get_stock_info.constantly_return_stock_price_on_page()

        print("\r//SELL// - Analysing:", ticker, "Current Price: $" + str(current_stock_price),
              "\t//BP: $", str(buying_price), end="")

        try:
            if float(current_stock_price) >= float(buying_price) * float(1.005):
                print("\n", ticker, "Has Made Enough Profit. Selling...")
                return True
            elif float(current_stock_price) <= float(buying_price) * float(0.995):
                print("\n", ticker, "Has Tanked, Selling to Stop Losses")
                return True
        except TypeError:
            pass


class Strategy003:

    """ Strategy003 will analyse a collection of 8 stocks"""

    def __init__(self, stock_list):
        self.get_stock_info = GatherStockInformation()

        self.stock_list = stock_list

        self.tick1_previous_stock_prices = []
        self.tick2_previous_stock_prices = []
        self.tick3_previous_stock_prices = []
        self.tick4_previous_stock_prices = []
        self.tick5_previous_stock_prices = []
        self.tick6_previous_stock_prices = []
        self.tick7_previous_stock_prices = []
        self.tick8_previous_stock_prices = []

    def evaluate_buying_potential(self, ticker):

        """ This will evaluate if the stock price has increased by 1% compared to when the function started,
        the function will only compare against the last 20 stock prices until it returns true """

        comparison_stock_price = 0

        self.get_stock_info.get_yahoo_stock_page(ticker)
        current_stock_price = self.get_stock_info.constantly_return_stock_price_on_page()

        if ticker == self.stock_list[0]:
            self.tick1_previous_stock_prices .append(current_stock_price)
            if len(self.tick1_previous_stock_prices) < 20:
                comparison_stock_price = self.tick1_previous_stock_prices[0]
            elif len(self.tick1_previous_stock_prices) >= 20:
                comparison_stock_price = self.tick1_previous_stock_prices[-19]
        elif ticker == self.stock_list[1]:
            self.tick2_previous_stock_prices .append(current_stock_price)
            if len(self.tick2_previous_stock_prices) < 20:
                comparison_stock_price = self.tick2_previous_stock_prices[0]
            elif len(self.tick2_previous_stock_prices) >= 20:
                comparison_stock_price = self.tick2_previous_stock_prices[-19]
        elif ticker == self.stock_list[2]:
            self.tick3_previous_stock_prices.append(current_stock_price)
            if len(self.tick3_previous_stock_prices) < 20:
                comparison_stock_price = self.tick3_previous_stock_prices[0]
            elif len(self.tick3_previous_stock_prices) >= 20:
                comparison_stock_price = self.tick3_previous_stock_prices[-19]
        elif ticker == self.stock_list[3]:
            self.tick4_previous_stock_prices.append(current_stock_price)
            if len(self.tick4_previous_stock_prices) < 20:
                comparison_stock_price = self.tick4_previous_stock_prices[0]
            elif len(self.tick4_previous_stock_prices) >= 20:
                comparison_stock_price = self.tick4_previous_stock_prices[-19]
        elif ticker == self.stock_list[4]:
            self.tick5_previous_stock_prices.append(current_stock_price)
            if len(self.tick5_previous_stock_prices) < 20:
                comparison_stock_price = self.tick5_previous_stock_prices[0]
            elif len(self.tick5_previous_stock_prices) >= 20:
                comparison_stock_price = self.tick5_previous_stock_prices[-19]
        elif ticker == self.stock_list[5]:
            self.tick6_previous_stock_prices.append(current_stock_price)
            if len(self.tick6_previous_stock_prices) < 20:
                comparison_stock_price = self.tick6_previous_stock_prices[0]
            elif len(self.tick6_previous_stock_prices) >= 20:
                comparison_stock_price = self.tick6_previous_stock_prices[-19]
        elif ticker == self.stock_list[6]:
            self.tick7_previous_stock_prices.append(current_stock_price)
            if len(self.tick7_previous_stock_prices) < 20:
                comparison_stock_price = self.tick7_previous_stock_prices[0]
            elif len(self.tick7_previous_stock_prices) >= 20:
                comparison_stock_price = self.tick7_previous_stock_prices[-19]
        elif ticker == self.stock_list[7]:
            self.tick8_previous_stock_prices.append(current_stock_price)
            if len(self.tick8_previous_stock_prices) < 20:
                comparison_stock_price = self.tick8_previous_stock_prices[0]
            elif len(self.tick8_previous_stock_prices) >= 20:
                comparison_stock_price = self.tick8_previous_stock_prices[-19]

        print("\r//BUY// - Analysing:", str(ticker), " Current Price: $" + str(current_stock_price),
              "\t//CP: $" + str(comparison_stock_price), end="")

        try:
            if float(current_stock_price) >= float(comparison_stock_price) * float(1.003):
                print("\n", str(ticker), " is Worth Buying ")

                # Clear the previous stock prices if the stock is worth buying
                if ticker == self.stock_list[0]:
                    self.tick1_previous_stock_prices.clear()
                elif ticker == self.stock_list[1]:
                    self.tick2_previous_stock_prices.clear()
                elif ticker == self.stock_list[2]:
                    self.tick3_previous_stock_prices.clear()
                elif ticker == self.stock_list[3]:
                    self.tick4_previous_stock_prices.clear()
                elif ticker == self.stock_list[4]:
                    self.tick5_previous_stock_prices.clear()
                elif ticker == self.stock_list[5]:
                    self.tick6_previous_stock_prices.clear()
                elif ticker == self.stock_list[6]:
                    self.tick7_previous_stock_prices.clear()
                elif ticker == self.stock_list[7]:
                    self.tick8_previous_stock_prices.clear()

                return True, current_stock_price

        except TypeError as e:
            print(e)
        except ValueError as x:
            print(x)

    def evaluate_selling_potential(self, stock, buying_price):

        """ This will sell if the stock has gone up by 0.8%. It will also sell
        if the stock has gone down by 0.6% to stop losses """

        self.get_stock_info.get_yahoo_stock_page(stock)

        current_stock_price = self.get_stock_info.constantly_return_stock_price_on_page()

        print("\r//SELL// - Analysing:", stock, "Current Price: $" + str(current_stock_price),
              "\t//BP: $", str(buying_price), end="")

        try:
            if float(current_stock_price) >= float(buying_price) * float(1.008):
                print("\n", stock, "Has Made Enough Profit. Selling...")
                return True
            elif float(current_stock_price) <= float(buying_price) * float(0.994):
                print("\n", stock, "Has Tanked, Selling to Stop Losses")
                return True
        except TypeError:
            pass