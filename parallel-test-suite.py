import os
import time
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


start_time = time.time()

usernames = ['user1', 'user2']
usernames1 = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10', 'user11', 'user12', 'user13', 'user14', 'user15', 'user16',
             'user17', 'user18', 'user19', 'user20', 'user21', 'user22', 'user23', 'user24', 'user25', 'user26', 'user27', 'user28', 'user29', 'user30', 'user31', 'user32',
             'user33', 'user34', 'user35', 'user36', 'user37', 'user38', 'user39', 'user40', 'user41', 'user42', 'user43', 'user44', 'user45', 'user46', 'user47', 'user48',
             'user49', 'user50', 'user51', 'user52', 'user53', 'user54', 'user55', 'user56', 'user57', 'user58', 'user59', 'user60', 'user61', 'user62', 'user63', 'user64',
             'user65', 'user66', 'user67', 'user68', 'user69', 'user70', 'user71', 'user72', 'user73', 'user74', 'user75', 'user76', 'user77', 'user78', 'user79', 'user80',
             'user81', 'user82', 'user83', 'user84', 'user85', 'user86', 'user87', 'user88', 'user89', 'user90', 'user91', 'user92', 'user93', 'user94', 'user95', 'user96',
             'user97', 'user98', 'user99', 'user100']
passwords = ['user1!', 'user2!', 'user3!', 'user4!', 'user5!', 'user6!', 'user7!', 'user8!', 'user9!', 'user10!', 'user11!', 'user12!', 'user13!', 'user14!', 'user15!', 'user16!',
             'user17!', 'user18!', 'user19!', 'user20!', 'user21!', 'user22!', 'user23!', 'user24!', 'user25!', 'user26!', 'user27!', 'user28!', 'user29!', 'user30!', 'user31!',
             'user32!', 'user33!', 'user34!', 'user35!', 'user36!', 'user37!', 'user38!', 'user39!', 'user40!', 'user41!', 'user42!', 'user43!', 'user44!', 'user45!', 'user46!',
             'user47!', 'user48!', 'user49!', 'user50!', 'user51!', 'user52!', 'user53!', 'user54!', 'user55!', 'user56!', 'user57!', 'user58!', 'user59!', 'user60!', 'user61!',
             'user62!', 'user63!', 'user64!', 'user65!', 'user66!', 'user67!', 'user68!', 'user69!', 'user70!', 'user71!', 'user72!', 'user73!', 'user74!', 'user75!', 'user76!',
             'user77!', 'user78!', 'user79!', 'user80!', 'user81!', 'user82!', 'user83!', 'user84!', 'user85!', 'user86!', 'user87!', 'user88!', 'user89!', 'user90!', 'user91!',
             'user92!', 'user93!', 'user94!', 'user95!', 'user96!', 'user97!', 'user98!', 'user99!', 'user100!']


def run_session(user):
    s = Service('/home/altynai/selenium-drivers/chromedriver')
    driver = webdriver.Chrome(service=s)
    try:
        url = 'https://service2.diplo.de/rktermin/extern/choose_category.do?locationCode=eriw&realmId=351&categoryId=568'
        driver.get(url)
        driver.implicitly_wait(5)
        username = driver.find_element(By.ID, 'username')
        username.send_keys(user)
        password = driver.find_element(By.ID, 'password')
        password.send_keys(user + '!')
        login_button = driver.find_element(By.ID, 'loginbtn')
        login_button.click()
        url = 'http://localhost/mod/surveyplugin/view.php'
        driver.get(url)
        print('Logged in')
        question1 = driver.find_element(By.ID, 'id_question335_1')
        question1.send_keys(Keys.SPACE)

        question2 = driver.find_element(By.ID, 'id_question336_1')
        question2.send_keys(Keys.SPACE)

        question3 = driver.find_element(By.ID, 'id_question337_1')
        question3.send_keys(Keys.SPACE)

        question4 = driver.find_element(By.ID, 'id_question338_1')
        question4.send_keys(Keys.SPACE)

        question5 = driver.find_element(By.ID, 'id_question339_1')
        question5.send_keys(Keys.SPACE)

        question6 = driver.find_element(By.ID, 'id_question340_1')
        question6.send_keys(Keys.SPACE)

        question7 = driver.find_element(By.ID, 'id_question341_1')
        question7.send_keys(Keys.SPACE)

        question8 = driver.find_element(By.ID, 'id_question342_1')
        question8.send_keys(Keys.SPACE)

        question9 = driver.find_element(By.ID, 'id_question343_1')
        question9.send_keys(Keys.SPACE)

        question10 = driver.find_element(By.ID, 'id_question344_1')
        question10.send_keys(Keys.SPACE)

        question11 = driver.find_element(By.ID, 'id_question345_1')
        question11.send_keys(Keys.SPACE)

        question12 = driver.find_element(By.ID, 'id_question346_1')
        question12.send_keys(Keys.SPACE)
        print('Answered all questions for student ' + user)

        next_button = driver.find_element(By.ID, 'id_submitbutton')
        next_button.send_keys(Keys.ENTER)
        print('Submitted the survey for student ' + user)

    except NoSuchElementException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some elements failed to load"}}')
    # Stop the driver
    driver.quit()

with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(run_session, usernames)

print("--- %s seconds ---" % (time.time() - start_time))

# Running parallel tests

# with 20 students and maximum of 20 workers for executor => no errors, 240 entries in student_answer_attempts: CHECK (expected functionality) --> DONE

# with 30 students and maximum of 20 workers for executor => no errors, 360 entries in student_answer_attempts: CHECK (expected functionality) --> DONE

# with 100 students and maximum of 25 workers for executor => no errors, 1200 entries in student_answer_attempts: CHECK (expected functionality)
