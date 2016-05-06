import Main
import os


if __name__ == "__main__":

    with open("Files/outputs/our_optimized_results.txt", 'w') as results_file:
        str = ""
        for file in os.listdir("Files/"):
            if file.endswith(".txt"):
                str += Main.main((file, 'optimized'))
        results_file.write(str)

    with open("Files/outputs/our_basic_results.txt", 'w') as results_file:
        str = ""
        for file in os.listdir("Files/"):
            if file.endswith(".txt"):
                str += Main.main((file, 'basic'))
        results_file.write(str)

