from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

page_url = "http://howstat.com/cricket/Statistics/Matches/MatchScorecard_ODI.asp?MatchCode=4692"
driver.get(page_url)
driver.find_element(By.TAG_NAME, 'tr').click()
