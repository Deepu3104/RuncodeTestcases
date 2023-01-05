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
contact = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[6]/a').click()
time.sleep(5)
Discord_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[3]/p[1]/a') 
highlight(Discord_button ,10, "red", 5)
time.sleep(5)
Discord_button.click()
time.sleep(5)
driver.quit