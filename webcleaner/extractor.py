from bs4 import BeautifulSoup, Tag
from typing import Optional

class ContentExtractor:
    """
    Extracts the main content from a cleaned HTML page, attempting to identify
    the most relevant section of text. This is a heuristic-based approach.
    """

    def __init__(self, parser: str = 'lxml'):
        """
        Initializes the ContentExtractor.

        Args:
            parser (str): The HTML parser to use ('lxml', 'html.parser', 'html5lib').
        """
        self.parser = parser

    def extract_main_content(self, html_content: str) -> str:
        """
        Extracts the main textual content from an HTML string.
        This method uses a heuristic of finding the tag with the most text content.

        Args:
            html_content (str): The HTML string (preferably pre-cleaned by WebCleaner).

        Returns:
            str: The extracted main content as a string.
        """
        if not html_content:
            return ""

        soup = BeautifulSoup(html_content, self.parser)

        # A simple heuristic: find the element with the most text content.
        # This can be improved with more sophisticated algorithms (e.g., readability.js port).
        max_text_len = 0
        main_element_text = ""

        for tag in soup.find_all(['p', 'div', 'article', 'section', 'main']):
            text_content = tag.get_text(separator=' ', strip=True)
            if len(text_content) > max_text_len:
                max_text_len = len(text_content)
                main_element_text = text_content

        if not main_element_text:
            # Fallback to entire body text if no specific element is found
            body = soup.find('body')
            if body:
                main_element_text = body.get_text(separator=' ', strip=True)

        return ' '.join(main_element_text.split())
