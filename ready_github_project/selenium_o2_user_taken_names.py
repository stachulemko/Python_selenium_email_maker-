from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


def register_and_check_email_availability(emails):

    driver = webdriver.Chrome()

    """EdgeService = Service(
        r"C:\\tools\\msedgedriver.exe")
    driver = webdriver.Edge(service=EdgeServsice)"""

    driver.get("https://1login.wp.pl/rejestracja?client_id=o2_poczta_o2_pl_nh&flow=registration&login_challenge=CkYKJDExZTJkN2EyYjgxOGU4Yjk4NDQyNmYyYjhmMDhkMzRiOGI4ZRCy59SqBhoYChJvMl9wb2N6dGFfbzJfcGxfbmgSAnYxEiC4M9tdpJM38y7xcdq5tQf5H9DJoPa6mwYHtKXbdr6N9Q&registrationFlow=newForced&registrationBrand=o2")

    driver.find_element(By.NAME, 'name').send_keys("Imie")
    driver.find_element(By.NAME, "lastName").send_keys("Nazwisko")
    driver.find_element(By.NAME, "sex").send_keys("M")
    driver.find_element(By.ID, "date").send_keys("6")
    select_month = driver.find_element(By.ID, "month")
    select = Select(select_month)
    select.select_by_value('2')

    driver.find_element(By.ID, "year").send_keys("1940")

    driver.find_element(By.ID, "login").send_keys(emails[0])
    
    time.sleep(8)
    x = driver.find_element(
        By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")
    print(x.tag_name)
    print(x.text)

    for email in emails[1:]:
        print(f"wstawiamy: {email}")
        driver.find_element(By.ID, "login").send_keys("")
        driver.find_element(By.ID, "login").clear()
        driver.find_element(By.ID, "login").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.ID, "login").send_keys(Keys.DELETE)
       
        print(f'login:{driver.find_element(By.ID, "login").text}')

   
        driver.find_element(By.ID, "login").send_keys(email)
    
        time.sleep(random.randint(1,2))
        
        x = driver.find_element(
            By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")

        if x.text == "Podany login jest już zajęty":
            with open('user_taken_names2.txt', 'a') as file:
                file.write(f"{email}")  
   
#print("asdasd")
print(len(sys.argv))
path=sys.argv[1]

print(path)
with open(path, 'r',encoding='utf-8') as file:
    email_to_check = file.readlines()
    register_and_check_email_availability(email_to_check)
print(path)
