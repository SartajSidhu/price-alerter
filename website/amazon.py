import requests
from bs4 import BeautifulSoup
from time import sleep
from email.message import EmailMessage
import smtplib, ssl

def amazoncheck(url, desire, email):
    headers =({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    while True:

        product = requests.get(url,headers=headers) #get given url
        soup = BeautifulSoup(product.content,'lxml') 
        name = soup.find(id="productTitle").get_text().strip() #product name
        
        try:
            price = float(soup.find(id="corePrice_feature_div").find_next("span").find_next("span").get_text().replace('$', '').replace(',', '').strip()) #price of product for amazon.ca
        except:

            try:
                price = float(soup.find(id="price_inside_buybox").get_text().replace('$', '').replace(',', '').strip()) #price of product for amazon.com
            except:
                price = "" #if there is no price of the product
                return 1

        try:
            if price <= desire:
                alert(name,desire,url,email)
                break #end loop once product has reached consumer desired price or is lower than it.

        except:
            #sometimes no price so if would cause error
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
