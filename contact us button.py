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
ContactUs_button  = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div/section/div/div[3]/section/div/div/div[12]/a')
driver.execute_script("arguments[0].scrollIntoView();", ContactUs_button)
#location = ContactUs_button.location
#y_cor = location["y"]
#driver.execute_script("window.scrollTo(0,"+str(y_cor)+" )") 
highlight(ContactUs_button ,10, "red", 5)
time.sleep(5)
ContactUs_button.click()
time.sleep(5)
driver.quit