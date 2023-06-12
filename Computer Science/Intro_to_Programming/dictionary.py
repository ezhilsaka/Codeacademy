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