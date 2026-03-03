song = {
    "hero" : 1980,
    "zero" : 1989,
    "wah"  : 1992
}

print(song["hero"])
song["new"] = 2000
print(song)
song["wah"] = 2010
print(song)

del song["wah"]
print(song)

print("wah" in song)
print("hero" in song)

print(song.keys())
print(song.values())

me = { 
    "name": "Durjoy", #keys is immutable so list cannot be key but tuple can
    "age" : 22,
    "skills": ["python", "c++"],
    "score" : 95,
    "backscore" : 95
}
print(me)

