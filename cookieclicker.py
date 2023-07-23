import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_web_driver = Service(r"C:\Users\green\Downloads\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_web_driver)

driver.maximize_window()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, value="cookie")


def clickcookie():
    i = 0
    timeout = time.time() + 5
    while time.time() <= timeout:
        cookie.click()


def checkRewards(money):
    rewards = [
    driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b'),
    driver.find_element(By.CSS_SELECTOR, value="#buyPortal b"),
    driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b'),
    driver.find_element(By.CSS_SELECTOR, value="#buyShipment b"),
    driver.find_element(By.CSS_SELECTOR, value="#buyMine b"),
    driver.find_element(By.CSS_SELECTOR, value="#buyFactory b"),
    driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b"),
    driver.find_element(By.CSS_SELECTOR, value="#buyCursor b"),
    ]
    for reward in rewards:
        reward_detail = reward.text.split(" - ")
        reward1 = reward_detail[1].split(',')
        cost = ""
        for number in reward1:
            cost += number
        cost = int(cost)
        if cost < money:
            reward.click()
            money -= cost
            break
        else:

def currentCookies():
    money2 = driver.find_element(By.ID, value="money").text.split(",")
    cost = ""

    for i in money2:
        cost += i
    return int(cost)

playing = True

i = 0
timeout = time.time() + 30
while time.time() <= timeout:
    clickcookie()
    money = currentCookies()
    checkRewards(money)

cookies_per_second = driver.find_element(By.XPATH, value='//*[@id="cps"]')

print(f"your average {cookies_per_second.text}")