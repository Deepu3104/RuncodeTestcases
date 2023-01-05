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
Github_button = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div[2]/div[1]/div[2]')
time.sleep(5)
highlight(Github_button,10,"red",5)
Github_button.click()
time.sleep(5)
Github_login = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/a[2]')
highlight(Github_login,10, "red", 5)
time.sleep(5)
Github_login.click()
Email = driver.find_element(By.XPATH,'//*[@id="login_field"]').send_keys("pradeep.mptesting@gmail.com") 
time.sleep(5)
password = driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("Mptesting@7") 
highlight(password,10, "blue", 5)
Submit = driver.find_element(By.XPATH,'//*[@id="login"]/div[3]/form/div/input[11]').click()
time.sleep(5) 
authorize_button = driver.find_element(By.XPATH,'//*[@id="js-oauth-authorize-btn"]').click()
time.sleep(5)
Organizations = driver.find_element(By.XPATH,'//*[@id="select-form"]/select')
highlight(Organizations,10,"blue",5)
Repo = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div[2]/div[2]/div[2]')
highlight(Repo,10,"blue",5)
Launch_VS_code = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div[2]/div[2]/div[2]/div[3]/div/a[1]')
highlight(Launch_VS_code,10,"blue",5)
time.sleep(5)
Launch_VS_code.click()
time.sleep(30)




