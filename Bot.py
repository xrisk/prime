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
        self.message('@'+user.replace(' ','')+' '+self.welcome)
            
    def start(self, callback):
        self.room.watch(callback)
        