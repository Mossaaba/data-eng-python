users = ['val', 'bob', 'mia', 'ron', 'ned']
del users[-1]
print(users)
users.remove('mia')
print(users)
users.insert(2, 'mia')
users.insert(4, 'ned')
print(users)

most_recent_user = users.pop()
print(most_recent_user)

print(users)

first_user = users.pop(0)
print(first_user)
print(users)

users.sort()