import os
from datetime import datetime

def capture(driver, name):

    folder = "screenshots"

    os.makedirs(folder, exist_ok=True)

    filename = datetime.now().strftime("%Y%m%d_%H%M%S")

    driver.save_screenshot(
        f"{folder}/{name}_{filename}.png"
    )
