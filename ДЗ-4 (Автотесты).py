from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Test Three

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(1)
username = driver.find_element(By.ID, "user-name")
username.send_keys("problem_user")
time.sleep(1)
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")
time.sleep(1)
login_btn = driver.find_element(By.CSS_SELECTOR, "input#login-button")
login_btn.click()

time.sleep(5)
driver.quit()

# Test Four
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(1)
username = driver.find_element(By.ID, "user-name")
username.send_keys("performance_glitch_user")
time.sleep(1)
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")
time.sleep(1)
login_btn = driver.find_element(By.CSS_SELECTOR, "input#login-button")
login_btn.click()

time.sleep(5)
driver.quit()

# Test Five

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(1)
username = driver.find_element(By.ID, "user-name")
username.send_keys("error_user")
time.sleep(1)
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")
time.sleep(1)
login_btn = driver.find_element(By.CSS_SELECTOR, "input#login-button")
login_btn.click()

time.sleep(5)
driver.quit()

# Test Six

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(1)
username = driver.find_element(By.ID, "user-name")
username.send_keys("visual_user")
time.sleep(1)
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")
time.sleep(1)
login_btn = driver.find_element(By.CSS_SELECTOR, "input#login-button")
login_btn.click()

time.sleep(5)
driver.quit()

# Браузер Microsoft

driver = webdriver.Edge ()
driver.get("https://www.saucedemo.com/")
time.sleep(1)
username = driver.find_element(By.ID, "user-name")
username.send_keys("visual_user")
time.sleep(1)
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")
time.sleep(1)
login_btn = driver.find_element(By.CSS_SELECTOR, "input#login-button")
login_btn.click()

time.sleep(5)
driver.quit()

# Поменять цвет кнопки

driver = webdriver.Chrome ()
driver.get("https://www.saucedemo.com/")
time.sleep(1)
username = driver.find_element(By.ID, "user-name")
username.send_keys("visual_user")
time.sleep(1)
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")
time.sleep(1)
driver.execute_script("""
    document.getElementById("login-button").addEventListener("click", function(event) {
        event.preventDefault();
        this.style.backgroundColor = "red";
    });
""")
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()
time.sleep(1)
new_color = "rgb(226, 35, 26)"
print(new_color)
time.sleep(5)
driver.quit()






