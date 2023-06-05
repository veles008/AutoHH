from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Set Chrome options to disable page load strategy
chrome_options = Options()
chrome_options.add_argument("--pageLoadStrategy=none")

# Set desired capabilities
capabilities = DesiredCapabilities().CHROME.copy()
capabilities['pageLoadStrategy'] = 'eager'

# Instantiate Chrome driver with the configured options and capabilities
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options, desired_capabilities=capabilities)

def logic_start():
    driver.get("https://hh.ru")
    driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[2]/div/div/div/div/div[5]/a').click()
