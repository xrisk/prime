import ChatExchange.chatexchange.client
import ChatExchange.chatexchange.events
import ChatExchange.chatexchange.browser
from random import choice

class Bot:
    def __init__(self, client, bot, room, welcome_message="Hi There!"):
        self.client = client
        self.room = room
        self.bot = bot
        self.paused = False
        self.welcome = welcome_message
        
    def pause(self):
        self.paused = True
        
    def unpause(self):
        self.paused = False
        
    def is_paused(self):
        return self.paused
    
    def message(self, text):
        if not self.paused:
            self.room.send_message(text)
            
    def greet(self, user):
        programming_languages = ["java", "python", "html", "c++", "bash", "javascript", "vbscript", "php"]
        language = choice(programming_languages)
        username = '@'+user.replace(' ','')+'!'
        
        if language == "java":
            self.message("System.out.println(\"Hello, "+username+"\");")
        elif language == "python":
            self.message("print \"Hello, "+username+"\"")
        elif language == "html":
            self.message("<p>Hello, "+username+"</p>")
        elif language == "c++":
            self.message("std::cout << \"Hello, "+username+"\";")
        elif language == "bash":
            self.message("echo Hello, %"+username+"%")
        elif language == "javascript":
            self.message("document.write('Hello, "+username+"');")
        elif language == "vbscript":
            self.message("WScript.Echo \"Hello, "+username+"\"")
        elif language == "php":
            self.message("<?php echo '<p>Hello, "+username+"</p>'; ?>")
            
    def start(self, callback):
        self.room.watch(callback)

def init_bot(cred):
    
    client = ChatExchange.chatexchange.client.Client(str(cred['host'].encode('utf-8'))[5:])
    client.login(cred['user'], cred['pass'])
    bot = client.get_me()
    room = client.get_room(int(cred['room']))
    room.join()
    return Bot(client, bot, room)
            
        
