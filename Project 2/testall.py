__author__ = 'ballololz'
import Main
import os


if __name__ == "__main__":
    fd = os.open("Files/outputs/our_optimized_results.txt", os.O_CREAT|os.O_RDWR)
    str = ""
    for file in os.listdir("Files/"):
        if file.endswith(".txt"):
            str += Main.main((file,))

    os.write(fd,str)