from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Number of times to send the message
n = 5

# Function to send the message n times
def send_whatsapp_message(number, message, n):
    # Start Chrome WebDriver
    driver = webdriver.Chrome()

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)  # Allowing time to scan the QR code

    # Find the input field for searching contacts
    search_field = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    search_field.click()

    # Enter the contact's name/number
    search_field.send_keys(number + Keys.ENTER)

    # Find the input field for typing the message
    message_field = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')

    # Send the message n times
    for i in range(n):
        message_field.send_keys(message + Keys.ENTER)
        time.sleep(1)  # Delay between each message

    # Close the WebDriver
    driver.quit()

# Provide the phone number or contact name, message, and number of times to send
contact = "Nanna"  # Replace with the recipient's name or phone number
message = "Hello, how are you?"  # Replace with the desired message

send_whatsapp_message(contact, message, n)
