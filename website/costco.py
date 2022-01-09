import requests
from bs4 import BeautifulSoup
from time import sleep
from alert import alert


def costcocheck(url, desire, email):
    headers =({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    while True:
        print("loop")
        product = requests.get(url,headers=headers) #get given url
        print("reach")
        soup = BeautifulSoup(product.content,'lxml') 
        name = soup.find(itemprop="name").get_text().strip() #product name
        
        try:
            price = soup.find(id="pull-right-price")#.find_next().get_text().replace('$', '').replace(',', '').strip()) #price of product for costco.ca
        except:

            try:
                price = float(soup.find(id="price_inside_buybox").get_text().replace('$', '').replace(',', '').strip()) #price of product for amazon.com
            except:
                price = "fail" #if there is no price of the product
        print(price)
        try:
            if price <= desire:
                break#alert(name,desire,url,email)
                 #end loop once product has reached consumer desired price or is lower than it.
            break
        except:
            #sometimes no price so if would cause error
            pass
        print("here")
        break
        sleep(60*60*8) #checks price every 8 hours

print("hey")
costcocheck("https://www.costco.ca/lg-24-in.-stainless-steel-front-control-dishwasher-with-quadwash-and-easyrack-plus.product.100773829.html",700,"hey")


