from html.parser import HTMLParser
from HtmlElement import HtmlElement

class JessicaParser(HTMLParser):
    def __init__(self, *, convert_charrefs = True):
        super().__init__(convert_charrefs=convert_charrefs)

        self.clear_elements()

    def clear_elements(self):
        self.elements: list[HtmlElement] = []
        self.elements.append(HtmlElement("root"))

    def parse(self, html_str: str) -> HtmlElement:
        self.feed(html_str)
        elem: HtmlElement = self.elements[0]
        self.clear_elements()

        return elem

    def handle_starttag(self, tag, attrs):
        lastElem = self.elements[-1]
        elem = HtmlElement(tag)
        lastElem.children.append(elem)
        self.elements.append(elem)
    
    def handle_endtag(self, tag):
        self.elements.pop()
    
    def handle_data(self, data):
        pass

def parse_html(html_str: str) -> HtmlElement:
    parser: JessicaParser = JessicaParser()
    elem: HtmlElement = parser.parse(html_str)
    return elem
