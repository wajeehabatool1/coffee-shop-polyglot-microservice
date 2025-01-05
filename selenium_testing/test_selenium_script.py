import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode

def wait_and_find_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

try:
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)  # Set implicit wait

    # Open the application
    driver.get("http://34.47.194.60:3000")
    logger.info("Navigated to http://34.47.194.60:3000")

    # Test Registration Flow
    # Click Register button
    register_button = wait_and_find_element(driver, By.XPATH, "//button[contains(text(), 'Register Yourself')]")
    register_button.click()
    logger.info("Clicked on 'Register Yourself' button")

    # Fill registration form
    name_input = wait_and_find_element(driver, By.XPATH, "//input[@placeholder='Name']")
    email_input = wait_and_find_element(driver, By.XPATH, "//input[@placeholder='Email']")
    
    name_input.send_keys("John Doe")
    email_input.send_keys("johndoe@example.com")
    logger.info("Entered registration details")

    # Submit registration
    register_submit = wait_and_find_element(driver, By.XPATH, "//button[text()='Register']")
    register_submit.click()
    logger.info("Submitted registration form")

    # Wait for and verify registration success message
    success_message = wait_and_find_element(
        driver, 
        By.XPATH, 
        "//div[contains(@class, 'bg-green-100') and contains(text(), 'Registration Successful')]"
    )
    assert "Registration Successful" in success_message.text
    logger.info("Registration success message verified")

    # Test Order Flow
    # Click Order button
    order_button = wait_and_find_element(driver, By.XPATH, "//button[contains(text(), 'Order Your Coffee')]")
    order_button.click()
    logger.info("Clicked on 'Order Your Coffee' button")

    # Fill order form
    name_input = wait_and_find_element(driver, By.XPATH, "//input[@placeholder='Your Name']")
    name_input.clear()
    name_input.send_keys("John Doe")

    # Handle dropdowns using Select class
    coffee_type_select = Select(wait_and_find_element(driver, By.XPATH, "//select[contains(@class, 'border-gray-300')]"))
    coffee_type_select.select_by_visible_text("Cappuccino")

    size_select = Select(wait_and_find_element(driver, By.XPATH, "//select[contains(@class, 'border-gray-300')][2]"))
    size_select.select_by_visible_text("Medium")

    extras_input = wait_and_find_element(driver, By.XPATH, "//input[@placeholder='Extras (comma-separated)']")
    extras_input.send_keys("Extra shot, Almond milk")
    logger.info("Entered order details")

    # Submit order
    order_submit = wait_and_find_element(driver, By.XPATH, "//button[text()='Place Order']")
    order_submit.click()
    logger.info("Submitted order form")

    # Wait for and verify order success message
    order_success = wait_and_find_element(
        driver, 
        By.XPATH, 
        "//div[contains(@class, 'bg-green-100') and contains(text(), 'Order Placed Successfully')]"
    )
    assert "Order Placed Successfully" in order_success.text
    logger.info("Order success message verified")

except Exception as e:
    logger.error(f"Test failed with error: {e}")
    raise

finally:
    # Clean up
    if 'driver' in locals():
        driver.quit()
        logger.info("Browser closed")
