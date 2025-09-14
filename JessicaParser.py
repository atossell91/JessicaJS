from html.parser import HTMLParser
from HtmlElement import HtmlElement

class JessicaParser(HTMLParser):
    def __init__(self, *, convert_charrefs = True):
        super().__init__(convert_charrefs=convert_charrefs)

        self.elements: list[HtmlElement] = []
        self.elements.append(HtmlElement("root"))

    def parse(self, html_str: str):
        self.feed(html_str)
    
    def flush(self):
        root: HtmlElement = self.elements[0]
        self.elements = []
        return root

    def handle_starttag(self, tag, attrs):
        lastElem = self.elements[-1]
        elem = HtmlElement(tag)
        lastElem.children.append(elem)
        self.elements.append(elem)
    
    def handle_endtag(self, tag):
        self.elements.pop()
    
    def handle_data(self, data):
        pass
