# Renderoo

https://pypi.org/project/Renderoo/

Renderoo is a small library to render HTML components into HTML templates using python.

The objective is to allow you to build a library of components as python code.

Note that this is not meant to render on the fly. Nor is it meant to be used for client side components.

The use case that promted the development of this library was how annoying it is to write HTML templates in Django.

The Django template engine is easy and simple to use.

But I wanted to reduce the amount of repetition when dealing with HTML.

Repeating HTML over and over opens up the door to errors and style bugs.

This is certainly inspired by JSX, except that I did not choose to create a new markup language for this. It did not make much sense.

# Requirements

Renderoo requires `Python 3` or newer releases. 

I strongly suggest `Python 3.6+` for to the availability of f-strings.


# Install

To install Renderoo run `pip install Renderoo`

# Usage

Renderoo provides two functionalities:

- a component class to subclass when defining your own components
- an html template writer class to write your templates to file

## Defining your own components

There are 4 ways you can define your components.

### Stand alone component

A stand alone component does not accept any parameters and returns an html string.

```
class HelloWorldComponent(Component):
    def render(self):
        return "<p>Hello, world.</p>"
```

### Nested components

A nested component is one component directly inside another.

```
class HelloWorldComponent(Component):
    def render(self):
        return "<p>Hello, world.</p>"


class NestedComponent(Component):
    def render(self):
        return f"<div>{HelloWorldComponent().render()}</div>"
```

### Parametrized component

A parametrized component render method accepts a component as a parameter.

```
class ParametrizedComponent(Component):
    def render(self, component):
        return f'<div>{component}</div>'
```

### Parent with child component

A parent with child component accepts a component as an argument.

```
class ParentWithChildComponent(Component):
    def __init__(self, child_component):
        self.child_component = child_component

    def render(self):
        return f"<div>{self.child_component}</div>"
```


## Using the template writer

The template writer is simply a shortcut to writing your templates to file.

It accepts two parameters: `html` and `template_name`
 
`html` is the html being written.
 
Example: `<p>Hello, world.</p>`

`template_name` is the template name as a full path of where it's going to be written. 

Example: `/path/to/the/template.html`

You can define your own template writers by subclassing the `TemplateWriter` class.

## Using the Renderoo app

`python -m renderoo [init, build, help]`

- `init` - Will initialize a Renderoo project in the currect working directory.

- `build` - Will build all templates in current working directory and output them to wherver you configured it to.

- `help` - Help message and actionable documentation.

# Issues and Bug reports

- Open a ticket
- Clearly explain the issue
- Patiently wait for a response

# Pull requests

Pull requests are welcome and may not be immeditely merged.
Please open an issue to discuss the merits of your idea.

# License

MIT