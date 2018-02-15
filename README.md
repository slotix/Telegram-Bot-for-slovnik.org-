# Telegram-Bot-for-slovnik.org-
Tento bot prekladá slová z ruštiny do slovenčiny a zo slovenčiny do ruštiny.

Этот бот переводит слова с русского на словацкий и со словацкого на русский.

![screenshot 2016-03-14 23 41 57](https://cloud.githubusercontent.com/assets/684169/18109372/3fb63ad0-6f11-11e6-8c9b-ccd4f1e1cccf.jpg)


This bot uses python-telegram-bot wrapper from 
https://github.com/python-telegram-bot/python-telegram-bot

Thanks to http://slovnik.sk for their awsome dictionary.  

1. Create a new bot and get your Telegram bot HTTP API token. 
Find more info at https://core.telegram.org/bots#6-botfather  
2. Create new .env file with specified settings. See .example.env
3. Initialise your TOKEN = '' variable with newly generated value.
The token is a string looks like 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw that will be required to authorize the bot and send requests to the Bot API.
4. OUTPUT_LIMIT trims output to OUTPUT_LIMIT chars
5. specify LANGUAGE : 'anglicky', 'nemecky', 'francuzsky', 'spanielsky', 'madarsky', 'taliansky', 'rusky'
6. Launch pyhton slovnik.py
