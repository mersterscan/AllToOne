try:
    from os import system , listdir
    from os.path import isfile,join , splitext
except:
    print("[+]: Error In Importing The OS Libbrary !")
try:
    from colorama import Fore as TextColor
except:
    print(TextColor.BLUE + "[!]: The Colorama Library Is Not Installed In Your Computer , Installing The Colorama..")
    system("pip install colorama")
try:
    from time import sleep as Wait
except:
    print("[+]: The time Library Is Not Installed In Your Computer , Installing The time..")
    system("pip install time")
# ---------------------------------

system("cls" or "clear")

print(TextColor.YELLOW + "</-------------------------------------------------------/>\n\n [$]: Be Barname Tarkib File Text Khosh Amadid ! \n \n [I]: In Barname Jahat Tarkib Chandin File Text Ba Ham Estefade Mishavad \n \n [!]: Baraye Estefade Az In Barname Shoma Bayad Az Mavared Zir Peyravi Konid: \n \n [1]: Tamami File Haye Text { .txt } Dar Yek Pushe Bashand \n \n [2]: Adress Pushe Ra Bayad be tor Daghigh Vared Konid! \n \n [Example]: C:/Users/AliReza/Desktop/Folder \n\n</-------------------------------------------------------/> \n\n ")

Folderloc = input(TextColor.GREEN + "[F]: Lotfan Mahal Folder Ra Vared Konid -> ")

AllFiles = [f for f in listdir(Folderloc)]

Texts = []

for i in AllFiles:
    name , ext = splitext(i)
    
    if ext == '.txt':
        
        Texts.append(i)
        
for TXTFile in Texts:
    
    OpenTXT = open(Folderloc + '/' + TXTFile , 'r')
    
    NewFile = open(Folderloc + "/NewTXT.txt" , 'a')
    
    NewFile.write(OpenTXT.read() + "\n")
    
print("[+]: Tamam File Ha Darun File NewTXT Gonjande Shod.!")