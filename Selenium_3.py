# Selenium Tutorial #3
# Page navigating and clicking elements
# More videos on https://www.youtube.com/watch?v=Xjv1sY630Uc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/fcapdeville/Temporal/Python/Selenium/chromedriver_linux64/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(PATH, options=options)
driver.get("https://techwithtim.net")

# Search by comparison to text
link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )   # Locate an element by text
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )   # Locate an element by ID
    element.click()

    driver.back()      # Going back to the previous page
    driver.back()      # Going back to the previous page
    driver.forward()    # Going back to the next page

finally:
    driver.quit()
