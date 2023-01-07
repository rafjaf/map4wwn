#!/usr/local/bin/python3
# Map4WWN 0.1-2023-01-07

import random

DEFAULT_NUMBER_OF_ROOMS = 12
# NUMBER_OF_EXITS = [1, 1, 2, 2, 3, 3, 3, 4]
NUMBER_OF_EXITS = [1, 1, 1, 2, 2, 3]
ROOM_CONTENT = [" (C) (T)", " (C)", " (H)", " (E)", " (D)", " (D)", "", ""]
ROOM_DESCRIPTION = [
	[
		"Residential Room", 
		[
			"Dormitory barracks for servants",
			"The owner or ruler's bedchamber",
			"High-ranking resident bedroom",
			"Latrine or privy",
			"Kennel or beast pen",
			"Prison or slave cages",
			"Meager room for minor servant",
			"Sickroom for patients",
			"Guest chambers for visitors",
			"Kitchen or dining hall",
			"Bathing chamber or washroom",
			"Study or private library"
		]
	],
	[
		"Work Room",
		[
			"Smithy or forge",
			"Smokehouse or food preparation",
			"Sewing or weaving room",
			"Torture chamber",
			"Healer's work room",
			"Arcane laboratory",
			"Alchemist's workshop",
			"Artistan's workshop",
			"Artist's workshop",
			"Washroom or scullery",
			"Brewery room",
			"Processing room for raw good"
		]
	],
	[
		"Cultural Room",
		[
			"Plaza or meeting area",
			"Amphitheatre or recital room",
			"Art gallery",
			"Cultural monument",
			"Grave, cemetery, ossuary",
			"Library or archive",
			"Garden or flowing water feature",
			"Ornately iconographic chamber",
			"Room for a particular cultural rite",
			"Drinking hall",
			"Performance stage or area",
			"Drug den or place of debauchery"
		]
	],
	[
		"Martial Room",
		[
			"Armory or martial storage",
			"Training area",
			"Barracks for soliders",
			"Guard post",
			"Parade ground",
			"Commemorative hall",
			"Map or planning room",
			"War machine fabrication or storage",
			"Dueling area",
			"Beast-fighting arena",
			"Strong point or fortification",
			"Gate or fortified entrance"
		]
	],
	[
		"Religious Room",
		[
			"Private shrine",
			"Altar room",
			"Monastric prayer cell",
			"Ritual chamber",
			"Monument to a deity",
			"Ceremonial bath",
			"Room for a labor holy to the god",
			"Storage for religous equipage",
			"Secured chamber for holy relics",
			"Secret or unoffical chapel",
			"Priest's private chambers",
			"Public area adorned with icons"
		]
	],
	[
		"Utility Room",
		[
			"Work material storage",
			"Pantry or food storage",
			"Storeroom for random detritus",
			"Furnace or boiler room",
			"Exotic ancien power or light room",
			"Pool or water source room",
			"Concealed servant's passage",
			"Domestic staff head office",
			"Vault for valuables",
			"Secret or unobstrusive entrance",
			"Grand passage or ornate corridor",
			"Barn or fodder storage"
		]
	]
]

class Room:
	def __init__(self):
		self.number = 0
		self.category = ""
		self.description = ""
		self.content = ""
		self.adjacent_rooms = []
		self.exits = 0

def main():
	# Ask for parameters
	answer = input(f"How many rooms of interest will the dungeon contain? (Default: {DEFAULT_NUMBER_OF_ROOMS}) ")
	try:
		number_of_rooms = int(answer)
	except ValueError:
		number_of_rooms = DEFAULT_NUMBER_OF_ROOMS
	answer = input(f"Do you wish room description to be included in the map? (YES/no) ")
	try:
		insert_description = True if answer[0].lower == "y" else False
	except:
		insert_description = True
	# Determine rooms
	rooms = []
	for i in range(number_of_rooms):
		r = Room()
		r.number = i
		rooms.append(r)
	for i in range(number_of_rooms):
		r = rooms[i]
		# Determine room description
		cat = random.randrange(0,len(ROOM_DESCRIPTION))
		r.category = ROOM_DESCRIPTION[cat][0]
		subcat = random.randrange(0,len(ROOM_DESCRIPTION[cat][1]))
		r.description = ROOM_DESCRIPTION[cat][1][subcat]
		# Determine room content
		r.content = ROOM_CONTENT[random.randrange(0,len(ROOM_CONTENT))]
		if len(r.content) and r.content[2] != "C" and random.randrange(0,5) == 0:
			r.content += " (T)"
		# Determine exits
		exits = NUMBER_OF_EXITS[random.randrange(0,len(NUMBER_OF_EXITS) - 1)]
		for j in range(exits):
			current_room = i
			room_to_add = random.randrange(0, number_of_rooms)
			while room_to_add == current_room:
				room_to_add = random.randrange(0, number_of_rooms)
			if room_to_add not in rooms[current_room].adjacent_rooms \
				and current_room not in rooms[room_to_add].adjacent_rooms \
				and rooms[current_room].exits < 4 \
				and rooms[room_to_add].exits < 4:
					rooms[current_room].exits += 1
					rooms[room_to_add].exits += 1
					rooms[current_room].adjacent_rooms.append(room_to_add)
	# Export map in Mermaid style 
	print("\ngraph BT")
	if insert_description:
		for i in range(number_of_rooms):
			if len(rooms[i].adjacent_rooms):
				for j in range(len(rooms[i].adjacent_rooms)):
					if j == 0:
						print(f'\tR{i+1}["{i+1}. {rooms[i].description}{rooms[i].content}"] --- R{rooms[i].adjacent_rooms[j]+1}')
					else:
						print(f'\tR{i+1} --- R{rooms[i].adjacent_rooms[j]+1}')					
			else:
				print(f'\tR{i+1}["{i+1}. {rooms[i].description}{rooms[i].content}"]')
	else:
		for i in range(number_of_rooms):
			if len(rooms[i].adjacent_rooms):
				for j in range(len(rooms[i].adjacent_rooms)):
					if j == 0:
						print(f'\tR{i+1}["{i+1}{rooms[i].content}"] --- R{rooms[i].adjacent_rooms[j]+1}')
					else:
						print(f'\tR{i+1} --- R{rooms[i].adjacent_rooms[j]+1}')					
			else:
				print(f'\tR{i+1}["{i+1}{rooms[i].content}"]')
		print("\nRooms description:")
		for i in range(number_of_rooms):
			print(f"{i+1}. {rooms[i].category}: {rooms[i].description}")
	print("\nMap can be displayed in any Mermaid editor such as https://mermaid.live/")

if __name__ == "__main__":
	main()
