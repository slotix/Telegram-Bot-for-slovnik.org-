import requests
from bs4 import BeautifulSoup
import re
import os 

'''http://slovnik.azet.sk/preklad/rusko-slovensky/?q=минимализм'''
BASE_URL = "http://slovnik.azet.sk/preklad/{}-{}/?q={}"
'''
    --- Telegram restrictions ---
    400 BAD_REQUEST	MESSAGE_TOO_LONG	Message was too long.
    Current maximum length is 4096 UTF8 characters
'''
MAX_LENGTH = 4093

'''
target_langs = ['anglicky', 'nemecky', 'francuzsky', 'spanielsky', 'madarsky', 'taliansky', 'rusky']
'''


class Parser:
    def __init__(self, q):
        self.query = q.strip()
        self.text_length = MAX_LENGTH
        self.source = 'slovensko'
        self.target = os.environ['LANGUAGE']


    def download(self):
        r =requests.get(BASE_URL.format(self.source, self.target, self.query))
        r.encoding = 'utf-8'
        self.soup = BeautifulSoup(r.text, "lxml")


    def parse(self):
        items = self.soup.find_all("a", attrs={"class": "unselectable lupa"})
        if len(items) == 0:
            return None
        for item in items:
            item.decompose()
        items = self.soup.find_all("table", "p")
        translated_items = [re.sub(r'\[[^\]]+\]', '', item.text) for item in items]


        text = '\n'.join(translated_items)
        if len(text) > self.text_length:
            txt = (text[:self.text_length] + '...\n')
            link  = '<a href="{}">More... </a>.'.format(BASE_URL.format(self.source, self.target, self.query))
            return '{0}\n{1}'.format(txt, link)
        else:
            return text

    def get_translated_text(self, length= MAX_LENGTH):
        self.download()
        self.text_length = length
        result = self.parse()
        if not result:
            self.source = '{}o'.format(languages[7])
            self.target = '{}y'.format(languages[0])
            self.download()
            result = self.parse()
        return result