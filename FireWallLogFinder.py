import time
string = 'Empty'
log_input = []

def finding(fstring):
    start_time = time.time() 
    ofile = open(log_output, 'w')
    for file in log_input:
        with open (file , 'r' , encoding='latin-1') as infile:
            for line in infile:
                if "!@#$end" not in line:
                    if fstring in line:
                        ofile.write(line)
                else:
                    break
    ofile.close()
    print("The job has been finished and {} has been created".format(log_output))
    print("\n--- %s seconds ---" % (time.time() - start_time))

def entring():
    log_input = []
    start_time = time.time()
    print("\nPlease enter yor files name each on one line and press enter.when you done please type end ")
    i = 1
    while True:
        l = input()
        if l == 'end' or 'End' or 'END' or '' :
            break
        print('\n', i, '> ', l)
        log_input.append(l)
        i = i + 1
    for file in log_input:
        ifile = open(file,'a', encoding='latin-1')
        ifile.write('!@#$end')
        ifile.close()
    print("\n--- %s seconds ---" % (time.time() - start_time))
    return(log_input)

while True:
    print("----------------------------------------------------------------------------------------------------------")
    inp = input("Log Finder By Rlabrmm\n1-Input Files Name\n2-Run\n3-Exit\n")
    if inp == '1':
        try:
            log_input = entring()
        except IOError: 
            print("It looks some thing goes wrong. Please check your Files Name.")
    elif inp == '2':
        try:
            string = input("Please enter Your finding string: ")
            log_output = string + '.txt'
            finding(string)
        except IOError: 
            print("It looks some thing goes wrong. Please check your Files Name or finding string.")
    elif inp == '3':
        print("Bye")
        break
    else:
        continue
        
