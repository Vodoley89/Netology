import requests
from bs4 import BeautifulSoup
"""
<div class="supernova-search-group__input"><fieldset class="bloko-input-text-wrapper bloko-input-text-wrapper_icon-right"><input type="text" id="a11y-search-input" placeholder="Профессия, должность или компания" name="text" autocomplete="off" data-qa="search-input" class="bloko-input-text" value="python"><span class="bloko-icon-dynamic"><a href="/search/vacancy/advanced?no_default_area&amp;area=1&amp;enable_snippets=true&amp;ored_clusters=true&amp;text=python" data-qa="advanced-search" class="bloko-icon-link"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="bloko-icon bloko-icon_initial-gray-60 bloko-icon_highlighted-gray-80"><path d="M5 8L13 8M13 8C13 9.65686 14.3431 11 16 11C17.6569 11 19 9.65685 19 8C19 6.34315 17.6569 5 16 5C14.3431 5 13 6.34315 13 8ZM11 16L19 16M11 16C11 17.6569 9.65685 19 8 19C6.34315 19 5 17.6569 5 16C5 14.3431 6.34315 13 8 13C9.65685 13 11 14.3431 11 16Z" stroke="var(--bloko-icon-color, var(--bloko-icon-color-default))" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg></a></span></fieldset></div>

"""

HOST = "https://hh.ru/search/vacancy?text=python&area=1&customDomain=1"


html = requests.get(HOST).text
print(html)