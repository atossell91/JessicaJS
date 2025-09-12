class HtmlElement:
    def __init__(self, name):
        self.name: str = name
        self.children: list[HtmlElement] = []
        self.data = None