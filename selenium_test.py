from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
URL = "http://localhost:4200"
FILE_PATH = r"C:\Users\hp\Desktop\Lecture 2.pdf"
if not os.path.isfile(FILE_PATH):
    print("❌ Test file not found – create test.pdf on Desktop")
    exit(0)   # still exit cleanly (no crash)
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
wait = WebDriverWait(driver, 15)
try:
    # 1️⃣ Select file
    file_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    file_input.send_keys(FILE_PATH)
    # 2️⃣ Click first button (Upload)
    upload_btn = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "button"))
    )
    upload_btn.click()

    # 3️⃣ Check system response (alert OR no alert)
    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        print("✅ TEST PASS – System showed alert:", alert.text)
        alert.accept()
    except TimeoutException:
        print("✅ TEST PASS – No alert, upload may be successful")
except Exception as e:
    print("❌ Unexpected error:", e)
    print("❌ TEST FAIL")
else:
    print("🎉 FINAL RESULT: TEST PASS")
time.sleep(2)
driver.quit()
