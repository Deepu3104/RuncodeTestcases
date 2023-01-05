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
Login_button = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[2]/li/a')
highlight(Login_button ,10, "blue", 5)
time.sleep(5)
Login_button.click()
Google_login = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/a[1]')
highlight(Google_login,10, "red", 5)
time.sleep(5)
Google_login.click()
Email = driver.find_element(By.XPATH,'//*[@id="identifierId"]') 
time.sleep(5)
highlight(Email,10, "green", 5)
time.sleep(5)
Email.send_keys("pradeep.mptesting@gmail.com")
Next = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span')
time.sleep(5)
highlight(Next,10,"red",5)
Next.click() 
time.sleep(5)
password = driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input') 
highlight(password,10, "blue", 5)
time.sleep(5)
password.send_keys("Mptesting")
Submit = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button').click()
time.sleep(5) 
profile_drop = driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li')
highlight(profile_drop,10,"blue",5)
time.sleep(5)
profile_drop.click()
time.sleep(5)
Signout_button = driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li/ul/li[3]/a')
highlight(Signout_button,10,"blue",5)
time.sleep(5)
#Signout_button.click()
driver.quit()

