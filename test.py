import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import telebot


options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--start-maximized')
options.add_argument("--window-size=1920,1080")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')

driver = webdriver.Chrome(options=options)
action = ActionChains(driver)

bot = telebot.TeleBot("6528485256:AAFr27qVMMB-A_Ig_YeX3DSK-kvWBr-TR3U")
chat_id = 479102451

url = ''



def retry(max_attempts, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            print(f"Function {func} failed after {max_attempts} attempts")
        return wrapper

    return decorator





def find_css(selector):
    return WebDriverWait(driver, 10).until(
        EC.((By.CSS_SELECTOR, selector)))


def find_xpath(selector):
    return WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, selector)))

driver.get('https://www.moskvaonline.ru/providers')
driver.execute_script("window.scrollBy(0,500)")
btn_prov = find_xpath('//img[@alt="Ростелеком"]/ancestor::div[@datatest="providers_provider_button"]/descendant::div[@datatest="providers_form_inspect_connect_tariff_button"]')
print('найден')
action.scroll_to_element(btn_prov).perform()
btn_prov.click()
current_number = find_xpath(
    '/html/body/div/div/div[4]/div/div/div/div[1]/form/div/div[1]/div/div[2]/div[2]/a')