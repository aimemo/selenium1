from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://ya.ru")
assert "Яндекс" in driver.title
elem = driver.find_element(By.ID, "text")
elem.clear()
elem.send_keys("Python")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.quit()