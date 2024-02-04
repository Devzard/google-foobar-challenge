"""
After completing all the challenges this secret encoded message is recevied.
The message can be decoded using your username as key.
It outputs this dictionary:
{'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}
"""



import base64

MESSAGE = '''
H0IRFBALDAAbQE9dT05eS1wFEUVNU08KHAQLCgYIHFweGV5FRQQAHAwWBQILQENJHlxfAgoQFQBP\nSUlIQAYJDBtcXVAGCQdGX0hOEgsPBgIZDFRcVxBCQltTTxwdBAgMDAoNHhUZQxcDAxEBHQBPR1VH\nSBpYX1xDSUJGFQcGVEhdT0AYAFcYHhk=
'''

KEY = 'debashishgogoi999'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))

### OUTPUT : {'success' : 'great', 'colleague' : 'esteemed', 'efforts' : 'incredible', 'achievement' : 'unlocked', 'rabbits' : 'safe', 'foo' : 'win!'}