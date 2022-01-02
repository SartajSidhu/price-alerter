import requests
from bs4 import BeautifulSoup
from time import sleep
from .alert import alert


def amazoncheck(url, desire):
    headerz =({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
    while True:

        product = requests.get(url,headers=headerz) #get given url
        soup = BeautifulSoup(product.content,'lxml') 
        name = soup.find(id="productTitle").get_text().strip() #product name
    
        try:
            price = float(soup.find(id='priceblock_saleprice').get_text().replace('$', '').replace(',', '').strip()) #price of product
            
        except:
            price = '' #exception for no price
        print(price)
        try:
            if price <= desire:
                #alert(name,desire,url)
                break #end loop once product has reached consumer desired price or is lower than it.

        except:
            #sometimes no price so if would cause error
            pass
        break
        #sleep(60*60*8) #checks price every 8 hours

amazoncheck("https://www.amazon.ca/Sony-WH-1000XM4-Canceling-Headphones-WH1000XM4/dp/B0863TXGM3?ref_=Oct_DLandingS_D_b5c11b03_60&smid=A3DWYIK6Y9EEQB&th=1",12)



