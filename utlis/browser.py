from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.config import IMPLICIT_WAIT

def launch_browser():
    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()
    driver.implicitly_wait(IMPLICIT_WAIT)

    return driver
