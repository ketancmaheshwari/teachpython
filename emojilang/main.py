import emodict as ed

#print(ed.emodict.get("grin"))

line = "india pakistan play cricket ."

splitline = line.split()

for i in splitline:
	print(ed.emodict.get(i, i), end=" ")

print()
