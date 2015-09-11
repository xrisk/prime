"""
Module containing the definintion for `Credential` objects.

This module contains the class prototype for `Credential` objects,
which are required to initialise instances of `Bot`.

Also present are the functions
`read` which inputs credentials from sys.stdin via prompts,
and `validate` which checks whether this particular `credential` instance
contains valid credentials.
"""

import getpass

class Credential:

	"""
	Store a email/password/hostsite tuple.

	`Credential` objects may be initialised either via the constructor,
	or using the utility function `read` present in the `credential` module.

	'Credential' objects are immutable and behaviour is undefined
	if attributes are modified after initialisation.

	Instance properties may be accessed directly. No getters are defined.

	`Credential` objects may be used for initialising instances of Bot.
	"""

	def __init__(self, email, password, host):
		"""
		The constructor for `Credential` instances.

		Throws `ValueError` if the passed arguments are not valid,
		as defined in `validate` (see docstring).

		@email=a email with an account at StackExchange
		@password=the password associated with StackExchange account
		@host=the StackExchange site to join (valid strings are defined in hosts.txt)
		"""
		self.email = email
		self.password = password
		self.host = host

		try:
			validate(self)
		except ValueError:
			del self.email
			del self.password
			del self.host
			raise


def validate(x):
	"""
	Check validity of a `Credential` instance.

	Type checks are made on x.email, x.password and x.host.
	All three must have types of `str`.

	In addition, the existance of x.host in hosts.txt is checked.
	"""
	if type(x.email) is not str:
		raise ValueError
	if type(x.password) is not str:
		raise ValueError
	if type(x.host) is not str:
		raise ValueError

	with open('hosts.txt') as f:
		for line in f:
			if line == x.host and line.strip() != '':
				return True
	return False


def read():
	"""Prompt-based function to read in from sys.stdin."""
	e = raw_input("Enter your StackExchange email ID >> ")
	p = getpass.getpass("Enter your StackExchange password >> ")
	possible_hosts = []
	with open('hosts.txt') as f:
		for line in f:
			possible_hosts.append(line.strip())

	possible_hosts = filter(lambda x: x != '', possible_hosts)
	for i in range(len(possible_hosts)):
		print i + 1, possible_hosts[i]
	h = raw_input("Enter a choice of host site >> ")
	while not (h.isdigit() and 1 <= int(h) <= len(possible_hosts)):
		print "Invalid option."
		h = raw_input("Enter a choice of host site >> ")
	return Credential(e, p, possible_hosts[int(h)])
