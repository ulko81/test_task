class ElementNotFoundException(Exception):
    def __init__(self, item, cause = None):
        super(ElementNotFoundException, self).__init__()
        self.item = item

    def __str__(self):
        return "The element with By.{0} and locator - '{1}' was not found".format(*self.item)


class PageNotFoundException(Exception):
    def __init__(self, url, cause = None):
        super(PageNotFoundException, self).__init__()
        self.url = url

    def __str__(self):
        return "The page '{}' was not found".format(self.url)
