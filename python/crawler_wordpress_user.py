import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Initialize the browser driver (in this case, Firefox)
driver = webdriver.Firefox()

# User get pass and hide password
print("Por favor, insira suas credenciais de login:")
username = input("Username: ")
password = getpass.getpass("Password: ")

# Authenticate the user and password
driver.get("https://www.website.org/wp-login.php")
driver.find_element(By.ID, "user_login").send_keys(username)
driver.find_element(By.ID, "user_pass").send_keys(password)
driver.find_element(By.ID, "wp-submit").click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "the-list"))
)

usernames = []
emails = []
names = []

# Define URL initial
url = "https://www.website.org/wp-admin/users.php?role=subscriber"

while url:
    driver.get(url)
    
    # Wait for the table to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "the-list"))
    )
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Extract the usernames, emails and names
    for row in soup.find_all('tr')[1:]: # Skip the first row (header)
        username_td = row.find('td', {'class': 'username'})
        email_td = row.find('td', {'class': 'email'})
        name_td = row.find('td', {'class': 'name'})
        
        if username_td and email_td and name_td:
            username_strong = username_td.find('strong')
            email_a = email_td.find('a')
            
            if username_strong and email_a:
                usernames.append(username_strong.text)
                emails.append(email_a.text)
                names.append(name_td.text)
    
    # Find the next page button
    next_page = soup.find('a', {'class': 'next-page'})
    url = next_page['href'] if next_page else None

# Close the browser
driver.quit()

# Save the data to a CSV file
df = pd.DataFrame({'Username': usernames, 'Name': names, 'Email': emails})
df.to_csv('users.csv', index=False)
