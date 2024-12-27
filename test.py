

def send_message(driver, text):
    try:
        # 예: 특정 요소 찾기 및 클릭
        element = driver.find_element("xpath", '//android.widget.TextView[@content-desc="다음"]')
        element.click()

        # 메시지 입력 예제
        input_box = driver.find_element("id", "com.nexon.fo4m:id/message_input")
        input_box.send_keys(text)

        # 전송 버튼 클릭 예제
        send_button = driver.find_element("id", "com.nexon.fo4m:id/send_button")
        send_button.click()
    except Exception as e:
        print(f"Failed to send message: {e}")
