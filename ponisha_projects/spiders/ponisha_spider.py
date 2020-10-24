import urllib.parse
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ..items import Project
import datetime


class PonishaSpider(scrapy.Spider):
    name = "ponisha"
    allowed_domains = ["ponisha.ir"]
    start_urls = ['https://ponisha.ir/search/projects/skill-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D8%AA%D8%AD%D8%AA-%D9%88%D8%A8/status-open']

    def start_requests(self):
        for url in self.start_urls:
            # Auto scroll down
            print(url)
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=1,
                wait_until=EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'pagination')),
            )

    def parse(self, response):
        """
        @with_selenium
        """
        projects = self.get_projects_list(response)
        for project in projects:

            # Calling abstarct method get_project_dict()
            project_dict = self.get_project_dict(project)

            info_url = project.xpath('.//a[1]/@href').get()
            yield SeleniumRequest(
                url=info_url,
                callback=self.parse_full_project_page,
                cb_kwargs=dict(project_dict=project_dict),
                wait_time=1,
                wait_until=EC.presence_of_element_located(
                    (By.ID, 'url-input'))
            )

        next_page_url = response.xpath(
            '//body/div[2]/div[1]/div[2]/div/form/div[4]/nav/ul/li[11]/a/@href').get()
        if next_page_url != None:
            yield SeleniumRequest(
                url=f'https://ponisha.ir{next_page_url}',
                callback=self.parse,
                wait_time=1,
                wait_until=EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'pagination')),
            )

    def get_projects_list(self, response):
        """
        @with_selenium
        """
        return response.xpath('//li[contains(@class,"item")]')

    def get_project_dict(self, selector):
        return {
            'last_modified': datetime.datetime.now(),
            'title': selector.xpath('.//div[contains(@class, "detail")]/div/div[contains(@class, "title")]/a/h4/text()').get(),
            'skills': selector.xpath('.//div[contains(@class, "labels")]/a/@title').getall(),
            'budget': selector.xpath('.//div[1]/div/span/span/span[1]/text()').get(),
            'applicants_number': ''.join([n for n in ''.join(selector.xpath('.//div[2]/div[2]/div[1]/text()').get()).strip() if n.isdigit()]),
            'remaining_time': selector.xpath('.//div[2]/div[2]/div[2]/span/text()').get().strip()
        }

    def parse_full_project_page(self, response, project_dict):
        """
        @with_selenium
        """
        project_dict['creator'] = response.xpath(
            '//div[contains(@class, "header-content")]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/a[1]/text()').get()
        project_dict['short_link'] = response.xpath(
            '//*[@id="url-input"]/text()').get()
        project_dict['description'] = '\n'.join(response.xpath(
            '//body/div[2]/div[2]/div/div[1]/div[1]/p//text()').getall())

        return Project(project_dict)
