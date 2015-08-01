from Bot import Bot
import time
import ChatExchange.chatexchange.client
import ChatExchange.chatexchange.events
import ChatExchange.chatexchange.browser
import thread
import os

bot = None
modules = None
privileged = []

def get_credentials():
    import os
    res = {}
    
    if 'ChatExchangeU' in os.environ:
        res['user'] = os.environ['ChatExchangeU']
    else: 
        res['user'] = raw_input('Enter your Stack Overflow email ID:')
    
    if 'ChatExchangeP' in os.environ:
        res['pass'] = os.environ['ChatExchangeP']
    else:
        res['pass'] = (raw_input('Enter your Stack Overflow password:'))
        
    if 'RoomID' in os.environ:
        res['room'] = (os.environ['RoomID'])
    else:
        res['room'] = (raw_input('Enter the ID of the Room which you wish to enter:'))
                   
    if 'HostSite' in os.environ:
        res['host'] = (os.environ['HostSite'])
    else:
        import json
        try:
            hosts = json.loads(open('hosts.json').read())
        except:
            return None
        print "Welcome Bot Host Site Options"
        for i in hosts:
            print i, hosts[i]
        print "What will be your Welcome Bot's host site?"
        try:
            res['host'] = hosts[raw_input().strip()]

        except KeyError:
            res['host'] = "invalid" 
    return res
    
def validate_credentials(c):
    
    if type(c) is not dict:
        return False
    if c['host'] == 'invalid':
        return False
    
    try:
        room = int(c['room'])
        return True
    except Exception, e:
        print e
        return False
    
def init_bot(cred):
	
    client = ChatExchange.chatexchange.client.Client(str(cred['host'].encode('utf-8'))[5:])
    client.login(cred['user'], cred['pass'])
    bot = client.get_me()
    room = client.get_room(int(cred['room']))
    room.join()
    return Bot(client, bot, room)
            

def init_modules():
    import json, imp, os
    global modules
    try:
        cur_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modules')
        modules = json.loads(open('modules.json').read())
        for i in modules:
            s = imp.load_source(i[2:], os.path.join(cur_path, modules[i]))
            exec('import '+i[2:], globals())
            # print i[2:]
            
    except IOError, e:
       
        print e
    except ValueError, e:
    	print e
    
def init_privileged():
    import shelve
    global privileged
    f = shelve.open('privileged-users.db')
    for i in f:
        privileged.add(i)
    i.close()


def main():
   
    global bot
    global modules
    init_modules()
                 
    while True:
        creds = get_credentials()
        print creds
        if validate_credentials(creds) == True: break

    bot = init_bot(creds)
    bot.start(on_event)
    
    while True:
        text = raw_input(">> ")
        if text == "die":
            bot.message("I'm dead :(")
            time.sleep(0.4)
            break
        else:
            bot.message(text)

    os._exit(6)


def on_event(event, client):
   
    if isinstance(event, ChatExchange.chatexchange.events.UserEntered):
        on_enter(event)
    elif isinstance(event, ChatExchange.chatexchange.events.MessagePosted):
        on_command(bot, event)


def on_enter(event):
    print "User Entered"
    if event.user.id == bot.bot.id or event.user.reputation < 20:
        pass
    else:
        bot.greet(event.user.name)



def on_command(bot, event):
    text = event.content;
    tokens = text.split()
    if len(tokens) >= 1:
        command = tokens[0]
        if command in modules:
            command = tokens[0][2:]
            func = eval(command+'.main')
            if event.user.id in privileged:
                thread.start_new_thread(threaded_command, tuple([bot, func, event, True]))
            else:
                thread.start_new_thread(threaded_command, tuple([bot, func, event, False]))

def threaded_command(bot, func, event, priv):
    text=event.content
    string = text[text.find(' '):].strip()
    event.message.reply(func(string, priv))

if __name__ == '__main__':
    main()
