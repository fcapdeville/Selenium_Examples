# Selenium Tutorial #1
# Can open a web page

from selenium import webdriver

PATH = "/home/fcapdeville/Temporal/Python/Selenium/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com.ar") # Open the page

print(driver.title)

driver.close()                          # Close the tag
driver.quit()                           # Close the window

# More videos on https://www.youtube.com/watch?v=Xjv1sY630Uc
