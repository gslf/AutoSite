from typing import Dict
from jinja2 import Template


class DataTemplate:
    """
    A class to handle HTML templating using Jinja2.
    """

    def __init__(self, template_path: str):
        """
        Initialize the DataTemplate with the path to the HTML template.

        :param template_path: Path to the HTML template file
        """
        self.template_path = template_path

    def _load_template(self) -> Template:
        """
        Load and parse the HTML template file.

        :return: A Jinja2 Template object
        """
        with open(self.template_path, "r", encoding="utf-8") as file:
            template_content = file.read()
        return Template(template_content)

    def render(self, context: Dict[str, str], output_path: str) -> None:
        """
        Render the template with the provided context and save the result to a file.

        :param context: Dictionary containing the values to inject into the template
        :param output_path: Path to save the rendered HTML file
        """
        template = self._load_template()
        rendered_content = template.render(context)

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(rendered_content)