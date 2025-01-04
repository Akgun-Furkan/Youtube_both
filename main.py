from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
"""import os

user_data_path = "C:/Users/agnfu/AppData/Local/Google/Chrome/User Data/"
profiles = [name for name in os.listdir(user_data_path) if os.path.isdir(os.path.join(user_data_path, name))]
print("Mevcut profiller:", profiles)

"""
# ChromeDriver yolu
chromedriver_path = r"C:\Users\agnfu\OneDrive\Masaüstü\chromedriver-win64\chromedriver-win64/chromedriver.exe"

# Kullanmak istediğiniz profilin adını girin
profile_name = "Volley"  # Örneğin: "Default" ya da "Profile 2"

# Chrome ayarları
options = webdriver.ChromeOptions()
profile_path =f"C:/Users/agnfu/AppData/Local/Google/Chrome/User Data/{profile_name}"

options.add_argument(f"user-data-dir={profile_path}")
options.add_argument("--window-size=1920,1080")  # Tarayıcı boyutu

# Tarayıcıyı başlat
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # YouTube'u aç
    driver.get("https://www.youtube.com/@afskvedit/shorts")

    # Gerekirse sayfanın tamamen yüklenmesini bekle
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("YouTube başarıyla açıldı.")

    # Gerekirse biraz bekle
    sleep(3)
    one_video_path=driver.find_element(By.XPATH,"//*[@id='content']/ytm-shorts-lockup-view-model-v2/ytm-shorts-lockup-view-model/a/div/img")
    one_video_path.click()
    actions = ActionChains(driver)
    sleep(2)
    for i in range(0,101):

        actions.send_keys(Keys.ARROW_DOWN).perform()
        sleep(20)


finally:
    # Tarayıcıyı kapatmak için
    driver.quit()
