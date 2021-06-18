from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications":1})

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

username_field = driver.find_element_by_id('username')
username_field.click()
username_field.send_keys('edinas09@gmail.com')

password_field = driver.find_element_by_id('password')
password_field.click()
password_field.send_keys('')

login_btn = driver.find_element_by_class_name('login__form_action_container')

login_btn.click()



messaging_field = driver.find_elements_by_link_text("Messaging")[0].click()


try:
    messages = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".msg-conversations-container__conversations-list"))
    )
    print(messages.text)
except:
    driver.quit()


driver.quit()

