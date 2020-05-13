# DNA analysis
from time import sleep
sample = ["GTA", "GGG", "CAC"]

# Method to take a file, read it, add it's contents to an empty string and return the updated string.
def read_dna(dna_file):
    # check if file already exists, delete if exists
    import os
    if os.path.exists(dna_file):
        print("File exists")
        read_dna.exist = True 
        dna_data = ""
        with open(dna_file, "r") as f:
            for line in f:
                dna_data += line
        return dna_data
        print("Read file")             
    else:
        print("File does not exist")
        read_dna.exist = False
        
# Method to take a string, create a list of condons and return the list.
def dna_condons(dna):
    condons = []
    for i in range(0, (len(dna)), 3):
        if (i + 3) <= len(dna):
            condons.append(dna[i:(i+3)])
    return condons

# Method to iterate through both the sample and suspect's DNA.
def match_dna(dna):
    matches = 0
    for condon in dna:
        if condon in sample:
            matches += 1
    return matches

# Method to check whether sample matches suspect dna
def is_criminal(dna_sample):
    dna_data = read_dna(dna_sample)
    print(read_dna.exist)
    if read_dna.exist == True:
        condons = dna_condons(dna_data)
        num_matches = match_dna(condons)
        if num_matches >= 3:
            print("%s matches found. Carry on the investigation." % (num_matches))
        else:
            print("%s matches found. Free the suspect." % (num_matches))
    else:
        print("file incorrect")
    

#is_criminal("suspect1.txt")
#is_criminal("suspect2.txt")
#is_criminal("suspect3.txt")
#is_criminal("suspect4.txt")
#is_criminal("suspect5.txt")

# Method for DNA replication
def replication(dna_strand):
    original_strand = read_dna(dna_strand)
    #print(ladder1)
    opposite_strand = ""
    for i in original_strand:
        if i == "A":
            opposite_strand += "T"
        elif i == "T":
            opposite_strand += "A"
        elif i == "C":
            opposite_strand += "G"
        elif i == "G":
            opposite_strand += "C"
        elif i =="U":
            print("This is an RNA strand not DNA!")
            break
        else:
            print("Invalid DNA strand.")
            break
    #return opposite_strand
    if len(opposite_strand) == len(original_strand):
        print("                 " + "-" * len(original_strand))
        print("Original strand: %s" % (original_strand))
        print("                 " + "|" * len(original_strand))
        print("Opposite strand: %s" % (opposite_strand))
        print("                 " + "-" * len(original_strand))
    else:
        print("Replication process aborted..")

#replication("suspect2.txt")
#replication("dna_test_sequence.txt")

# Method for DNA transcription
def transcription(dna_strand):
    print("Starting transcription method..")
    sleep(3)
    original_strand = read_dna(dna_strand)
    print("Test line")
    print(original_strand)
    mRNA_strand = ""
    print(mRNA_strand)
    for i in original_strand:
        if i == "A":
            mRNA_strand += "U"
            print(mRNA_strand)
        elif i == "T":
            mRNA_strand += "A"
            print(mRNA_strand)
        elif i == "C":
            mRNA_strand += "G"
            print(mRNA_strand)
        elif i == "G":
            mRNA_strand += "C"
            print(mRNA_strand)
        elif i =="U":
            print("This is an RNA strand not DNA!")
            break
        else:
            print("Invalid DNA strand.")
            break
    #return mRNA_strand
    if len(mRNA_strand) == len(original_strand):
        print("mRNA strand: %s" % (mRNA_strand))
    else:
        print("Transcription process aborted..")

    # write string to file
    # check if file already exists, delete if exists
    import os
    if os.path.exists("transcribed_mRNA.txt"):
        print("Removing old mRNA file...")
        sleep(3)
        os.remove("transcribed_mRNA.txt")
    else:
        print("mRNA file does not already exist")

    # create mRNA file
    print("Transcribing DNA strand to mRNA...")
    sleep(3)
    print("Creating mRNA file...")
    sleep(3)
    f = open("transcribed_mRNA.txt", "x")

    # write mRNA to file
    f = open("transcribed_mRNA.txt", "a")
    f.write(mRNA_strand)
    f.close()
    print("mRNA file created!")

#transcription("dna_test_sequence.txt")

# Method for translation of mRNA to polypeptide chain
def translation(dna_strand):
    mRNA_data = transcription(dna_strand)    
    codons = []
    for i in range(0, (len(mRNA_data))):
        if (i + 3) <= len(mRNA_data):
            codons.append(mRNA_data[i:(i+3)])
    print(codons)
    counter = 0
    for codon in codons:
        new_condons = []        
        print("Checking for start codon..")
        # AUG corresponding to start using Met
        if codon == "AUG":
            print("Start codon found!")
            for i in range(counter, (len(codons)), 3):
                if i <= len(mRNA_data):
                    new_condons.append(codons[i])       
            print(new_condons)
            break
        else:
            counter += 1
    
    # mRNA condons corresponding to Amino acid
    AA_dict = {
        "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
        "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
        "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
        "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
        "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
        "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
        "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
        "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
        "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
        "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
        "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
        "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
        "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
        "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
        "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
        "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
        }

    AA_list = []
    for codon in new_condons:
        x = AA_dict.get(codon)
        if x != "Stop":
            AA_list.append(x)
        else:
            break
            
    print(AA_list)
    
#translation("dna_test_sequence.txt")

def create_dna(total):
   # from numpy import random
    from numpy import random
    x = random.choice(["A", "T", "C", "G"], p=[0.25, 0.25, 0.25, 0.25], size=(total))
    dna_string = ""
    for item in x:
        dna_string += item

    print(dna_string)

    # check if file already exists, delete if exists
    import os
    if os.path.exists("random_dna.txt"):
        print("Removing old DNA file...")
        os.remove("random_dna.txt")
    else:
        print("DNA file does not exist")

    # create dna file
    print("Creating new DNA file with %s random base codes..." % (total))
    f = open("random_dna.txt", "x")

    # write dna to file
    f = open("random_dna.txt", "a")
    f.write(dna_string)
    f.close()
    print("DNA file with %s random base codes created!" % (total))

#create_dna(100)



def welcome():
    print("Hello and welcome to the DNA lab!")
    sleep(2)
    print("Lab services are online")
    sleep(2)
    print("What service would you like to use?")

def start_analysis():
    welcome()
    start = True
    while start:
        print("1) DNA Match \n2) DNA Replication \n3) DNA Transcription \n4) DNA Translation \n5) Random DNA Generator \n6) Exit")
        user_choice = input("Enter choice: ")
    
        if user_choice == "1":
            print("DNA Match")
            sleep(5)
            dna_file = input("Enter suspect DNA file: ")
            is_criminal(dna_file)
            sleep(5)
        elif user_choice == "2":
            print("DNA Replication")
            sleep(5)
        elif user_choice == "3":
            print("DNA Transcription")
            sleep(5)
        elif user_choice == "4":
            print("DNA Translation")
            sleep(5)
        elif user_choice == "5":
            print("Random DNA Generator")
            sleep(5)
        elif user_choice == "6":
            print("Closing down the lab..")
            sleep(3)
            print("...")
            sleep(3)
            start = False
        else:
            print("Invalid input")

start_analysis()