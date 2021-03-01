# Trading 212 Bot
This is a rudimentary stock terminal trading robot that uses selenium and python. The code here is very basic/sloppy so I would recommend using the code as an idea/base of how you could implement a more sophisticated bot, rather than as it presents itself.

This program will automatically find stock prices using Yahoo Finance and trade the given stock depending on certain conditions that are set/amended if you change the code in the strategies.py file.

This uses the demo version of the Trading212 platform. Due to the nature of websites changing and Trading212 not having an official API this stock trading robot is likely not to function if any HTML code in the future is altered in any way. 

Make sure you have gecko driver in the right path(adjust the 'PATH' in both get_stock_price.py/tradebot.py) and use the run.py to set the create the class and set the conditions to run the bot.
