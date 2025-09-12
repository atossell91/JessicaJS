from html.parser import HTMLParser

class HtmlElement:
    def __init__(self, name):
        self.name: str = name
        self.children: list[HtmlElement] = []
        self.data = None

class JessicaParser(HTMLParser):
    def __init__(self, *, convert_charrefs = True):
        super().__init__(convert_charrefs=convert_charrefs)

        self.elements: list[HtmlElement] = []
        self.elements.append(HtmlElement("root"))

    def handle_starttag(self, tag, attrs):
        lastElem = self.elements[-1]
        elem = HtmlElement(tag)
        lastElem.children.append(elem)
        self.elements.append(elem)
    
    def handle_endtag(self, tag):
        self.elements.pop()
    
    def handle_data(self, data):
        pass
