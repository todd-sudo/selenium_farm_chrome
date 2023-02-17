import os
import time
import random

from selenium import webdriver


def get_web_driver_firefox():
    capabilities = {
        "browserName": "chrome",
        "version": "90.0",
        "enableVNC": True,
        "enableVideo": False
    }

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444/wd/hub",
        desired_capabilities=capabilities
    )
    return driver


def main():
    driver = get_web_driver_firefox()
    driver.get("https://eapteka.ru")
    time.sleep(4)
    data = driver.page_source
    with open("data.html", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
