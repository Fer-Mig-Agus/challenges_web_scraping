from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from rich import print
import pandas as pd
import time

def start_chrome():
    
    ruta=ChromeDriverManager().install()
    
    options=Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
    options.add_argument(f'user-agent={user_agent}')
    #options.add_argument('--headless')
    options.add_argument(
        "--start-maximized"
    ) 
    exp_opt = [
        "enable-automation", 
        "ignore-cerficate-errors",
        "enable-logging",
    ]
    options.add_experimental_option("excludeSwitches", exp_opt)
    s=Service(ruta)
    driver=webdriver.Chrome(
        service=s,options=options
    )
    
    return driver



    
def scraping_vea(url):
    list_products=[]
    
    for i in range(1,5):
    
        driver.get(f"{url}?page={i}")

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 0);")
        try:
            drinks=driver.find_elements(By.XPATH,"//div[contains(@class,'vtex-search-result-3-x-galleryItem--normal')]")
        except:
            drinks=[]
            
        
        if drinks and len(drinks)!=0:
            for drink in drinks:
                brand=drink.find_element(By.XPATH,'.//span[contains(@class,"vtex-product-summary-2-x-productBrandName")]').text
                description_product=drink.find_element(By.XPATH,".//span[contains(@class,'vtex-product-summary-2-x-brandName')]").text
                image=drink.find_element(By.XPATH,'.//img[contains(@class,"vtex-product-summary-2-x-image")]').get_attribute("src")
                
                list_products.append({
                    'brand':brand,
                    'description':description_product,
                    'image':image
                })
                
                print({
                    'brand':brand,
                    'description':description_product,
                    'image':image
                })
                
            
    
   
    return list_products
    
    







if __name__ == '__main__':
    
    url = "https://www.vea.com.ar/bebidas"
    driver=start_chrome()
    wait=WebDriverWait(driver,10)
    
    products=scraping_vea(url)
    if products and len(products)!=0:
        df=pd.DataFrame(products)
        df.to_excel('productsSelenim.xlsx',index=False,engine='openpyxl')
        print('Archivo de registro creado: productsSelenim.xlsx')
    else:
        print('Ocurrio un error')
    
    
    
 