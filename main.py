# The code for the Mod GUI
import colors as c
version = open("version.txt", "r")
print(f"{c.acolors.bright_green}Cloudy Client{c.bcolors.ENDC} |{c.acolors.bright_green} v{version.read()} {c.bcolors.ENDC}")
cmd_input=f"{c.bcolors.BOLD} >>> "
version.close()
config_read = open("config.txt", "r")



    

cmd = input(cmd_input)
if cmd == "help":
    print("""help:
    Brings up this menu
    exit:
    destructs the gui
    """)
    cmd = input(cmd_input)
elif cmd == "exit":
    exit(1)

