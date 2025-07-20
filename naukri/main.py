from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import naukri.constructor as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

class Naukri(webdriver.Chrome):
    def __init__(self,driver_path='/Users/srijangupta/Downloads/chromedriver-mac-arm64-2/chromedriver',teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown

        service=Service(executable_path=driver_path)
        options=Options()
        options.add_experimental_option('detach',True)
        super().__init__(service=service,options=options)
        self.implicitly_wait(1500)
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_frst_page(self):
            self.get(const.default_URL)


    def login(self):
        wait=WebDriverWait(self,200)
        button=wait.until(EC.element_to_be_clickable((By.ID,'login_Layer')))
        button.click()

    def enter_mail(self):
        wait=WebDriverWait(self,20)
        email_input=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Enter your active Email ID / Username"]')))
        email_input.send_keys(const.email)

    def enter_password(self):
        wait=WebDriverWait(self,20)
        password_input=wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Enter your password"]')))
        password_input.send_keys(const.password)

    def loggin_btn(self):
        wait = WebDriverWait(self, 20)
        button= wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary.loginButton')))
        button.click()

    def search_btn(self):
        wait = WebDriverWait(self, 20)
        button= wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.nI-gNb-sb__icon-wrapper')))
        button.click()


    def enter_job(self):
        wait=WebDriverWait(self,20)
        job=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[placeholder="Enter keyword / designation / companies"]')))
        job.send_keys(const.job_name)

    def enter_location(self):
        wait=WebDriverWait(self,20)
        location=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'input[placeholder="Enter location"]')))
        location.send_keys(const.location)

    def expand_btn(self):
        wait = WebDriverWait(self, 20)
        button= wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ni-gnb-icn-expand-more")))
        button.click()
        self.implicitly_wait(30)

    def job_btn(self):
        wait = WebDriverWait(self, 20)
        button= wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[value="ajob"]')))
        button.click()

    def job_search_btn(self):
        wait = WebDriverWait(self, 20)
        button= wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button .ni-gnb-icn-search')))
        button.click()

    def scrape_jobs(self):
        print("🔍 Scraping job listings...")

        wait = WebDriverWait(self, 15)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.cust-job-tuple")))

        jobs = self.find_elements(By.CSS_SELECTOR, 'div.cust-job-tuple')
        print(f"Found {len(jobs)} job cards.")

        results = []

        for job in jobs:
            try:
                title = job.find_element(By.CSS_SELECTOR, 'a.title').text
                company = job.find_element(By.CSS_SELECTOR, 'a.comp-name').text
                location = job.find_element(By.CSS_SELECTOR, 'span.locWdth').text
                experience = job.find_element(By.CSS_SELECTOR, 'span.expwdth').text
                posted = job.find_element(By.CSS_SELECTOR, 'span.job-post-day').text
                description = job.find_element(By.CSS_SELECTOR, 'span.job-desc').text

                # Tags (optional — list of skills)
                tags = [tag.text for tag in job.find_elements(By.CSS_SELECTOR, 'ul.tags-gt > li')]
                tags_joined = ", ".join(tags)

                results.append({
                    "Title": title,
                    "Company": company,
                    "Location": location,
                    "Experience": experience,
                    "Posted": posted,
                    "Tags": tags_joined,
                    "Description": description
                })

            except Exception as e:
                print("⚠️ Error parsing job card:", e)

        # Save to CSV
        import pandas as pd
        df = pd.DataFrame(results)
        df.to_csv("naukri_job_results.csv", index=False)
        print(f"✅ Saved {len(df)} jobs to naukri_job_results.csv")



