import os

defaultPackages = "python git httpd"

def install_or_remove_packages():
    iOrR= ""
    while iOrR!= "I" and iOrR!= "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR= input().upper()
        if iOrR== "I":
            iOrR= "install"
        elif iOrR== "R":
            iOrR= "remove"
        print("Entera list of packages to install")
        print("The list should be separated by spaces, for example:")
        print(" package1package2package3")
        print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program")
        packages = input().lower()
        if packages == "default":
            packages = defaultPackages
        if iOrR == "install":
            os.system("sudo dnf install " + packages)
        elif iOrR == "remove":
            while True:
                print("Purge files after removing? (Y/N)")
                choice = input().upper()
                if choice == "Y":
                    os.system("sudo dnf remove " +iOrR + " " + packages)
                    break
                elif choice == "N":
                    os.system("sudo dnf " + iOrR + "" + packages)
                    break
