import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"

INVALID_USER = "wrong_user"
INVALID_PASS = "wrong_pass"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def login(driver, username, password):
    driver.get(BASE_URL)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "user-name")))
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def test_login_valid_credentials(driver):
# Тест-1 Успешный логин
    login(driver, VALID_USER, VALID_PASS)
    WebDriverWait(driver, 5).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url


def test_login_invalid_credentials(driver):
# Тест-2 Неуспешный логин
    login(driver, INVALID_USER, INVALID_PASS)
    err = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert "Username and password do not match any user in this service" in err.text


def test_logout(driver):
# Тест -3 Выход
    login(driver, VALID_USER, VALID_PASS)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL


def test_add_to_cart_and_cart_page(driver):
# Тест -4 Добавление и отоброжение товара в корзине
    login(driver, VALID_USER, VALID_PASS)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button"))).click()
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_item")))
    items = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
    assert len(items) == 1


def test_remove_from_cart(driver):
# Тест -5 Удаление из корзины
    login(driver, VALID_USER, VALID_PASS)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button"))).click()
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart_item button"))).click()
    no_items = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
    assert len(no_items) == 0


def test_checkout_flow(driver):
# Тест -6 Заполнение информации о заказе
    login(driver, VALID_USER, VALID_PASS)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button"))).click()
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "first-name")))
    driver.find_element(By.ID, "first-name").send_keys("Pochoeva")
    driver.find_element(By.ID, "last-name").send_keys("Safia")
    driver.find_element(By.ID, "postal-code").send_keys("123")
    driver.find_element(By.ID, "continue").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    complete_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert "THANK YOU FOR YOUR ORDER" in complete_msg.text


def test_checkout_cancel(driver):
# Тест -7 Отмена заказа
    login(driver, VALID_USER, VALID_PASS)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".inventory_item button"))).click()
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "cancel"))).click()
    WebDriverWait(driver, 5).until(EC.url_contains("/cart.html"))
    assert "/cart.html" in driver.current_url
