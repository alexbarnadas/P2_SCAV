# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess as sp
import os


def print_info():
    line1 = "ffprobe bbb.mp4 2>&1 | grep 'Duration'"#"ffprobe - v error - show_format - show_streams bbb.mp4"
    line2 = "ffprobe bbb.mp4 2>&1 | grep 'Video'"
    line3 = "ffprobe bbb.mp4 2>&1 | grep 'Audio'"

    sp.run(line1, shell=True)
    sp.run(line2, shell=True)
    sp.run(line3, shell=True)


def rename_video():
    path = os.getcwd()+"/"
    print("Choose one of the available files, to rename:\n")

    chosen = path + input("The file I want to rename is called: ")
    new_name = path + input("And I want it to be known as: ")

    os.rename(chosen, new_name)


def custom_resize(name):
    h = input("Height: ")
    w = input("Width: ")
    size = h+"x"+w
    line = 'ffmpeg -i ' + name + ' -s ' + size + ' -c:a copy resize_' + name + size + '.mp4'
    sp.run(line, shell=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("#*#*#*#*# MAIN MENU #*#*#*#*#"
          "\nThe available files in the directory are:")
    sp.run("ls", shell=True)
    opt = int(input("\nThe available functions are:"
                    "\n1. Show file info"
                    "\n2. Rename a file"
                    "\n3. Custom resize"
                    "\nSelect one of them (1-3): "))

    if opt == 1:
        print_info()
    elif opt == 2:
        rename_video()
    elif opt == 3:
        file = input("The name of the file to resize is: ")
        custom_resize(file)
