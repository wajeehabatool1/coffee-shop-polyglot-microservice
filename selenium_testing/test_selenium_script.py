import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode, comment out if you want to see the browser

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to your React app
driver.get("http://localhost:3000")  # Replace with your app's URL

try:
    # Test Registration
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
    
    name_input = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
    register_button = driver.find_element(By.XPATH, "//button[text()='Register']")

    name_input.send_keys("Test User")
    email_input.send_keys("testuser@example.com")
    register_button.click()

    # Wait for registration confirmation
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'bg-green-100')]")))
    print("Registration successful")

    # Test Order Placement
    name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your Name']")))
    coffee_type_select = driver.find_element(By.XPATH, "//select[option[text()='Latte']]")
    size_select = driver.find_element(By.XPATH, "//select[option[text()='Small']]")
    extras_input = driver.find_element(By.XPATH, "//input[@placeholder='Extras (comma-separated)']")
    place_order_button = driver.find_element(By.XPATH, "//button[text()='Place Order']")

    name_input.send_keys("Test User")
    coffee_type_select.send_keys("Cappuccino")
    size_select.send_keys("Medium")
    extras_input.send_keys("Extra shot, Whipped cream")
    place_order_button.click()

    # Wait for order confirmation
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'bg-green-100')]")))
    print("Order placed successfully")

except Exception as e:
    print(f"Test failed: {str(e)}")

finally:
    # Close the browser
    driver.quit()

print("All tests completed")
