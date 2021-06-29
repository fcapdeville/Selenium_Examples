# Selenium Tutorial #4
# ActionChains and automatic cookie clicker (click repeatedly)
# More videos on https://www.youtube.com/watch?v=Xjv1sY630Uc

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "/home/fcapdeville/Temporal/Python/Selenium/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(50):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

driver.quit()
