import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CHR_Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FF_Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def chrome_browser():
    chrome_options = CHR_Options()
    chrome_options.add_argument("--disable-extensions")
    # Uncomment 14 line for headless mode.
    # chrome_options.add_argument("--headless")
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Chrome(
        ChromeDriverManager().install(),
        desired_capabilities=caps,
        options=chrome_options,
    )
    yield driver
    driver.find_element_by_tag_name("body").screenshot("TestFullPage.png")
    driver.quit()


@pytest.fixture(scope="session")
def firefox_browser():
    firefox_options = FF_Options()
    # Change firefox_options.headless = True for headless mode.
    firefox_options.headless = False
    caps = DesiredCapabilities().FIREFOX
    caps["pageLoadStrategy"] = "eager"
    driver = webdriver.Firefox(
        desired_capabilities=caps,
        options=firefox_options,
        executable_path=r"D:\Dev\cbrf\geckodriver.exe",
    )
    yield driver
    driver.find_element_by_tag_name("body").screenshot("TestFullPage.png")
    driver.quit()
