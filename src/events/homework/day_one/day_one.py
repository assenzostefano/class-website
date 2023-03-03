from day_two import day_two

# Libraries for open and use Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def insert_homework_to_mongo(collection, school_subject, date, description):
    # Check if homework already exists in the collection
    if collection.find_one({"long_date": date, "name": school_subject, "description": description}):
        print("Homework already in database")
    else:
        # Create dictionary for MongoDB document
        mydict = {
            "name": school_subject,
            "date": {
                "long_date": date,
                "day": date.split()[0],
                "month": date.split()[1],
                "year": date.split()[2]
            },
            "description": description
        }
        # Insert document into MongoDB
        x = collection.insert_one(mydict)
        print("Homework inserted into database")

def giorno_uno(driver, collection):
    #Giorno uno
    try:
        date = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[1]"))).text) # Date
        split_date = date.split() # Split date
        description = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/p"))).text) # Homework 1 or no homework

        # Insert homework for "No school subject"
        insert_homework_to_mongo(collection, "No school subject", date, description)

        # Loop through all school subjects and insert homework for each
        school_subjects = driver.find_elements_by_xpath("/html/body/div/div/main/div/div[2]/div/ul/li")
        for subject in school_subjects:
            school_subject = str(subject.find_element_by_xpath("./h2").text)
            homework = subject.find_element_by_xpath("./div/ul/li/p").text

            # Insert homework for current school subject
            insert_homework_to_mongo(collection, school_subject, date, homework)

        try:
            # Click on next day button
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click()
            # Call giorno_due() function from day_two.py for next day
            day_two.giorno_due(driver, collection)
        except TimeoutException:
            # No more days to scrape, end function
            pass
    
    except:
        print("Error")
