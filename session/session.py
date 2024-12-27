from appium import webdriver
from appium.options.android import UiAutomator2Options

def start_session():
    # Options 객체 생성
    options = UiAutomator2Options()
    options.platformName = "Android"
    options.deviceName = "RFCM90EMGQW"
    options.appPackage = "com.nexon.fo4m"
    options.appActivity = "com.nexon.fo4m.MainActivity"
    options.noReset = True
    options.ensureWebviewsHavePages = True
    options.nativeWebScreenshot = True
    options.newCommandTimeout = 3600
    options.uiautomator2ServerInstallTimeout = 60000

    # WebDriver 초기화
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723",
        options=options
    )
    return driver
