import json
from typing import List, Dict

class Settings:
    """A class to manage project settings
    """
    file_path: str
    data: List[Dict[str, str]]

    def __init__(self, file_path: str) -> None:
        """
        Init the settings class from a JSON file.
        :param file_path: JSON file path.
        """
        self.file_path = file_path
        self.data = self._load_settings()

    def _load_settings(self) -> List[Dict[str, str]]:
        """
        Load settings from JSON.
        :return: A list of setting dictionary {"source.md": "template.html"}. 
        """
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"JSON settings decoding error: {e}")
            return []