import requests
from bs4 import BeautifulSoup
from time import sleep
from alert import alert



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
        print(name)
        
        try:
            #price = float(soup.find(id="corePrice_feature_div").find_next("span").find_next("span").get_text().replace('$', '').replace(',', '').strip()) #price of product for amazon.ca
            price =soup.find(itemprop="price").get_text()

            #print(price)
        except:

            try:
                price = float(soup.find(id="price_inside_buybox").get_text().replace('$', '').replace(',', '').strip()) #price of product for amazon.com
            except:
                price = "" #if there is no price of the product
        print(price)
        try:
            if price <= desire:
                #alert(name,desire,url,email)
                break #end loop once product has reached consumer desired price or is lower than it.

        except:
            #sometimes no price, if so would cause error
            pass
        break
        sleep(60*60*8) #checks price every 8 hours

wmcheck("https://www.walmart.com/ip/Champion-Women-s-Plus-Mock-Neck-Zip-Up-Colorblock-Sherpa-Pullover/414028922?athcpid=414028922&athpgid=AthenaHomepageDesktop__gm__-1.0&athcgid=null&athznid=ItemCarousel_efadad11-5f2a-4eb7-9aae-5e76dcda3c48_items&athieid=null&athstid=CS020&athguid=y7AUAsnNDEsgcG4JMY3QDxhvLGsq_arwzvPi&athancid=null&athena=true&athbdg=L1700",5,"hery")