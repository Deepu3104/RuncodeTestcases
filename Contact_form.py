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
Full_Name = driver.find_element(By.XPATH,'//*[@id="id_full_name"]') 
highlight(Full_Name ,10, "blue", 5)
time.sleep(5)
Full_Name.send_keys('Testing')
Email_Address = driver.find_element(By.XPATH,'//*[@id="id_email_address"]')
highlight(Email_Address ,10, "blue", 5)
Email_Address.send_keys('pradeep.mptesting@gmail.com')
Mobile_number = driver.find_element(By.XPATH,'//*[@id="id_mobile_number"]')
highlight(Mobile_number,10,"blue",5)
Mobile_number.send_keys('123457888779')
Message = driver.find_element(By.XPATH,'//*[@id="id_message"]')
highlight(Message,10,"blue",5)
Message.send_keys('Testing contact form by using automaction ')
Submit_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/form/button')
highlight(Submit_button,10,"blue",5)
Submit_button.click()  
time.sleep(5)
driver.quit