import requests
from bs4 import BeautifulSoup
import re
import os 

'''http://slovnik.azet.sk/preklad/rusko-slovensky/?q=минимализм'''
BASE_URL = "https://slovnik.aktuality.sk/preklad/{}-{}/?q={}"
'''
    --- Telegram restrictions ---
    400 BAD_REQUEST	MESSAGE_TOO_LONG	Message was too long.
    Current maximum length is 4096 UTF8 characters
'''
MAX_LENGTH = 4093


class Parser:  
    def __init__(self, q):
        self.query = q.strip()
        self.text_length = MAX_LENGTH
        self.source = 'slovensko'
        self.target = os.environ['LANGUAGE']



    def download(self):
        r =requests.get(BASE_URL.format(self.source, self.target, self.query))
        r.encoding = 'utf-8'
        self.soup = BeautifulSoup(r.text, "html.parser")


    def parse(self):
        items = self.soup.find_all("li", attrs={"class": "leading-7 list-item"})
        if len(items) == 0:
            return None
        translated_items = [item.text.replace('(Pokračovanie pod reklamou)REKLAMA', '').replace('–','→') for item in items]   



        text = '\n'.join(translated_items)
        # if len(text) > self.text_length:
        #     txt = (text[:self.text_length] + '...\n')
        #     link  = '<a href="{}">More... </a>.'.format(BASE_URL.format(self.source, self.target, self.query))
        #     return '{0}\n{1}'.format(txt, link)
        # else:
        #     return text
        return text

    def get_translated_text(self, length= MAX_LENGTH):
        self.download()
        self.text_length = length
        result = self.parse()
        if not result:
            self.source = '{}o'.format(os.environ['LANGUAGE'][:-1])
            self.target = 'slovensky'
            self.download()
            result = self.parse()
        return result


#testing ...
# def main():
#     parser = Parser('Blby')
#     translated_text = parser.get_translated_text(length=MAX_LENGTH)
#     print(translated_text)
    

# if __name__ == '__main__':
#     main()