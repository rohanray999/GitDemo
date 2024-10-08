import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def browserSetup(request):
    global driver
    browser = request.config.getoption("--browser_name")
    if browser == "chrome":
        service_obj = Service("/Users/sagarrayamajhi/Downloads/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser == "safari":
        driver = webdriver.Safari()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.param item:"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):

    driver.get_screenshot_as_file(name)
    print("hello222")
    print("First Hello")
    print("Second Hello")
<<<<<<< HEAD
    print("New ")
    print("New test")
    print("Tasty")
=======
    print("Hello People")
    print("ready to deploy")
    print("ready Hello")
>>>>>>> development
