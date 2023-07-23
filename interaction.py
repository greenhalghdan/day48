import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_web_driver = Service(r"C:\Users\green\Downloads\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=chrome_web_driver, options=chrome_options)
# driver.maximize_window()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # article_count.click()
#
# all_portals = driver.find_element(By.LINK_TEXT("All portals"))
# all_portals.click()


# serach = driver.find_element(By.NAME, value="search")
# serach.send_keys("python")
# time.sleep(0.5)
# serach.send_keys(Keys.RETURN)

driver = webdriver.Chrome(service=chrome_web_driver, options=chrome_options)
driver.maximize_window()
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Daniel")
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Greenhalgh")
email = driver.find_element(By.NAME, value="email")
email.send_keys("test@email.com")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()

time.sleep(5)
