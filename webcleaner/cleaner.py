from bs4 import BeautifulSoup
from typing import Optional

class WebCleaner:
    """
    Cleans raw HTML content by removing common clutter like scripts, styles,
    comments, and redundant whitespace.
    """

    def __init__(self, parser: str = 'lxml'):
        """
        Initializes the WebCleaner.

        Args:
            parser (str): The HTML parser to use ('lxml', 'html.parser', 'html5lib').
                          'lxml' is generally faster.
        """
        self.parser = parser

    def clean_html(self, html_content: str) -> str:
        """
        Cleans the provided HTML content.

        Args:
            html_content (str): The raw HTML string to clean.

        Returns:
            str: Cleaned HTML string.
        """
        if not html_content:
            return ""

        soup = BeautifulSoup(html_content, self.parser)

        # Remove script and style tags
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        # Remove comments
        for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()

        # Get text and remove excessive whitespace
        text = soup.get_text(separator=' ')
        clean_text = ' '.join(text.split())

        return clean_text

class Comment:
    """Helper class for BeautifulSoup to identify comments."""
    def __eq__(self, other):
        return isinstance(other, Comment) or (hasattr(other, 'string') and other.string is not None and other.string.startswith('<!--') and other.string.endswith('-->'))

    def __hash__(self):
        return hash("Comment")
