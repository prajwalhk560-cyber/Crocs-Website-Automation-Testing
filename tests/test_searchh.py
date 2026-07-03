from selenium.webdriver.common.by import By

from utils.browser import launch_browser
from utils.config import BASE_URL
from utils.helper import pause

driver = launch_browser()

driver.get(BASE_URL)

search = driver.find_element(By.NAME, "q")

search.send_keys("Classic Clog")

pause(3)

driver.quit()