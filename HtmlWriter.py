def repeat_str(seq, repeats):
    output = ""
    for i in range(repeats):
        output = output + seq
    return output

def print_attrs(attrs: list[tuple]):
    output = ""
    if attrs is None:
        return output

    for tuple in attrs:
        output = output + f' {tuple[0]}="{tuple[1]}"'
    return output

def write_html(tree, indent=0):
    spaces = repeat_str(" ", indent)
    output: str = ""
    output = output + "\n" + spaces + "<" + tree.name + print_attrs(tree.attributes) + ">"

    print(tree.data)
    if tree.data is not None:
        output = output + "\n    " + spaces + tree.data

    for child in tree.children:
        output = output + write_html(child, indent + 4)
    output = output + "\n" + spaces + "</" + tree.name + ">"
    return output
