import pytest
import os
from selenium_ui_test_tool import create_driver

@pytest.fixture(scope="function")
def driver():
    """
    Standard fixture to create a driver instance.
    """
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    """
    Returns the base URL. Can be overridden by environment variable or config.
    """
    return os.getenv("BASE_URL", "https://example.com")
