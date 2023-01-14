from day_four import day_four

# Libraries for open and use Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def giorno_tre(driver, collection):
    #Giorno tre
    try:
        date = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[1]"))).text) # Date
        split_date = date.split() # Split date
        description = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/p"))).text) # Homework 1 or no homework
        mydict = {
                    "subjects": [
                    {
                        "name": "No school subject",
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description,
                    }
                ]
            }
        ]
    },

        x = collection.insert_many(mydict) # Insert data in MongoDB

        school_subject = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li/h2"))).text) # School subject 1
        new_school_subject = {"$set": {"School Subject": school_subject}} # Update school subject
        collection.update_one(mydict, new_school_subject) # Update school subject
        try:
            school_subject_1 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # School subject 1
            description_1 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1
            mydict1 = {
                    "subjects": [
                    {
                        "name": school_subject_1,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_1,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict1) # Insert data in MongoDB

            school_subject_2 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            description_2 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2
            mydict2 = {
                    "subjects": [
                    {
                        "name": school_subject_2,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_2,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict2) # Insert data in MongoDB

            school_subject_3 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            description_3 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3
            mydict3 = {
                    "subjects": [
                    {
                        "name": school_subject_3,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_3,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict3) # Insert data in MongoDB

            school_subject_4 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            description_4 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4
            mydict4 = {
                    "subjects": [
                    {
                        "name": school_subject_4,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_4,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict4) # Insert data in MongoDB

            school_subject_5 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            description_5 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
            mydict5 = {
                    "subjects": [
                    {
                        "name": school_subject_5,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_5,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict5) # Insert data in MongoDB

        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            day_four.giorno_quattro(driver, collection)
    except TimeoutException:
        try:
            school_subject_1 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/h2"))).text) # School subject 1
            description_1 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[1]/div/ul/li/p"))).text) # Homework 1
            mydict6 = {
                    "subjects": [
                    {
                        "name": school_subject_1,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_1,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict6) # Insert data in MongoDB

            school_subject_2 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/h2"))).text) # School subject 2
            description_2 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[2]/div/ul/li/p"))).text) # Homework 2
            mydict7 = {
                    "subjects": [
                    {
                        "name": school_subject_2,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_2,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict7) # Insert data in MongoDB

            school_subject_3 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/h2"))).text) # School subject 3
            description_3 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[3]/div/ul/li/p"))).text) # Homework 3
            mydict8 = {
                    "subjects": [
                    {
                        "name": school_subject_3,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_3,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict8) # Insert data in MongoDB

            school_subject_4 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/h2"))).text) # School subject 4
            description_4 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[4]/div/ul/li/p"))).text) # Homework 4
            mydict9 = {
                    "subjects": [
                    {
                        "name": school_subject_4,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_4,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict9) # Insert data in MongoDB

            school_subject_5 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/h2"))).text) # School subject 5
            description_5 = str(WebDriverWait(driver, 250).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div[2]/div/ul/li[5]/div/ul/li/p"))).text) # Homework 5
            mydict10 = {
                    "subjects": [
                    {
                        "name": school_subject_5,
                        "homework": [
                        {
                            "date": {
                            "day": split_date[0],
                            "month": split_date[1],
                            "year": split_date[2],
                        },
                    "description": description_5,
                    }
                ]
            }
        ]
    },

            x = collection.insert_many(mydict10) # Insert data in MongoDB
        except TimeoutException:
            WebDriverWait(driver, 250).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/div/div[1]/div[1]/div[1]/button[3]"))).click() # Click on next day button
            day_four.giorno_quattro(driver, collection)