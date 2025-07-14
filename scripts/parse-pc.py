from bs4 import BeautifulSoup
import requests

r = requests.get('https://wisec24-autumn.hotcrp.com/users/pc')
html = r.text
soup = BeautifulSoup(html, 'html.parser')

table_with_foldul_id = soup.find('table', id='foldul')


for row in table_with_foldul_id.find_all('tr'):
    name = row.find('td', class_ = 'pl_name')
    aff = row.find('td', class_ = 'pl_affiliation')

    if name is None:
        continue

    # XXX: Hacky way to determine chair
    is_chair = name.text.endswith(' chair')
    if is_chair:
        name = name.text.split(' chair')[0]
    else:
        name = name.text

    aff = aff.text
    name += ','

    msg = f'- {name:30}*{aff}*'
    if is_chair:
        msg += ' (Chair)'

    print(msg)
