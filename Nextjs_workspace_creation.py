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
Login_button = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[2]/li/a').click()
time.sleep(5)
Google_login = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/a[1]').click()
time.sleep(5)
Email = driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys("pradeep.mptesting@gmail.com") 
time.sleep(5)
Next = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click() 
time.sleep(5)
password = driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input') .send_keys("Mptesting")
Submit = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button').click()
time.sleep(5) 
New_workspace = driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div/div[2]/a').click()
time.sleep(5)
Template_button = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div[2]/div[1]/div[1]/div/a')
highlight(Template_button,10,"blue",5)
Nextjs_workspace = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div[2]/div[2]/div/div[6]')
highlight(Nextjs_workspace,10,"blue",5)
Nextjs_workspace.click()
time.sleep(30)
driver.quit
