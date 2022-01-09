import requests
from bs4 import BeautifulSoup
from time import sleep
from email.message import EmailMessage
import smtplib, ssl



def wmcheck(url, desire, email):
    headers = {"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
				"accept-encoding":"gzip, deflate, br",
				"accept-language":"en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
				"upgrade-insecure-requests":"1",
				"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
    while True:

        product = requests.get(url,headers=headers) #get given url
        soup = BeautifulSoup(product.content,'lxml') 
        name = soup.find("h1").get_text().strip() #product name
        
        try:
            price = float(soup.find(itemprop="price").get_text().replace('$', '').replace(',', '').strip())

        except:
            price = "" #if there is no price of the product
            return 1
        try:
            if price <= desire:
                alert(name,desire,url,email)
                break #end loop once product has reached consumer desired price or is lower than it.

        except:
            #sometimes no price, if so would cause error
            pass
        break
        sleep(60*60*8) #checks price every 8 hours

def alert(name,desire,url,email):
    port = 465  # For SSL

    msg = EmailMessage()
    msg.set_content("Hi there,\n\nThe %s has reached %.2f or lower.\n\nHere is the link to the product:\n%s" % (name,desire,url))
    

    msg['Subject'] = "Sartaj's Price Alert!"
    msg['From'] = "sartajpricealerts@gmail.com"
    msg['To'] = email

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("sartajpricealerts@gmail.com", "pricealert123")
        server.send_message(msg)



