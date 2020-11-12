class Browser(object):

    def __init__(self, engine):
        self.engine = engine

    def open(self, url):
        return self.engine.open(url)

    def element(self, locator):
        return self.engine.element(locator)

    def send_keys(self, text):
        return self.engine.send_keys(text)

    def close(self):
        self.engine.close()
