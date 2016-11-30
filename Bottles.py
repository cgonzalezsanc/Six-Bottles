class Bottles:

	def song(self, beverage = 'beer'):
		return self.verses(99,0, beverage)

	def verses(self, last, first, beverage = 'beer'):
		o = self.verse(last, beverage)
		for i in range (last-1, first-1, -1):
			o += "\n" + self.verse (i,beverage) 
		return o

	def verse(self, number = None, beverage = 'beer'):
		if number == 0:
			return """No more bottles of {0} on the wall, no more bottles of {0}.
Go to the store and buy some more, 99 bottles of {0} on the wall.
""".format(beverage)
		elif number == 1:
			return """1 bottle of {0} on the wall, 1 bottle of {0}.
Take it down and pass it around, no more bottles of {0} on the wall.
""".format(beverage)
		elif number == 2:
			return """2 bottles of {0} on the wall, 2 bottles of {0}.
Take one down and pass it around, 1 bottle of {0} on the wall.
""".format(beverage)
		elif number == 6:
			return """1 six-pack of {0} on the wall, 1 six-pack of {0}.
Take one down and pass it around, no more six-pack of {0} on the wall.
""".format(beverage)
		else:
			return """{0} bottles of {2} on the wall, {0} bottles of {2}.
Take one down and pass it around, {1} bottles of {2} on the wall.
""".format(number, number-1, beverage)



        
