"""This module contains the `Bot` class, and `init_bot` utility method."""

import ChatExchange.chatexchange.browser
import ChatExchange.chatexchange.client
import ChatExchange.chatexchange.events
import random


class Bot:

	"""
	A high level wrapper for the chatbot.

	Notable methods included are `message` and `greet`.
	"""

	def __init__(self, client, room):
		"""
		Constructor for the `Bot` class.

		@client=instance of `ChatExchange.chatexchange.client`
		@room=room ID to join
		"""
		self.bot = self.client.get_me()
		self.client = client
		self.paused = False
		self.room = self.client.get_room(room)
		self.room.join()

	def pause(self):
		"""Pause the bot, has no effect if already paused."""
		self.paused = True

	def unpause(self):
		"""Unpause the bot, has no effect if not paused."""
		self.paused = False

	def is_paused(self):
		"""Return the pause state of the bot."""
		return self.paused

	def message(self, text):
		"""Send a message to the current room. Ignore if paused."""
		if not self.paused:
			self.room.send_message(text)

	def greet(self, user):
		"""Greet a user."""
		username = '@' + user.replace(' ', '')
		self.message("Welcome to the Teenage Territory, " + username + "!")

	def start(self, callback):
		"""Start watching the room for events, sending them to `callback`."""
		self.room.watch(callback)


def init_bot(cred):
	"""Utility method to generate a `Bot` object from a valid dictionary."""
	client = ChatExchange.chatexchange.client.Client(
		str(cred['host'].encode('utf-8'))[5:])
	client.login(cred['user'], cred['pass'])
	return Bot(client, int(cred['room']))
