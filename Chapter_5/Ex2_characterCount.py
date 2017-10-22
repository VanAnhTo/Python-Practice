import pprint

message = 'Today is a beautiful day. The sun is shining and low windy.'
count= {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character]+1

pprint.pprint(count)
#print(pprint.pformat(count))