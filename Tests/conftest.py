import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()