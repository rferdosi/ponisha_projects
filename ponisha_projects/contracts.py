from scrapy_selenium import SeleniumRequest

class WithSelenium(Contract):
    """ Contract to set the request class to be SeleniumRequest for the current call back method to test.  
    Required to test SeleniumRequests.  

    @with_selenium
    """
    name = 'with_selenium'
    request_cls = SeleniumRequest
