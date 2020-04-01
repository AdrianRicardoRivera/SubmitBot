import os
import sys
from time import sleep
from credentials import username, password
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SubmitBot():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless') #chrome with no window
        #open chrome
        try:
            self.driver = webdriver.Chrome(sys.path[0] + "/venv/bin/chromedriver", options=chrome_options)
        except Exception:
            print ("Failed to open chrome. Please install Google Chrome.")
            sys.exit(1)
        self.driver.implicitly_wait(10) #wait 10 seconds before throwing ElementNotFound exception
    def login(self):
        #navigate to gradescope.com
        self.driver.get('https://gradescope.com')

        #find and click first log in button
        lg_btn = self.driver.find_element_by_xpath('/html/body/div/main/div[2]/div/header/nav/div[2]/span[3]/button')
        lg_btn.click()

        #enters username and password inside the credentials.py file
        email_in = self.driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[1]/form/div[1]/input')
        email_in.send_keys(username)
        pass_in = self.driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[1]/form/div[2]/input')
        pass_in.send_keys(password)

        #find and click second log in button
        lg_btn2 = self.driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[1]/form/div[4]/input')
        lg_btn2.click()
        #find and click CMSC330
        try:
            course = self.driver.find_element_by_xpath('//*[@href="/courses/85770"]')
        except Exception:
            print("failed to login. Check credentials.py")
            self.driver.close()
            sys.exit(1)
        course.click()

    def submit(self, proj_name, file_paths):
        #case for first upload
        try:
            #find and click project
            proj = self.driver.find_element_by_xpath('//*[@aria-label="Submit {}"]'.format(proj_name))
            proj.click()
            #upload each file
            for i in range(len(file_paths)):
                input = self.driver.find_element_by_xpath('//*[@class="dz-hidden-input"]')
                input.send_keys(file_paths[i])
            #find and click upload commit button
            upload = self.driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[2]/form/div[5]/button[1]')
            upload.click()

        #case for reuploads
        except Exception:
            try:
                proj = self.driver.find_element_by_xpath('//*[@aria-label="View {}"]'.format(proj_name))
                proj.click()
                resubmit = self.driver.find_element_by_xpath('/html/body/div[1]/main/section/ul/li[4]/button')
                resubmit.click()
                for i in range(len(file_paths)):
                    input = self.driver.find_element_by_xpath('//*[@class="dz-hidden-input"]')
                    input.send_keys(file_paths[i])
                upload = self.driver.find_element_by_xpath('/html/body/div[1]/dialog/div/div[2]/form/div[5]/button[1]')
                upload.click()
            except Exception:
                print("failed to find {} or it is not accepting submissions".format(sys.argv[1]))
                self.driver.close()
                sys.exit(1)
if len(sys.argv) > 2: #check arguments
    proj = sys.argv[1]
    paths = []
    for i in range(2, len(sys.argv)):
        path = os.path.abspath(sys.argv[i]) #absolute path of file
        if (os.path.isfile(path)):
            paths.append(path)
        else:
            print("failed to find {}".format(sys.argv[i]))
            self.driver.exit()
            sys.exit(1)
    if (username == '') or (password == ''): #check for username and password
        print("Please enter your username and password into credentials.py")
        sys.exit(1)
    bot = SubmitBot()
    bot.login()
    bot.submit(proj, paths)
    bot.driver.close()
    print("Successfully Submitted!")
    sys.exit(0)
else:
   print("submit.py proj_name file1 file2 ...")