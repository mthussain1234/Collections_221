#hero story


story1 = {
    "start": "There was once a superhero who had lost his powers and was afraid he will never be able to use them again",
    "middle": "His mentor had convinced him to face his fears and endure through it as great evil was around the corner",
    "end": "He did not pay much attention at the time, but when turmoil had struck his instinct had kicked in and he managed to save and protect the city...Once Again!"

}

print(story1)
print(type(story1))

print(story1.keys())
print(story1.values())

print(story1["middle"])
print(story1["start"])
print(story1["end"])

story1["hero"] = "Vigil"
print(story1.keys())
print(story1.values())