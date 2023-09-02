from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from config.config import Data
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def get_chrome_driver(headless=False):
    try:
        options = webdriver.ChromeOptions()
        # options.add_argument('--incognito')
        path = f"{BASE_DIR}/cd"
        options.add_argument(f"--user-data-dir={path}")
        options.add_argument("--log-level=3")
        options.add_argument('--no-sandbox')

        if headless:
            options.add_argument('--headless')

        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
        time.sleep(2)
        driver.get(Data.url)
        return driver
    except Exception as e:
        print(e)
        print('------------------- Generation the New Driver')
        get_chrome_driver()



def send_keys_with_action_chains(driver, xpath, text, wait_time, previouse_clear=False):
    element = WebDriverWait(driver, wait_time).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))

    action = ActionChains(driver)
    action.move_to_element(element).perform()
    if previouse_clear:
        element.clear()

    action.click().send_keys(text).perform()

def btn_click_with_action_chains(driver, xpath, wait_time=10):
    element = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))

    action = ActionChains(driver)
    action.move_to_element(element).perform()
    action.click(element).perform()

def execute_script_based_click(driver, xpath, timeout=60):
    el = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    driver.execute_script("arguments[0].click();", el)