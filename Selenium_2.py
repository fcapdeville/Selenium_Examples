# Selenium Tutorial #2
# Open a page, search something, get the info and show it on screen on python program
# More videos on https://www.youtube.com/watch?v=Xjv1sY630Uc

# Categories to look:
# 1 ==> ID
# 2 ==> Name              / Not necessary unique
# 3 ==> Class (less used) / Not necessary unique

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/fcapdeville/Temporal/Python/Selenium/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element_by_name("s")                   # Search for the object with the name "s"
search.send_keys("test")                                    # Write "test" in it
search.send_keys(Keys.RETURN)                               # Write enter in the element

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)

finally:
    driver.quit()
