# HTML Table to Markdown Table Converter

This script converts an HTML table to a Markdown table with the following conditions:
- If a text is separated with a new line within a `<td>` tag, rather than going to a new line or printing 'n', use the HTML `<br>` tag to position the text within the cell.
- If the text has attributes that cannot be converted to markdown, for example `<span style>`, the script will print it exactly as an HTML tag.

## Usage

```python
from html_to_markdown import html_to_markdown

html_table = '<table>...</table>'
markdown_table = html_to_markdown(html_table)
print(markdown_table)
```

## Note

This script is a basic example of how to do the conversion and you might need to handle more edge cases, add error handling and validation.

## Requirements

- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)


## Installation

```
pip install beautifulsoup4
```

## Contributing

Feel free to fork this repository, improve the code and submit a pull request for review.