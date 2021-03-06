# GPU-Finder-BOT
BestBuy GPU Finder BOT - Built to help find GPU stock during Pandemic

Hello, I created a simple BOT for helping me find a new graphics card during the Pandemic since supply everywhere is basically non-existent.  It is a simple Python program that checks a BestBuy listting every second to see if the GPU/Item I am looking at is avalable.  If the button says "Sold-Out" it will keep running until it says "Add-Cart".  Once it says "Add-Cart" it will stop searching and send me and my friend a text message (Email to SMS) with a link to the BestBuy listing.  It doesn't buy it for us, it just notifies us so we can quickly try to get it since sometimes notifications are slow to come in (BestBuy doesn't have a notify option anyways though)

Requirements:
  Python
  Selenium - This is a webscraping software that you will need to install.  This link helped me link it up with pycharm: https://youtu.be/IYILCEV5j6s
  Chrome Driver - https://youtu.be/7R5n0sNSza8
  smtplib - This is what will send Text Messages via Email.  Helpful guide: https://gist.github.com/alexle/1294495
  
 Other Helpful Sources:
  https://youtu.be/3mRssb4AlqI
