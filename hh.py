import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Set Chrome options to disable page load strategy
chrome_options = Options()
chrome_options.add_argument("--pageLoadStrategy=none")

# Set desired capabilities
capabilities = DesiredCapabilities().CHROME.copy()
capabilities['pageLoadStrategy'] = 'eager'

# Instantiate Chrome driver with the configured options and capabilities
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options,
                          desired_capabilities=capabilities)


def logic_start(a):
    driver.get("https://hh.ru")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div/div/div/div/div[5]/a').click()
    time.sleep(3)
    driver.find_element(By.NAME, 'login').send_keys(a)
    driver.find_element(By.XPATH,
                        '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div/div[2]/form/div[5]/button[1]/span').click()


def logik_cod(b):
    time.sleep(2)
    driver.find_element(By.XPATH,
                        '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div/div/div/div/form/div/div[3]/div/fieldset/input').send_keys(
        b)
    time.sleep(2)
    button = driver.find_element(By.CLASS_NAME, u"verification-submit")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()
