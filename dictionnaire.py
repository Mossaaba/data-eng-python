users = []
new_user = {
 'last': 'fermi',
 'first': 'enrico',
 'username': 'efermi',
 }
users.append(new_user)

new_user = {
 'last': 'curie',
 'first': 'marie',
 'username': 'mcurie',
 }
users.append(new_user)

for user_dict in users:
    for key, value in user_dict.items():
        print(key + ': ' + value)
    print('\n')


### Nesting list 

fav_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
}


for name, languages in fav_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

## Nesting dictionnaire in dictionnaire

users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

for username, user_info in users.items():
 print("\nUsername: " + username)
 full_name = user_info['first'] + " " + user_info['last']
 location = user_info['location']

 print("\tFull name: " + full_name.title())
 print("\tLocation: " + location.title())       



# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])

# alien_color = alien_0.get('color', 'No color assigned')

# print(alien_0)
# del alien_0['points']
# print(alien_0)


# fav_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# # Show each person's favorite language.
# for name, language in fav_languages.items():
#  print(name + "'s favorite language is " + language.title() + ".")


aliens = []
# Make a million green aliens, worth 5 points
# each. Have them all start in one row.
for alien_num in range(1000000):
 new_alien = {}
 new_alien['color'] = 'green'
 new_alien['points'] = 5
 new_alien['x'] = 20 * alien_num
 new_alien['y'] = 0
 aliens.append(new_alien)
# Prove the list contains a million aliens.
num_aliens = len(aliens)
print("Number of aliens created:")
print(num_aliens)
for alien in aliens:
    print(alien)
