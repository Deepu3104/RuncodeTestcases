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
Google_login = driver.find_element(By.XPATH,'/html/body/div/div/div/div/div/div/div/a[1]').click()
time.sleep(5)
Email = driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys("pradeep.mptesting@gmail.com") 
Next = driver.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click() 
time.sleep(5)
password = driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Mptesting")
Submit = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button').click()
time.sleep(5) 
profile_drop = driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li')
highlight(profile_drop,10,"blue",5)
time.sleep(5)
profile_drop.click()
teams = driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li/ul/li[1]/a')
highlight(teams,10,"blue",5)
teams.click()
time.sleep(5)
Edit_button = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div[2]/div[3]/button[1]')
highlight(Edit_button,10,"blue",5)
time.sleep(5)
Edit_button.click()
time.sleep(5)
Edit_Name = driver.find_element(By.XPATH,'//*[@id="edit_team_name_129"]')
highlight(Edit_Name,10,"blue",5)
time.sleep(5)
Edit_Name.clear()
time.sleep(5)
Edit_Name.send_keys("Testing1")
time.sleep(5)
Save_button = driver.find_element(By.XPATH,'//*[@id="edit_submit_129"]')
highlight(Save_button,10,"blue",5)
time.sleep(5)
Save_button.click()
driver.quit
