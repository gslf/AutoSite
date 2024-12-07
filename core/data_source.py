from typing import Tuple, Dict
from utils.html_preprocessor import  CustomCodeBlockExtension

import markdown

class DataSource:
    """
    A class to parse a markdown file with a metadata header
    and convert the content into HTML while extracting the metadata.
    """

    def __init__(self, file_path: str):
        """
        Initialize the DataSource with the path to the markdown file.

        :param file_path: Path to the markdown file
        """
        self.file_path = file_path

    def _parse_header(self, lines: list[str]) -> Tuple[Dict[str, str], int]:
        """
        Parse the metadata header from the markdown file.

        :param lines: List of lines from the file
        :return: A tuple containing the metadata dictionary and the index of the first non-header line
        """
        header = {}
        header_start = lines.index("###\n") if "###\n" in lines else -1
        header_end = header_start + 1 if header_start != -1 else -1

        if header_start != -1:
            for line in lines[header_start + 1:]:
                if line.strip() == "###":
                    break
                key, value = line.split(":", 1)
                header[key.strip()] = value.strip()
                header_end += 1

        return header, header_end

    def _convert_to_html(self, markdown_content: str) -> str:
        """
        Convert markdown content to HTML.

        :param markdown_content: The markdown content to convert
        :return: HTML string
        """
        return markdown.markdown(markdown_content, extensions=[CustomCodeBlockExtension()])

    def process(self) -> Dict[str, str]:
        """
        Process the markdown file to extract metadata and convert content to HTML.

        :return: A dictionary containing the metadata and the HTML string
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        metadata, content_start = self._parse_header(lines)
        markdown_content = "".join(lines[content_start + 1:]) if content_start != -1 else "".join(lines)
        html_content = self._convert_to_html(markdown_content)
        metadata["main_content"] = html_content

        return metadata