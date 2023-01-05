from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def highlight(element,effect_time,color, border):
    
    driver = element._parent 
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: "+str(border)+"px solid "+color+";")
    time.sleep(effect_time)
    apply_style(original_style)
driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://runcode.io/')
driver.maximize_window ()
time.sleep(5)
pricing = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[3]/a').click()
time.sleep(5)
Subscribe_button = driver.find_element(By.XPATH,'//*[@id="__next"]/section[1]/div/div/div/section/div/section/div[2]/div/div[1]/div/div/div/div[3]/a')
highlight(Subscribe_button ,10, "red", 5)
time.sleep(5)
Subscribe_button.click()
time.sleep(5)
driver.quit