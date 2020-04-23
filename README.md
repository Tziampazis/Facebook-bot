# Facebook-bot
This is a simple Facebook bot that can send messages based on a given name.
This implementation is based on Google Chrome. It can be altered into Firefox, etc.


INSTALLATION
------------

1) Install Python 3.x
2) Add Python to your Enviroment PATH
3) Download chromedirver from url: https://chromedriver.chromium.org/downloads
4) Extract the downloaded chromedriver 
* (The path where you extracted the chromedriver will be needed for the code) 
5) Change the code accordingly based on your facebook credentials and desired chat name.

YOU ARE READY TO GO!
--------------

LIMITATIONS

The code is written in the simplest form possible thus there exist some burriers and issues regarding 
the flow of the code. 

Namely:

1)The timer.wait() can be adjusted based on your internet speed
2)The chat is selected through the web-app bar. When a message is send it must not be interrupted by 
  other incoming messages, otherwise the code will continue spamming on the newly open window.
3)The chat given must be visible when the chat pop up is clicked.
