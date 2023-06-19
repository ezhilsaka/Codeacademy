songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)

plays['Purple Haze'] = 1

plays.update({'Respect': 94})

library = {'The Best Songs': plays, 'Sunday Feelings': {}}
print(library)

# way to access the invalid key in dictionary

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["energy"])

key_to_check = "energy"

if key_to_check in zodiac_elements:
  print(zodiac_elements['energy'])

#.get method of dictionary to get the value 

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)

stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

######################## Deleting a key in dictionary using pop method ######################

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

hp = available_items.pop("stamina grains", 0)
health_points = health_points + hp

hp = available_items.pop("power stew", 0)
health_points = health_points + hp

hp = available_items.pop("mystic bread", 0)
health_points = health_points + hp

print(available_items)
print(health_points)