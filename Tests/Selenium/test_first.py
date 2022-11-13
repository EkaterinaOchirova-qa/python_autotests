import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_open_browser():
    """
    Test case 1
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = "https://test.qa.studio"
    driver.get(url=url)

    element = driver.find_element(by=By.CSS_SELECTOR, value="[data-product_sku='J4W5ADY72']")
    element.click()


    css_button_selector = "[class='button checkout wc-forward razzi-button button-outline']"
    WebDriverWait(driver, timeout=3, poll_frequency=1).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_button_selector)))

    element = driver.find_element(by=By.CSS_SELECTOR, value=css_button_selector)
    element.click()



    


    assert True, ""