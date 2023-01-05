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
Add_teams_button = driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/button')
highlight(Add_teams_button,10,"blue",5)
Add_teams_button.click()
time.sleep(5)
Cross_symbol = driver.find_element(By.XPATH,'//*[@id="edit_team_129"]/div/div/div/button')
highlight(Cross_symbol,10,"blue",5)
time.sleep(5)
Cross_symbol.click()
driver.quit
