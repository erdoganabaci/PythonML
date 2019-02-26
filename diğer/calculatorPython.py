def cal(x,y,opr):
	if opr not in "+-*/":
		print("Just use it +-*/")
	if opr == "+":
		print("fsafsa")
		return str(x) + opr + str(y) + "=" + str(x+y)
	if opr == "-":
		return str(x) + opr + str(y) + "=" + str(x-y)
	if opr == "*":
		return str(x) + opr + str(y) + "=" + str(x*y)
	if opr == "/":
		return str(x) + opr + str(y) + "=" + str(x/y)

while True:
	x = int(input("Enter The First Number: "))
	y = int(input("Enter The Second Number: "))
	opr = input("Choose operation :")
	print(cal(x,y,opr))