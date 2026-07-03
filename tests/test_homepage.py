from utils.browser import launch_browser
from utils.config import BASE_URL
from utils.screenshot import capture

driver = launch_browser()

driver.get(BASE_URL)

print("Page Title:")
print(driver.title)

capture(driver, "homepage")

driver.quit()
