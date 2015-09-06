"""
prime.

A chatbot which can be run in the rooms of stackoverflow.com
This file contains the `main` function which launches the bot.
Also contained are auxillary methods for the dynamic loading of commands.

"""

import Bot
import ChatExchange.chatexchange.events
import credentials
import imp
import json
import os
import shelve
import sys
import thread
import time

bot = None
modules = None
privileged = []


def open(file, mode='r', buffering=-1):
	"""Hacky solution to resolve relative path imports. NOT for client use."""
	import __builtin__
	import os.path
	file_path = os.path.join(os.path.dirname(__file__), file)
	return __builtin__.open(file_path, mode, buffering)


def init_modules():
	"""
	Dynamically loads modules by reading the `modules.json` file.

	Uses `inp` to parse .py files specified by `modules.json`.
	Modules are then made available to the global namespace
	using `import` in conjunction with `exec`.
	"""
	global modules
	try:
		cur_path = os.path.join(
			os.path.dirname(os.path.abspath(__file__)), 'modules')
		modules = json.loads(open('modules.json').read())
		for i in modules:
			imp.load_source(i[2:], os.path.join(cur_path, modules[i]))
			exec('import ' + i[2:], globals())
	except IOError, e:
		print e
	except ValueError, e:
		print e


def init_privileged():
	"""
	Populate the `privileged` list.

	Previously pickled User IDs are read from the privileged-users.db file.
	"""
	global privileged
	f = shelve.open('privileged-users.db')
	for i in f:
		privileged.add(i)
	i.close()


def main():
	"""
	An interactive function that starts the bot.

	Initialises modules, populates `privileged`, and launches the bot.
	Blocks indefinitely till the `die` command is supplied at sys.stdin`
	"""
	global bot
	global modules
	init_modules()

	while True:
		creds = credentials.get()
		print creds
		if credentials.validate(creds):
			break

	bot = Bot.init_bot(creds)
	bot.start(on_event)
	print 'PRIME HAS STARTED'
	bot.message("I'm alive :)")
	while True:
		if 'no-input' not in sys.argv:
			text = raw_input(">> ")
			if text == "die":
				print 'PRIME HAS STOPPED RUNNING'
				bot.message("I'm dead :(")
				time.sleep(0.4)
			break
		else:
			bot.message(text)

	os._exit(6)


def on_event(event, client):
	"""Receive events fired by the bot and bubble them to appropriate handlers."""
	if isinstance(event, ChatExchange.chatexchange.events.UserEntered):
		on_enter(event)
	elif isinstance(event, ChatExchange.chatexchange.events.MessagePosted):
		on_command(bot, event)


def on_enter(event):
	"""The handler for when a user enters the chatroom being watched."""
	print "User Entered"
	if event.user.id == bot.bot.id or event.user.reputation < 20:
		pass
	else:
		bot.greet(event.user.name)


def on_command(bot, event):
	"""The handler for when a message is posted."""
	text = event.content
	tokens = text.split()
	if len(tokens) >= 1:
		command = tokens[0]
		if command in modules:
			command = tokens[0][2:]
			func = eval(command + '.main')
			if event.user.id in privileged:
				thread.start_new_thread(threaded_command, tuple([bot, func, event, True]))
			else:
				thread.start_new_thread(threaded_command, tuple([bot, func, event, False]))


def threaded_command(bot, func, event, priv):
	"""
	Execute the funtion object `func` and blocks till completion.

	`func` is determined by `on_command`.
	The function replies to the message with the string returned by `func`.
	"""
	text = event.content
	string = text[text.find(' '):].strip()
	event.message.reply(func(string, priv))

if __name__ == '__main__':
	main()
