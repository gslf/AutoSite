from core.settings import Settings
from core.data_source import DataSource
from core.data_template import DataTemplate
from core.list_manager import ListManager

SETTINGS_PATH = "template/settings.json"

def autosite() -> None:
    # Load Settings
    settings = Settings(SETTINGS_PATH)

    for page in settings.data:
        # Load Source markdown
        source = DataSource(page["source"])
        page_context = source.process()
        template = DataTemplate(page["template"])
        template.render(page_context, page["output"])

        listManager = ListManager(page["list"])
        listManager.add_entry(url = page_context["url"], 
                              title = page_context["title"],
                              data = page_context["data"],
                              abstract = page_context["description"])





if __name__ == "__main__":
    autosite()