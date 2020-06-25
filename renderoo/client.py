from renderoo.colors import COLORS, CEND


class RenderooCommandLineClient:

    def __init__(self, action):
        self.action = self.actions.get(action, self.HELP)

    BUILD = 'build'
    HELP = 'help'
    INIT = 'init'

    example_component = '''from renderoo.component import Component


class ExampleComponent(Component):
    def render(self):
        return '<p>Example Component</p>'

'''


    project_template = '''from renderoo.template_writer import HTMLTemplateWriter
from example_component import ExampleComponent

components = {
   'ExamplComponent' : {
           'html': ExampleComponent().render(), 'template': 'example.html'
       }
}

for name, component in components.items():
    print(f'Writing {component.get("template")} ...')
    html_template = HTMLTemplateWriter(component.get('html'), component.get('template'))
    html_template.write()

'''

    def build(self):
        with open('renderoo_file.py', 'r') as f:
            exec(f.read())
        print(f'{COLORS.get("success")}Build succeeded ...{CEND}')

    def help(self):
        print(f'{COLORS.get("info")}Help!{CEND}')
    
    def init(self):
        with open('example_component.py', 'w') as f:
            f.write(self.example_component)

        with open('renderoo_file.py', 'w') as f:
            f.write(self.project_template)
        
        print(f'{COLORS.get("info")}Renderoo initialized in current working directory.{CEND}')

    actions = {
        BUILD: build,
        HELP: help,
        INIT: init
    }
    
    def run_action(self):
        return self.action(self)
