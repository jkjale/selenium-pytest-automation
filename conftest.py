import pytest
import yaml
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="function")
def driver(config):
    if config["browser"] == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    else:
        raise ValueError(f"Unsupported browser: {config['browser']}")
    driver.maximize_window()
    yield driver
    driver.quit()
