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
password = driver.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input').send_keys("Mptesting") 
time.sleep(5)
Submit = driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button').click()
time.sleep(5) 
Teams_dropdown = driver.find_element(By.XPATH,'//*[@id="dropdownMenuButton1"]')
highlight(Teams_dropdown,10,"blue",5)
time.sleep(5)
Teams_dropdown.click()
Teams = driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div/div[1]/section/div/ul/li/a')
highlight(Teams,10,"blue",5)
time.sleep(5)
Teams.click()
time.sleep(5)
Active_tab =driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div/div[2]/ul/li[1]/a')
highlight(Active_tab,10,"blue",5)
time.sleep(5)
Shared_tab =driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div/div[2]/ul/li[2]/a')
highlight(Shared_tab,10,"blue",5)
time.sleep(5)
Deleted_tab =driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div/div[2]/ul/li[3]/a')
highlight(Deleted_tab,10,"blue",5)
New_workspace = driver.find_element(By.XPATH,'/html/body/section/div/div/div[2]/div/div[2]/a')
highlight(New_workspace,10,"blue",5)
time.sleep(5)
New_workspace.click()
driver.quit



