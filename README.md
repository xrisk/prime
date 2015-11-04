# prime

A Python bot that runs on the StackExchange chatrooms. Inspired by [michaelpri’s](https://github.com/michaelpri10) similar program,  I used [manishearth’s](https://github.com/manishearth) excellent [ChatExchange](https://github.com/manishearth/ChatExchange) Python library. To run the bot, first clone the repo:

`$ git clone https://github.com/xrisk/prime --recursive`

The bot is written for Python2, so make sure you have that. Then, 

`python prime.py`

It’ll ask for your StackExchange email and password. Remember that only accounts with 20 rep can speak in the chatrooms.

```
$ python prime.py
SET UP CREDENTIALS FOR PRIME
Enter your Stack Overflow email ID: rishav.kundu98@gmail.com
Enter your Stack Overflow password: (hidden)
Enter the ID of the room you wish to enter: 85048
1 chat.exchange.com
2 chat.meta.stackoverflow.com
3 chat.stackoverflow.com
Enter the host site for Prime: 3
{'host': u'chat.stackoverflow.com', 'room': '85048', 'user': 'rishav.kundu98@gmail.com', 'pass': ';)'}
PRIME HAS STARTED
>> 

```

Type `die` at the prompt there, to well, kill the bot. 😧 Anything else at the prompt will be echoed to the chatroom.

For your convenience, prime can set itself up from  environment variables. You need to set `ChatExchangeU`, `ChatExchangeP`, `RoomID`, and `HostSite` in your env appropriately. Beware that `HostSite` must be one of the _values_ (**not** keys) defined in [hosts.json](https://github.com/xrisk/prime/blob/master/credentials/hosts.json).

## Extending prime

Want to add a new command to prime? Well, I’ve made it ridiculously simple for you to do just that. You need to do two things: 

- Add a new key-value pair to modules.json. For example, 
 `"//echo": "echo.py"`. The key is what you need to type in the chatroom to trigger the command, and the value is the name of the python script that gets called by prime.

- Create that same python script  inside the `modules` folder. It should have a function called `main` which takes two arguments, and returns one string. Here’s the contents of `echo.py` as I would write it;

```
def main(message, priv=False):
	return 'You said: ' + message
```
The first variable will contain the input to the command, as passed in the _chatroom_. So, if someone types

```
//echo I’m batman!
```

in the chatroom, your script will receive `I’m batman!` in `message`. `priv` will a bool depending on whether the user who typed that command is “privileged.” This feature is not implemented yet, and `priv` will always be `False`.


And that’s it! prime will now respond to the `echo` command. Nice and modular, isn’t it?

