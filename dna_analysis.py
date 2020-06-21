# DNA analysis
from numpy import random
from random import randint
from time import sleep
import os
import re

#######################
## File Manipulation ##
#######################

# Method to take a file, read it, add it's contents to an empty string and return the updated string
def read_dna(dna_file):
    # check if file exists and read it   
    if os.path.exists(dna_file):        
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

# Method to check if a file exists, writes output to file
def write_file(data):
    # check if file already exists, delete if exists
    filename = input("Enter filename to write output to: ")
    if os.path.exists(filename):
        print("Removing old file...")
        sleep(3)
        os.remove(filename)
    else:
        pass
        #print("%s does not exist." % (filename))
    # create file
    print("Creating new file...")
    sleep(3)
    f = open(filename, "x")
    # write to file
    f = open(filename, "a")
    f.write(data)
    f.close()
    print("File created!")

#################
## Sub Methods ##
#################

# Method to take a string, create a list of condons and return the list
def dna_condons(dna):
    condons = []
    for i in range(0, (len(dna)), 3):
        if (i + 3) <= len(dna):
            condons.append(dna[i:(i+3)])
    return condons

# Method to read file amd create list of codons
def convert_to_codons(dna_file):
    dna_data = read_dna(dna_file)
    if read_dna.exist:
        codons = re.findall("(\w{3})", dna_data)
        # Last multiple of 3 is not put into list
        print(codons)
    else:
        print("File is invalid.")

# Method to iterate through both the sample and suspect's DNA
def match_dna(dna):
    matches = 0
    sample = []
    sample = input("Enter condon samples(e.g AAA, TTT, GGG): ")
    for condon in dna:
        if condon in sample:
            matches += 1
    return matches

# Method to search dna file and give number of matches
def search_dna(dna_file):
    sample = input("Enter condon samples(e.g AAA, TTT, GGG): ")
    dna_data = read_dna(dna_file)
    if read_dna.exist:
        sequence = re.findall(sample, dna_data)
        matches = len(sequence)
        print(sequence)
        print(matches)
        chosen_matches = input("Minimum number of matches for investigation: ")
        if (chosen_matches.isdigit()) ==  True:
            chosen_matches = int(chosen_matches)
            if matches >= chosen_matches:
                data = "%s matches found. Carry on the investigation." % (matches)
                print(data)
                write_file(data)
            else:
                print("%s matches found. Free the suspect." % (matches))            
        else:
            print("Invalid input. Not an integer.") 
    else:
        print("File does not exist.")

######################
## Analysis Methods ##
######################

# Method to check whether sample matches suspect DNA
def is_criminal(dna_sample):
    dna_data = read_dna(dna_sample)
    if read_dna.exist == True:
        condons = dna_condons(dna_data)
        num_matches = match_dna(condons)
        chosen_matches = input("Minimum number of matches for investigation: ")
        if (chosen_matches.isdigit()) ==  True:
            chosen_matches = int(chosen_matches)
            if num_matches >= chosen_matches:
                data = "%s matches found. Carry on the investigation." % (num_matches)
                print(data)
                write_file(data)
            else:
                print("%s matches found. Free the suspect." % (num_matches))            
        else:
            print("Invalid input. Not an integer.")
    else:
        print("File does not exist.")
    
# Method for DNA replication
def replication(dna_strand):
    print("Starting replication process..")
    sleep(3)
    original_strand = read_dna(dna_strand)
    if read_dna.exist == True:    
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
            data = ("                 " + "-" * len(original_strand) +
             "\nOriginal strand: %s" % (original_strand) +
             "\n                 " + "|" * len(original_strand) +
             "\nOpposite strand: %s" % (opposite_strand) +
             "\n                 " + "-" * len(original_strand)
              )
            print(data)
            write_file(data)
        else:
            print("Replication process aborted..")
    else:
        print("File does not exist.")

# Method for DNA transcription
def transcription(dna_strand):
    print("Starting transcription method..")
    sleep(3)
    original_strand = read_dna(dna_strand)
    if read_dna.exist == True:
        print(original_strand)
        mRNA_strand = ""
        print(mRNA_strand)
        for i in original_strand:
            if i == "A":
                mRNA_strand += "U"
                #print(mRNA_strand)
            elif i == "T":
                mRNA_strand += "A"
                #print(mRNA_strand)
            elif i == "C":
                mRNA_strand += "G"
                #print(mRNA_strand)
            elif i == "G":
                mRNA_strand += "C"
                #print(mRNA_strand)
            elif i =="U":
                print("This is an RNA strand not DNA!")
                break
            else:
                print("Invalid DNA strand.")
                break
        if len(mRNA_strand) == len(original_strand):
            print("mRNA strand: %s" % (mRNA_strand))
            write_file(mRNA_strand)
        else:
            print("Transcription process aborted..")

        # Removing old mRNA file...
        #"Transcribing DNA strand to mRNA..
        # write string to file
        # check if file already exists, delete if exists

    else:
        print("File is invalid.")

# Method for translation of mRNA to polypeptide chain
def translation(dna_strand):
    #mRNA_data = transcription(dna_strand)
    mRNA_data = read_dna(dna_strand)
    if read_dna.exist == True:
        
        codons = []
        for i in range(0, (len(mRNA_data))):
            if (i + 3) <= len(mRNA_data):
                codons.append(mRNA_data[i:(i+3)])
        #print(codons)
        print("Checking for start codon..")
        counter = 0
        for codon in codons:
            new_condons = []        
            
            # AUG corresponding to start using Met
            if codon == "AUG":
                print("Start codon found!")
                for i in range(counter, (len(codons)), 3):
                    if i <= len(mRNA_data):
                        new_condons.append(codons[i])       
                #print(new_condons)
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

        #AA_list = []
        AA = ""
        for codon in new_condons:
            x = AA_dict.get(codon)
            if x != "Stop":
                #AA_list.append(x)
                AA += (x + " ")
            else:
                break
                    
        print(AA)
        # need to convert list to string


        write_file(AA)
    else:
        print("File is invalid.")

# Method to create a single strand of DNA with a given numebr of bases
def create_dna(total):    
    total = int(total)
    
    x = random.choice(["A", "T", "C", "G"], p=[0.25, 0.25, 0.25, 0.25], size=(total))
    dna_string = ""
    for item in x:
        dna_string += item
    print("Creating new DNA file with %s random base codes..." % (total))
    print(dna_string)
    write_file(dna_string)

# Method to add a single base mutation randomly within a given DNA strand
def mutation(dna_strand):
    new_dna = read_dna(dna_strand)
    if read_dna.exist == True:
        base_number = input("Enter the length of base mutation: ")        
        if(base_number.isdigit()):
            base_number = int(base_number)
            import random
            x = random.choices(["A", "T", "C", "G"], k = base_number)
            random_bases = ""
            for item in x:
                random_bases += item

            y = randint(0, len(new_dna))
            mutated_dna = new_dna[:y] + random_bases + new_dna[y:]
            print("DNA output: %s" % (mutated_dna))
            write_file(mutated_dna)
            sleep(5)
        else:
            print("The length of base mutation is not an integer!")
    else:
        print("File is invalid.")

##########################
## Command Line Methods ##
##########################

def welcome():
    print("############################################")
    print("##### DNA Lab Analysis -- Version 2.13 #####")
    print("############################################")
    print("############################################")
    print("##### Welcome to the DNA lab! ##############")
    sleep(2)
    print("############################################")
    print("Lab services are online")
    print("############################################")
    sleep(2)
    print("############################################")
    print("### Which service would you like to use? ###")
    print("############################################")

def start_analysis():
    welcome()
    start = True
    while start:
        print("1) DNA Match \n2) DNA Replication \n3) DNA Transcription \n4) DNA Translation" + 
        "\n5) Random DNA Generator \n6) Random DNA Mutation \n7) Information \n8) Exit")
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
            replication_file = input("Enter DNA file you wish to replicate: ")
            replication(replication_file)
            sleep(5)
        elif user_choice == "3":
            print("DNA Transcription")
            sleep(5)
            transcription_file = input("Enter DNA file you wish to transcribe: ")
            transcription(transcription_file)
            sleep(5)
        elif user_choice == "4":
            print("DNA Translation")
            sleep(5)
            translation_file = input("Enter mRNA file you wish to translate to Amino Acids: ")
            translation(translation_file)
            sleep(5)
        elif user_choice == "5":
            print("Random DNA Generator")
            sleep(5)
            total = input("Enter number total number of bases in DNA: ")
            from math import floor
            if (total.isdigit()):
                create_dna(total)
                sleep(5)
            else:
                print("Total is not an integer!")
        elif user_choice == "6":
            print("Random Mutation")
            sleep(3)
            mutation_file = input("Enter DNA file you wish to mutate: ")
            mutation(mutation_file)
            sleep(3)
        elif user_choice == "7":
            print("Option Information" + "\n" +
             "\n1) DNA Match - Check whether suspect matches smaple DNA" +
             "\n2) DNA Replication - Replicate a DNA strand to give both it's original and complemetary strands" +
             "\n3) DNA Transcription - Transcribe a DNA strand to its mRNA counterpart"
             "\n4) mRNA Translation - Translate an mRNA strand to amino acids in a polypeptide chain" +
             "\n5) Random DNA Generator - Create a random DNA strand given a number of DNA bases" +
             "\n6) Random DNA Mutation - Insert a random DNA base into a DNA strand to cause a mutation" +
             "\n" +
             "\n")         
        elif user_choice == "8":
            print("Closing down the lab..")
            sleep(3)
            print("...")
            sleep(3)
            start = False
        else:
            print("Invalid input")

###################
## Begin Program ##
###################

start_analysis()