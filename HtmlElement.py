class HtmlElement:
    def __init__(self, name):
        self.name: str = name
        self.children: list[HtmlElement] = []
        self.data: str = None
        self.attributes: list[str, str] = None

    def clone(self):
        clone = HtmlElement(self.name)
        clone.data = self.data
        for child in self.children:
            child_clone = child.clone()
            clone.children.append(child_clone)
        return clone
