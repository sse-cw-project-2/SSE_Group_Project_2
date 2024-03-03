from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# Path to your WebDriver executable (change the path as needed)
# If the WebDriver executable is in your PATH, you can omit this.

# Initialize the WebDriver (this example uses Chrome)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the web application
    driver.get("http://localhost:5000")
    # Optionally, wait for the page to load or for specific elements to become available
    # This example waits up to 10 seconds for the page title to be available
    driver.implicitly_wait(10)

    # Check the title of the page
    assert "Home" in driver.title

    # Perform additional tests, such as finding elements or interacting with the page
    # For example, to find an element by its ID and enter text:
    # element = driver.find_element(By.ID, "yourElementId")
    # element.send_keys("some text")

    print("Test passed: Page title is as expected.")
except AssertionError:
    print("Test failed: Page title is not as expected.")
except WebDriverException:
    print("Test failed: WebDriver error occurred. Is Flask running?")
finally:
    # Close the browser window
    driver.quit()
