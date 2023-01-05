from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
offers = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/a')
highlight(offers ,10, "blue", 5)
time.sleep(5)
offers.click()
Student_program = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/ul/li[1]/a')
highlight(Student_program,10, "blue", 5)
time.sleep(5)
Student_program.click()
time.sleep(5)
driver.back()
offers.click()
Startup_program = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/ul/li[2]/a')
highlight(Startup_program,10, "blue", 5)
time.sleep(5)
Startup_program.click()
time.sleep(5)
driver.back()
time.sleep(10)
offers = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/a').click()
#try: 
 #  offers.click() 
#except StaleElementReferenceException:
 #  offers = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/a').click()
college_program = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/ul/li[3]/a')
highlight(college_program,10, "blue", 5)
time.sleep(5)
college_program.click()
time.sleep(5)
driver.back()
time.sleep(5)
offers = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/a').click()
Incubator_program = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/ul/li[4]/a')
highlight(Incubator_program,10, "blue", 5)
time.sleep(5)
Incubator_program.click()
time.sleep(5)
driver.back()
offers = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/a').click()
Nonprofits_program = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/ul/li[5]/a')
highlight(Nonprofits_program,10, "blue", 5)
time.sleep(5)
Nonprofits_program.click()
time.sleep(5)
driver.back()
offers = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/a').click()
OSS_Contributors_Program = driver.find_element(By.XPATH,'//*[@id="navbarNavDropdown"]/ul[1]/li[2]/ul/li[6]/a')
highlight(OSS_Contributors_Program,10, "blue", 5)
time.sleep(5)
OSS_Contributors_Program.click()
time.sleep(5)
driver.back()
driver.quit