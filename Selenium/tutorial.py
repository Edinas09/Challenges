from selenium import webdriver
browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')
input_element = browser.find_element_by_css_selector('input[id="ipt1"]')
print(input_element)
input_element.send_keys('My First Automation')
button_element = browser.find_element_by_css_selector('button[name="butn1"]').click()