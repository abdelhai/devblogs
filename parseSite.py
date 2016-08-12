from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def error(self, message):
        pass

    n = False

    def handle_data(self, data):
        if self.n:
            print(data)
            self.n = False
        if "Site:" in data:
            self.n = True


with open('Powered-by-Pelican', 'r') as file:
    data = file.read().replace('\n', '')

parser = MyHTMLParser()
parser.feed(data)
