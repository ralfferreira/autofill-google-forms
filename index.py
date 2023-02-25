import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


url = ""

driver = webdriver.Chrome('/home/ralf/Downloads/chromedriver/chromedriver')

driver.get(url);

fake = Faker()

def fill_form(name, email, phone):
    inputs = driver.find_elements(By.CSS_SELECTOR, ".whsOnd.zHQkBf")

    time.sleep(1)

    inputs_array = [
        name, email, phone
    ]

    for i in range(len(inputs)):
        inputs[i].clear()
        inputs[i].send_keys(inputs_array[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    submit.click()



count = 0

while True:
    # Verifique se o contador atingiu o valor 20
    if count == 20:
        break
    
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    fill_form(name, email, phone)

    count += 1
    print(f"Formulario preenchido")
    time.sleep(1)
    driver.refresh()


time.sleep(1)
driver(quit)