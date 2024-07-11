from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get('file:///C:/Users/ADMIN/AppData/Local/Temp/7d68cb5e-af4c-4d5e-8266-dd6822fc6b3c_AutomationChallenge_2022.zip.b3c/QE-index.html')  # URL of the Home page



# Test 1
def test_1():
    wait.until(EC.presence_of_element_located((By.ID, 'inputEmail')))
    wait.until(EC.presence_of_element_located((By.ID, 'inputPassword')))
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
    driver.find_element(By.ID, 'inputEmail').send_keys('test@example.com')
    time.sleep(1)
    driver.find_element(By.ID, 'inputPassword').send_keys('password')
    time.sleep(1)



# Test 2
def test_2():
    list_items = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="test-2-div"]//ul[@class="list-group"]/li')))
    assert len(list_items) == 3
    assert 'List Item 2' in list_items[1].text
    badge_value = list_items[1].find_element(By.XPATH, './/span[@class="badge badge-pill badge-primary"]').text
    assert badge_value == '6'



# Test 3
def test_3():
    dropdown_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "dropdownMenuButton"))
    )
    time.sleep(1)
    
    # Assert the default selected option
    assert dropdown_button.text.strip() == "Option 1", "Default option not selected"
    time.sleep(1)
    
    # Click the dropdown to open the options
    dropdown_button.click()
    time.sleep(1)
    
    # Wait for the dropdown options to be visible
    option_to_select = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, '//a[@class="dropdown-item" and text()="Option 3"]'))
    )
    time.sleep(1)
    
    # Click the desired option
    option_to_select.click()
    time.sleep(1)
    
    # Verify that the selected option is now displayed on the button
    updated_dropdown_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "dropdownMenuButton"), "Option 3")
    )
    time.sleep(1)
    assert dropdown_button.text.strip() == "Option 3", "Option 3 was not selected correctly"



# Test 4
def test_4():
    button1 = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="test-4-div"]//button[1]')))
    button2 = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="test-4-div"]//button[2]')))
    assert button1.is_enabled()
    time.sleep(1)
    assert not button2.is_enabled()
    time.sleep(1)



# Test 5
def test_5():
    button = wait.until(EC.visibility_of_element_located((By.ID, 'test5-button')))
    button.click()
    success_message = wait.until(EC.visibility_of_element_located((By.ID, 'test5-alert')))
    assert success_message.is_displayed()
    assert not button.is_enabled()



# Test 6
def test_6():
    def get_grid_value(row, col):
        return driver.find_element(By.XPATH, f'//div[@id="test-6-div"]//tbody//tr[{row+1}]//td[{col+1}]').text
    assert get_grid_value(2, 2) == 'Ventosanzap'



# Running tests
try:
    test_1()
    print("Test 1 passed")
except Exception as e:
    print(f"Test 1 failed: {e}")

try:
    test_2()
    print("Test 2 passed")
except Exception as e:
    print(f"Test 2 failed: {e}")

try:
    test_3()
    print("Test 3 passed")
except Exception as e:
    print(f"Test 3 failed: {e}")

try:
    test_4()
    print("Test 4 passed")
except Exception as e:
    print(f"Test 4 failed: {e}")

try:
    test_5()
    print("Test 5 passed")
except Exception as e:
    print(f"Test 5 failed: {e}")

try:
    test_6()
    print("Test 6 passed")
except Exception as e:
    print(f"Test 6 failed: {e}")



# Teardown
driver.quit()
