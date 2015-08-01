from random import choice
quotes = ["Billions of Blue Blistering Barnacles!", "Blue Blistering Bell-Bottomed Balderdash!", "Dunderheaded coconuts!", "Fuzzy wuzzy!",
		  "Great flat-footed grizzly bear!", "Ten thousand thundering typhoons!"]


def main(s, priv=False):
	return "{} It's alive!".format(choice(quotes))