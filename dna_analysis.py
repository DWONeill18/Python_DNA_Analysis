# DNA analysis

sample = ["GTA", "GGG", "CAC"]

# Method to take a file, read it, add it's contents to an empty string and return the updated string.
def read_dna(dna_file):
    dna_data = ""
    with open(dna_file, "r") as f:
        for line in f:
            dna_data += line
    return dna_data

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
    condons = dna_condons(dna_data)
    num_matches = match_dna(condons)
    if num_matches >= 3:
        print("%s matches found. Carry on the investigation." % (num_matches))
    else:
        print("%s matches found. Free the suspect." % (num_matches))

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
    original_strand = read_dna(dna_strand)
    mRNA_strand = ""
    for i in original_strand:
        if i == "A":
            mRNA_strand += "U"
        elif i == "T":
            mRNA_strand += "A"
        elif i == "C":
            mRNA_strand += "G"
        elif i == "G":
            mRNA_strand += "C"
        elif i =="U":
            print("This is an RNA strand not DNA!")
            break
        else:
            print("Invalid DNA strand.")
            break
    if len(mRNA_strand) == len(original_strand):
        print("mRNA strand: %s" % (mRNA_strand))
    else:
        print("Transcription process aborted..")
    
transcription("dna_test_sequence.txt")



# Method for translation of mRNA to polypeptide chain
def translation(mrna_strand):
    pass