import smtplib
import time
from selenium import webdriver
#Remember you must install selenium and chrome driver.  Check readme for help
PATH = "C:\\Users\\(Path_to_where_you_saved_your_chrome_driver)\\chromedriver.exe"

browser = webdriver.Chrome(PATH)

browser.get('Link to the BestBuy listing')



buyButton = False

numRefresh = 1


while not buyButton:
    try:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled") #"btn-disabled" can sometimes change so to find the new name if it does change is find the button using inspect element in the browser
        print("Button(s) arent ready yet -- Refrsh count: " + str(numRefresh))

        numRefresh += 1
        time.sleep(1)
        browser.refresh()


    except:

        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")  #"btn-primary" can sometimes change so to find the new name if it does change is find the button using inspect element in the browser
        print("Button was clicked. :)")

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login('YourEmailAddress@gmail.com', 'YourPassword')
        # Send text message through SMS gateway of destination number

        from_mail = 'YourEmailAddress@gmail.com'  #I believe it needs to be Gmail
        
        # Use sms gateway provided by mobile carrier:
        # at&t:     number@mms.att.net
        # t-mobile: number@tmomail.net
        # verizon:  number@vtext.com
        # sprint:   number@page.nextel.com
        to = 'PhoneNumberToBeSentTo@tmomail.net'    #Example 1234567891@mms.att.net
        body = 'Link to the BestBuy listing'
        message = ("From: %s\r\n" % from_mail + "To: %s\r\n" % to + "Subject: %s\r\n" % '' + "\r\n" + body)
        

        server.sendmail(from_mail, to, message)

        print("Messages sent!")

        addToCartBtn.click()  #This adds the item to your cart
        buyButton = True
