import pytest
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
        # Launch Chrome browser and open GUVI website.
        # Close browser after test execution.
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    yield driver
    driver.quit()

def test_dynamic_xpath_items(driver):

    # Validate dynamic XPath for all header menu items.
    # Indexing is used because both desktop and mobile versions exist in the DOM
    live_class = driver.find_element(By.XPATH,"(//p[normalize-space()='LIVE Classes'])[1]")
    course = driver.find_element(By.XPATH,"(//header//p[normalize-space()='Courses'])[1]")
    practice = driver.find_element(By.XPATH,"(//header//p[normalize-space()='Practice'])[1]")
    resource = driver.find_element(By.XPATH,"(//header//p[normalize-space()='Resources'])[1]")
    ourproduct = driver.find_element(By.XPATH,"(//header//p[normalize-space()='Our Products'])[1]")
    login_bt = driver.find_element(By.XPATH,"(//button[@id='login-btn'])[1]")
    sign_up = driver.find_element(By.XPATH,"(//header//button[normalize-space()='Sign up'])[1]")

    assert live_class.is_displayed()
    assert course.is_displayed()
    assert practice.is_displayed()
    assert resource.is_displayed()
    assert ourproduct.is_displayed()
    assert login_bt.is_displayed()
    assert sign_up.is_displayed()

def test_xpath_operations(driver):
    """
       Validate Relative XPath operations:
       Parent, Child, Sibling and Parent of href element
       """

    # Base element: Courses menu
    courses = driver.find_element(
        By.XPATH,"(//header//p[normalize-space()='Courses'])[1]"
    )
    # Parent element
    parent = driver.find_element(
        By.XPATH,
        "(//header//p[normalize-space()='Courses'])[1]/parent::div"
    )

    assert parent.is_displayed()

    # Child element (first child of parent)
    child = driver.find_element(
        By.XPATH,"(//header//p[normalize-space()='Courses'])[1]/parent::div/child::*[1]"
    )

    assert child.is_displayed()

    # Following sibling (Practice)
    follow_sibling = driver.find_element(
        By.XPATH,
        "(//header//p[normalize-space()='Courses'])[1]"
        "/ancestor::div[contains(@class,'group')]"
        "/following-sibling::div[1]"
    )

    assert follow_sibling is not None

    # Preceding sibling (LIVE Classes)
    precede_sib = driver.find_element(
        By.XPATH,
        "(//header//p[normalize-space()='Courses'])[1]"
        "/ancestor::div[contains(@class,'group')]"
        "/preceding-sibling::div[1]"
    )

    assert precede_sib is not None

    # Parent of element having href attribute
    href_parent = driver.find_element(
        By.XPATH,
        "(//a[@href])[1]/parent::*"
    )
    assert href_parent is not None