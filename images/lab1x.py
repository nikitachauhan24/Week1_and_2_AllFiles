''' This is a demo script called lab1x.py.  It’s just a suggestion demonstrating Strings, if statements, and functions.   The area between the quotes is a comment area.  You should use them liberally in your own code to explain and to identify that each section does. '''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

msg1 = bcolors.WARNING+"Welcome to the Lab."+bcolors.ENDC+"  You've selected English."
msg2 = "Bienvenido a la Lección. Has seleccionado español."
msg3 = "欢迎来到课程。 你选择了中文。"
msg4 = "\n\nBye!\n\n"

print("Welcome!  Please select from the following choices:")
print("1 = select English\n2 = Seleccione español\n3 = 选择中文\n4 = Quit  ")
opt = int(input("\tChoice: "))


if opt == 1:
	print(msg1)
elif opt == 2:
	print(msg2)
elif opt == 3:
	print(msg3)
else:
	print(msg4)

print("-"*60)

''' define some functions '''
def messageToUser():
	print("Here are some demos about Strings ... ")

def parseTheString(opt):
	str = bcolors.BOLD+"This is a test of a string.  Let's parse it!"+bcolors.ENDC
	str2 = "Algunas personas de TI no son educadas."
	str3 = "今年夏天的热量肯定很热"
	
	if opt == 1:
		print("\nThe length of the string is \t",len(str))
		print("How many letter 'e's are in the string?\t", str.count("e"))
		print("Let's capitalize and lower-case it: \t", str.upper(), " \n\t", str.lower())
		print("And let's replace every 'e' with a 'q':\t", str.replace('e','q'))
	elif opt == 2:
		print("\nLa longitud de la cadena es \t",len(str2))
		print("¿Cuántas letras e están en la cadena?\t", str2.count("e"))
		print("Vamos a capitalizar y minúsculas: \t", str2.upper(), " \n\t", str2.lower())
		print("Y reemplazemos cada 'e' con una 'q':\t", str2.replace('e','q'))
	elif opt == 3:
		print("\n字符串的长度是 \t",len(str3))
		print("字符串中有多少个字母'串'？\t", str3.count("串"))

def sliceExample():
	print("\n","_"*60)
	print("\n"+bcolors.OKGREEN+ "And here is your lab! ... "+bcolors.ENDC + 
	" Your job is to practice the "+bcolors.BOLD+"slice"+bcolors.ENDC+" command.")
	print("E.g., using str as your string, extract the first 2 letters")
	print("then cause your string to print backwards.")


''' CALL some functions '''
messageToUser()
parseTheString(opt)
sliceExample()

print("-"*60, "\n"*2)
print("That's it for now.  Please continue with the rest of the lab...  cheers")
print("-"*60, "\n"*2)
