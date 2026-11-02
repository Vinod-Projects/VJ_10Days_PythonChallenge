from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

search_text = input("What would you like to search for? ")
driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, "q"))
)
search_box.send_keys(search_text)

input("Text entered. Press Enter to close Chrome.")
driver.quit()
