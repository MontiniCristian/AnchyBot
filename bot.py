# Copyright (c) 2017 Montini Cristian

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import telepot
from config import TOKEN, DEBUG_MODE, WHITE_LIST, ERROR_CONTACTS, CONTACTS
from telepot.loop import MessageLoop
from tools.parser import parser
import time
import threading
from tools.keygen import keygen

LOG = open("anchy.log", "a")


def handle(msg):
    """
        This function handle the text sent by an User.
        By now it give access on at my User
        @:param msg
    """
    now = time.strftime("%c")
    content_type, chat_type, chat_id = telepot.glance(msg)
    # ----------------------------------------------------------------------------------------------------

    # In this point on the function is checked the username
    # by searching into a WHITE_LIST declared in config.py
    # and then write on the log file.

    if str(msg['chat']['username']) not in WHITE_LIST:
        if '/start' in msg['text']:
            bot.sendAudio(chat_id, open('/home/debian/AnchyBot/Media/Audio/Anchy', 'rb'))

        if DEBUG_MODE:
            bot.sendMessage(304537207, 'Accesso bloccato ' + str(msg['chat']['username']) + "-->" + msg['text'])

        bot.sendMessage(chat_id, " Access Denied!\nYou're not allowed to use me\n" + CONTACTS)
        LOG.write("[" + str(now) + "] " + msg['chat']['username'] + " Access Denied!\n")
        return

    # ----------------------------------------------------------------------------------------------------

    # At this point of the function start the conversation
    # with an authenticated @username.

    else:

        if '/start' in msg['text']:  # Use relatives path declared in config.py
            bot.sendAudio(chat_id, open('/home/debian/AnchyBot/Media/Audio/Anchy', 'rb'))

        if DEBUG_MODE:
            bot.sendMessage(304537207, str(msg['chat']['username']) + "--> " + msg['text'])

        LOG.write("[" + str(now) + "] " + str(msg['chat']['username']) + "--> " + msg['text'] + "\n")
        if content_type == 'text':
            query = parser(msg['text'])

            if query == "Document":
                bot.sendDocument(chat_id, open("scan.pdf", "rb"))
                return

            if "_voice.mp3" in str(query):
                try:
                    bot.sendAudio(chat_id, open(query, "rb"))
                except Exception as e:
                    bot.sendMessage(chat_id, ERROR_CONTACTS)
                    raise e

                return

            if not query:
                return

            else:
                bot.sendMessage(chat_id, query)
                return


# --------------------------------------------------------------------------------------------------------

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

try:
    while 1:
        time.sleep(10)

except KeyboardInterrupt as e:
    LOG.close()
