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

def is_criminal(dna_sample):
    dna_data = read_dna(dna_sample)
    condons = dna_condons(dna_data)
    num_matches = match_dna(condons)
    if num_matches >= 3:
        print("%s matches found. Carry on the investigation." % (num_matches))
    else:
        print("%s matches found. Free the suspect." % (num_matches))

is_criminal("suspect1.txt")
is_criminal("suspect2.txt")
is_criminal("suspect3.txt")
is_criminal("suspect4.txt")
is_criminal("suspect5.txt")

