import sys
import os
import time
import telepot
import requests
import pafy

TOKEN = "1303414146:AAE309nEKwqQNxQWtdjalMj4ySF6lAmN13I"
vid = 'https://cdn-35.uplovd.com/l2J2JcQ6o3/a42385bc-1599631409/file_3037.mp4'
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    flavor = telepot.flavor(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print (flavor, summary)
    
    order = msg['text'].split(' ')
    title = ''
    url = ''
    flag_URL = 0
    flag_VIDEO = 0
    for text in order:
    	if text.startswith('https://') or text.startswith('www.') or text.startswith('youtu') or text.startswith('http://'):
    		url = text
    		flag_URL = 1
    	else:
            for i in range(text.find('http',len(text))):

                url = url + text[i]
                flag_URL = 1           
            
    	 
    if flag_URL == 1:
        video = pafy.new(url)
        best = video.getbest()
        message = video.title + '\t(' + video.duration + ')'
        bot.sendMessage(chat_id, message)
        if flag_VIDEO == 0:
            r = requests.get('http://tinyurl.com/api-create.php?url=' + best.url)
            message = 'Download Video: ' + str(r.text)
            bot.sendVideo(chat_id, r.text,reply_to_message_id=msg['message_id']) 
    for text in order:
        if 'surish' in text:
            bot.sendVideo(chat_id, vid,reply_to_message_id=msg['message_id'])
    
    
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

while 1:
    time.sleep(10)
