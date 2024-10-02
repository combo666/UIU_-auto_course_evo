from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  # Import Select for dropdown menus
from selenium.webdriver.chrome.service import Service

# Step 1: Set up WebDriver
driver_path = 'G:\Applications\chromedriver-win64\chromedriver-win64/chromedriver.exe'  # Update with your path to the ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Step 2: Open the login page
driver.get("https://ucam.uiu.ac.bd/")

# Step 3: Log in to the system
username_field = driver.find_element(By.ID, "logMain_UserName")
password_field = driver.find_element(By.ID, "logMain_Password")

username_field.send_keys("your_student_id")  # Replace with your username
password_field.send_keys("your")  # Replace with your password

# Click the login button
login_button = driver.find_element(By.ID, "logMain_Button1")
login_button.click()

# Step 4: Wait until login process is complete and dashboard page loads
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home")))

# Step 5: Click the 'Registration' button
registration_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Registration"))
)
registration_button.click()

# Step 6: Click the 'Course Evaluation' button
course_evaluation_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Course Evaluation"))
)
course_evaluation_button.click()

# Step 7: Click the 'Evaluation Form' button
evaluation_form_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Evaluation Form"))
)
evaluation_form_button.click()

# Step 8: Wait for the dropdown to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContainer_ddlAcaCalSection")))

import time

# Step 9: Select the first available course from the dropdown
course_dropdown = Select(driver.find_element(By.ID, "ctl00_MainContainer_ddlAcaCalSection"))
course_dropdown.select_by_index(1)  # Select the first available course

# Wait for a few seconds for the form to load
time.sleep(3)

# Now select the grade
grade_dropdown = Select(driver.find_element(By.ID, "ctl00_MainContainer_ddlExpectedGrade"))
grade_dropdown.select_by_index(2)  # Select grade A-



# Step 11: Wait for the form to load and then fill it out (Example: "Strongly Agree" for the first question)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ctl00_MainContainer_rbtTheory1_0")))

# Fill out the form with your desired responses
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory1_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory2_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory3_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory4_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory5_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory6_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory7_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory8_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory9_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory10_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory11_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory12_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory13_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory14_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory15_2").click()  
driver.find_element(By.ID, "ctl00_MainContainer_rbtTheory16_2").click() 



# Step 12: Submit the form
submit_button = driver.find_element(By.ID, "ctl00_MainContainer_btnTheorySubmit")
submit_button.click()

# Step 13: Wait for the URL to change (indicating form submission completed)
WebDriverWait(driver, 30).until(EC.url_changes("https://ucam.uiu.ac.bd/Employee/EvaluationForm.aspx?mmi=40545a1642555b514e63"))

# Step 14: Close the browser after the URL changes
driver.quit()



