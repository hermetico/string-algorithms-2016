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

    print "RESULTS"
    equal = False
    with open("Files/outputs/our_optimized_results.txt", 'r') as optimized:
        with open("Files/outputs/our_basic_results.txt", 'r') as basic:
            if optimized.read() == basic.read():
                print "Optimized and basic results ARE EQUAL"
                equal = True
            else:
                print "Optimized and basic results ARE NOT EQUAL"

    if equal:
        print "comparing with .out files"
        with open("Files/outputs/our_optimized_results.txt", 'r') as optimized:
            for line in optimized.readlines():
                #line = line.split(' ')
                #filename = line[0].replace(':', '')
                #branching = line[1]
                #non_branching = line[2]
                filename, branching, non_branching = line.split(' ')

                filename = "Files/outputs/" + filename.replace('.txt:', '.out')

                if not os.path.isfile(filename):
                    continue

                with open(filename, 'r') as f:
                    lines = f.readlines()    # Read all lines
                    # loops through the last line
                    n = -1
                    last = lines[n]
                    while last == '\n':
                        n -=1
                        last = lines[n]


                    f_branching, f_nonbranching = last.split(' ')

                    if branching == f_branching and non_branching == non_branching:
                        print "%s OK" % filename
                    else:
                        print "%s NO OK" % filename