import re
from typing import Final
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

class Browser:
    def __init__(self, driver: str):
        print('Starting up...')
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service= self.service, options = self.chrome_options)

    def scrape_emails(self, url: str)-> set:
        print('scrapping emails')
        self.browser.get(url)
        page_source: str = self.browser.page_source

        list_of_emails: set = set()

        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(re.match.group())
        return list_of_emails

    def closer_browser(self):
        print('Closing...')
        self.browser.close


def main():
    driver: str = 'ChromeDriver'
    browser = Browser(driver=driver)

    emails: set = browser.scrape_emails('===Enter URL Here===')

    for i, email in enumerate(emails, start=1):
        print(i, email, sep = ': ')

if __name__ == '__main__':
    main()

