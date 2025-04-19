import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_valid_user(driver, config):
    login_page = LoginPage(driver)
    login_page.load(config["base_url"])
    login_page.login("myUsername", "myPassword")

    assert "dashboard" in driver.current_url.lower()
