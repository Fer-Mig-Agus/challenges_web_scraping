from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
def start_chrome():
    #url = "https://www.vea.com.ar/bebidas?page=1"
    
    ruta=ChromeDriverManager().install()
    
    options=Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--headless')
    s=Service(ruta)
    driver=webdriver.Chrome(
        service=s,options=options
    )
    
    return driver

    
    
    
    
def scraping_vea(driver,url):
    
    driver.get(f"{url}?page=1")
    print(driver)
    


















if __name__ == '__main__':
    
    url = "https://www.vea.com.ar/bebidas"
    driver=start_chrome()
    wait=WebDriverWait(driver,10)
    products=scraping_vea(driver,url)
    
    
 