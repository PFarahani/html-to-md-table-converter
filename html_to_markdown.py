from bs4 import BeautifulSoup

def html_to_markdown(html_table):
    soup = BeautifulSoup(html_table, 'html.parser')
    markdown_table = ''

    # Check for <th> Tag
    if soup.find('thead'):
        header = []
        for t in soup.find_all('th'):
          header.append(t.text.strip())
        markdown_table += '| ' + ' | '.join(header) + ' |' + '\n'
        # Add the markdown table's header divider
        markdown_table += '|' + '----|'*len(header) + '\n'

    else:
        header = []
        # Use first row as header
        first_row = soup.find('tr')
        for t in first_row.find_all('td'):
          header.append(t.text.strip())
        markdown_table += '| ' + ' | '.join(header) + ' |' + '\n'
        # Add the markdown table's header divider
        markdown_table += '|' + '----|'*len(header) + '\n'  


    # loop through the data rows
    for tr in soup.find_all('tr')[1:]:
        row = []
        for td in tr.find_all('td'):
            # join the td contents and replace new line with <br>
            row.append(td.renderContents().decode().strip().replace('\n','<br>'))
        # join the cells in the row with | and add new line at the end
        markdown_table += '| ' + ' | '.join(row) + ' |\n'

    return markdown_table