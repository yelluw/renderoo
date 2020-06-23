import os
from unittest import TestCase
from unittest.mock import patch, mock_open
from component import Component
from template_writer import HTMLTemplateWriter


class HelloWorldComponent(Component):
    def render(self):
        return "<p>Hello, world.</p>"


class HelloWorldComponentTest(TestCase):
    def setUp(self):
        self.component = HelloWorldComponent()

    def test_component_render_returns_html_string(self):
        self.assertTrue(self.component.render() == "<p>Hello, world.</p>")


class NestedComponent(Component):
    def render(self):
        return f"<div>{HelloWorldComponent().render()}</div>"


class NestedComponentTest(TestCase):
    def setUp(self):
        self.nested_component = NestedComponent()

    def test_nested_component_returns_html_string(self):
        self.assertTrue(
            self.nested_component.render() == f"<div>{HelloWorldComponent().render()}</div>")


class ParametrizedComponent(Component):
    def render(self, component):
        return f'<div>{component}</div>'


class ParametrizedComponentTest(TestCase):
    def setUp(self):
        self.parametrized_component = ParametrizedComponent()

    def test_parametrized_component_returns_html_string(self):
        hello_world_component = HelloWorldComponent().render()
        self.assertTrue(
            self.parametrized_component.render(
                hello_world_component) == f"<div>{hello_world_component}</div>")


class ParentWithChildComponent(Component):
    def __init__(self, child_component):
        self.child_component = child_component

    def render(self):
        return f"<div>{self.child_component}</div>"


class ParentWithChildComponentTest(TestCase):
    def setUp(self):
        self.child_component = HelloWorldComponent().render()
        self.parent_with_child_component = ParentWithChildComponent(
            self.child_component).render()

    def test_parent_with_child_component_returns_html_string(self):
        self.assertTrue(
            self.parent_with_child_component == "<div><p>Hello, world.</p></div>")


class HelloWorldHTMLTemplateTest(TestCase):
    def setUp(self):
        self.html = HelloWorldComponent().render()
        self.template_name = 'test.html'
        self.html_template = HTMLTemplateWriter(
            self.html,
            self.template_name,)

    def test_write_template(self):
        self.html_template.write()
        with open(self.template_name, 'r') as f:
            template = f.read()
        self.assertTrue(template == self.html)
        os.remove(self.template_name)
