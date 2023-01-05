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
blog = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[5]/a').click()
time.sleep(5)
Introduction = driver.find_element(By.XPATH,'//*[@id="__next"]/div/section/div/div/div/div[1]/div/div/div/div[2]/a')
highlight(Introduction ,10, "blue", 5)
time.sleep(5)
Introduction.click()
time.sleep(5)
driver.quit

