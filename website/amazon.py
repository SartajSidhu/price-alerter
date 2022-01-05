import requests
from bs4 import BeautifulSoup
from time import sleep
from alert import alert


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
        print(price)
        try:
            if price <= desire:
                alert(name,desire,url,email)
                break #end loop once product has reached consumer desired price or is lower than it.

        except:
            #sometimes no price so if would cause error
            pass
        break
        sleep(60*60*8) #checks price every 8 hours





