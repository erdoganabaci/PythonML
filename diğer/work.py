name = input("Enter a name :")
print("Hoşgeldin Mr"+name+"Enjoy time")
secret_word = "Erdogan"
gues_stirng = ""
lives = 10

while lives > 0:
	character_left=0
	for character in secret_word:
		if character in gues_stirng:
			print(character)
		else:
			print("-")
			character_left+=1
	if character_left==0:
		print("Kazandın!!")
		break
	gues=input("Tahmin Et:")
	gues_stirng+=gues

	if gues not in secret_word:
		lives -=1
		print("Yanlış Tahmin")
		print(f"{lives} canın kaldı")
		if lives==0:
			print("Öldün")