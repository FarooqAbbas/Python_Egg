import random
#greetings=['Hello','Hi','Hey','Howdy','Hola']
colors=['Red','Black','Green']
#value = random.uniform(1,10)
#valueInt=random.randint(1,10)
results=random.choices(colors)
#value= random.choice(greetings)
#print(value + ',Farooq!')
deck=list(range(1,53))
random.shuffle(deck)
print(deck)