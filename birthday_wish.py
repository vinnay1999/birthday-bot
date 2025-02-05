import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

# Google Sheets setup
def get_birthday_names():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    
    sheet = client.open('Your Google Sheet Name').sheet1
    data = sheet.get_all_records()
    
    today = datetime.today().strftime('%m-%d')
    
    birthday_names = [row['Name'] for row in data if row['Birthday'].strftime('%m-%d') == today]
    
    return birthday_names

# WhatsApp Automation using Selenium
def send_whatsapp_message(names):
    if not names:
        print("No birthdays today!")
        return

    message = f"🎉 Happy Birthday {', '.join(names)}! 🎂🎈"
    group_name = "Your WhatsApp Group Name"

    driver = webdriver.Chrome()  # WebDriver Manager can be used here for ease
    driver.get("https://web.whatsapp.com/")
    
    input("Scan the QR code and press Enter...")  # Wait for manual login

    search_box = driver.find_element("xpath", "//div[@contenteditable='true']")
    search_box.send_keys(group_name)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(2)
    
    msg_box = driver.find_element("xpath", "//div[@title='Type a message']")
    msg_box.send_keys(message)
    msg_box.send_keys(Keys.RETURN)

    print("Birthday message sent!")
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    birthday_names = get_birthday_names()
    send_whatsapp_message(birthday_names)
