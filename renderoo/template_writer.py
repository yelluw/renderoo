class TemplateWriter:
    def __init__(self, html, template_name):
        self.html = html
        self.template_name = template_name

    def write(self):
        with open(self.template_name, 'w') as f:
            f.write(self.html)


class HTMLTemplateWriter(TemplateWriter):
    pass