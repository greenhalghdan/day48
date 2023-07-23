from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By

chrome_web_driver = Service(r"C:\Users\green\Downloads\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_web_driver)

# driver.get("https://www.amazon.co.uk/Logitech-Mechanical-Wireless-Illuminated-Bluetooth/dp/B07W6JM8BR/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=Read9&content-id=amzn1.sym.6aea875e-359f-49f3-864f-cff62d586b6a%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=6aea875e-359f-49f3-864f-cff62d586b6a&pf_rd_r=B3TK3YZQ9F1F0MW6XD3P&pd_rd_wg=ZmdVn&pd_rd_r=a6902ba4-3efe-40b2-b4e7-10ab29eccd9a&pd_rd_i=B07W6JM8BR")
#
# #driver.findElement(by=By.className("a-price-whole"))
# test = driver.find_element(by=By.CLASS_NAME, value="a-price")
# print(test.text)


#driver.close() # closes single tab
# driver.quit() # closes entire browser

driver.get("https://www.python.org")

# python = driver.find_element(By.NAME, value="q")
# print(python.get_attribute("placeholder"))
#
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
#
# print(doc_link.text)
#
# bug_link = driver.find_element(By.XPATH, value=('//*[@id="site-map"]/div[2]/div/ul/li[3]/a'))
# print(bug_link.text)
#
# driver.find_elements()

#events = driver.find_elements(By.CLASS_NAME, value="menu li")
upcoming_events = {}
events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
for event in events:
    dates = event.find_elements(By.TAG_NAME, value="time") #{event.find_element(By.TAG_NAME, value="a").text}')
    es = event.find_elements(By.TAG_NAME, value="a")
    date_value = []
    event_name = []
    for date in dates:
        date_value.append(date.text)
    for e in es:
        event_name.append(e.text)

    i = 0 #len(date_value)
    while i < len(date_value):
        upcoming_events[i] = {"date": date_value[i - 1], "event": event_name[i - 1] }
        i = i + 1
    print(upcoming_events)
driver.quit()