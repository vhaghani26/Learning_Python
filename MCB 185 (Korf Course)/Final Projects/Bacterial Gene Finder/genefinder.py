#!/usr/bin/env python3

'''
Develop a program that finds all the genes in a bacterial genome.

Specifications:
Program reads FASTA file of genome sequence
Genes begin with ATG and end with stop codon
Genes are at least X amino acids long (default 100)
Genes may be on either strand
Genes must be given unique names
Genes must be reported in a FASTA file as their protein sequence
Also create a genome report containing the following information:
    Name of the genome
    Size of the genome in bp
    Number of genes
    Percentage of genome that is coding
    Number of genes on the positive strand
    Number of genes on the negative strand
'''

import argparse
import biotools as bt


# Setup
parser = argparse.ArgumentParser(
	description='Prokaryotic gene finder.')
    
# Required arguments
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='FASTA file')
    
# Optional arguments
parser.add_argument('--minprot', required=False, type=int, default=100,
	metavar='<int>', help='Minimum amino acid length for reporting [%(default)i]')

# Switch
parser.add_argument('--genreport', action="store_true",
   help='Whether or not the user wants to see a genome report')

# Finalization
arg = parser.parse_args()


for name, seq in bt.read_fasta(arg.file):                   # Program reads FASTA file of genome sequence (was for name, seq in bt.read_fasta(seq):)
    gen_size = len(seq)                                     # Calculate the length of the genome size (reported if genreport is switched on)
    gen_name = 0                                            # Set-up to give genes unique names
    gen_num = 0                                             # Reports gene number if genreport is switched on
    cds = 0                                                 # Calculates the number of nucleotides that are part of an ORF (coding sequence)
    pos_strand = 0                                          # Calculates the number of genes on the positive strand
    neg_strand = 0                                          # Calculates the number of genes on the negative strand
    f_and_r = []                                            # Making a list to store F and R sequences (positive and negative strand)
    comp_seq = bt.anti(seq)                                 # Use anti function to create reverse complement and store it
    f_and_r.append(seq)                                     # Add the forward sequence to the list
    f_and_r.append(comp_seq)                                # Add the reverse sequence to the list
    for s in f_and_r:                                       # Use a for loop to apply find_orf to both the positive and negative strand
        genes = bt.find_orfs(s, arg.minprot)                # Apply the find_orfs function from biotools                                  
        for gene in genes:
            if gene in f_and_r[0]:                          # This conditional sorts genes as being on the positive or negative strand
                pos_strand += 1
            else:
                neg_strand +=1
            pro = []                                        # Make an empty list to add amino acids for each sequence
            for i in range (0, len(gene), 3):
                codon = gene[i:i+3]
                if codon in bt.aa: pro.append(bt.aa[codon]) # Translate the stored DNA sequences into protein sequences
                else:              pro.append('X')          # How to deal with Ns and such 
                protein = ''.join(pro)                      # Changes the list of nucletoides to a long string 
                gen_name += 1                               # Helps give genes unique names 
                cds += 1                                    
            gen_num += 1 
            print(f'>{name}-{gen_name}')                    # Genes reported in FASTA file as their protein sequence
            print(f'{protein}\n')
    if arg.genreport:                                       # If "genreport" is switched on in the terminal, this information gets reported
                    print("Genome Report")
                    print(f'Name of Genome: {name}')
                    print(f'Size of Genome: {gen_size} bp')
                    print(f'Number of Genes: {gen_num}')
                    print(f'Percentage Coding Genome: {(cds/len(seq))*100:.1f}%')
                    print(f'Genes on Positive Strand: {pos_strand}')
                    print(f'Genes on Negative Strand: {neg_strand}\n')


'''
python3 genefinder.py --file transcripts.fasta.gz --minprot 1 --genreport | less
>CBG00001.1-175
MTFCENKNLPKPPSDRCQVVVISILSMILDFYLKYNPDKHWAHLFYGASPILEILVIFGMLANSVYGNKLAMFACVLDLVSGVFCLLTLPVISVAENATGVRLHLPYISTFHSQFSFQVSTPVDLFYVATFLGFVSTILILLFLILDALKFMKLRKLRNEDLEKEKKMNPIEKV*

>CBG00001.1-255
MSSGGHLHSEYDSGFLSQVQSRQTLGSSILRSKSNFGDFGHFWNVGELGVWQQIGYVCLCPRLGLWRVLSFDSSSHFCC*

>CBG00001.1-277
MATNWLCLLVSSTWSLACSVF*

>CBG00001.1-320
MPLVSACTFHTSPLSIRSFLSKSQLQWTFSMLPLSLDSSPRF*

>CBG00001.1-330
MRIWKKRKR*

>CBG00001.1-398
MTEKNSSKTKVSAKFQSKSQTFSIGFIFFSFSRSSLRSLRSFMNLRASKIRKRRIRIVETNPRKVAT*

>CBG00001.1-467
MESGDVWKVQADTSGIFSNRNDWKSQKTEHARDQVEDTSKHSQFVAIHRVRQHSKNDQNLQNWTCSVE*

>CBG00001.1-530
MYGRCKRTPVAFSATEMTGRVKRQNTPETKSRTQANIANLLPYTEFANIPKMTKISKIGLAP*

>CBG00001.1-546
MEGASGHQWHFQQQK*

>CBG00001.1-553
MEMTTT*

Genome Report
Name of Genome: CBG00001.1
Size of Genome: 720 bp
Number of Genes: 10
Percentage Coding Genome: 76.8%
Genes on Positive Strand: 5
Genes on Negative Strand: 5





python3 genefinder.py --file transcripts.fasta.gz --minprot 25 --genreport | less
>CBG00001.1-175
MTFCENKNLPKPPSDRCQVVVISILSMILDFYLKYNPDKHWAHLFYGASPILEILVIFGMLANSVYGNKLAMFACVLDLVSGVFCLLTLPVISVAENATGVRLHLPYISTFHSQFSFQVSTPVDLFYVATFLGFVSTILILLFLILDALKFMKLRKLRNEDLEKEKKMNPIEKV*

>CBG00001.1-255
MSSGGHLHSEYDSGFLSQVQSRQTLGSSILRSKSNFGDFGHFWNVGELGVWQQIGYVCLCPRLGLWRVLSFDSSSHFCC*

>CBG00001.1-298
MPLVSACTFHTSPLSIRSFLSKSQLQWTFSMLPLSLDSSPRF*

>CBG00001.1-366
MTEKNSSKTKVSAKFQSKSQTFSIGFIFFSFSRSSLRSLRSFMNLRASKIRKRRIRIVETNPRKVAT*

>CBG00001.1-435
MESGDVWKVQADTSGIFSNRNDWKSQKTEHARDQVEDTSKHSQFVAIHRVRQHSKNDQNLQNWTCSVE*

>CBG00001.1-498
MYGRCKRTPVAFSATEMTGRVKRQNTPETKSRTQANIANLLPYTEFANIPKMTKISKIGLAP*

Genome Report
Name of Genome: CBG00001.1
Size of Genome: 720 bp
Number of Genes: 6
Percentage Coding Genome: 69.2%
Genes on Positive Strand: 3
Genes on Negative Strand: 3





python3 genefinder.py --file transcripts.fasta.gz --minprot 1 | less
>CBG00001.1-175
MTFCENKNLPKPPSDRCQVVVISILSMILDFYLKYNPDKHWAHLFYGASPILEILVIFGMLANSVYGNKLAMFACVLDLVSGVFCLLTLPVISVAENATGVRLHLPYISTFHSQFSFQVSTPVDLFYVATFLGFVSTILILLFLILDALKFMKLRKLRNEDLEKEKKMNPIEKV*

>CBG00001.1-255
MSSGGHLHSEYDSGFLSQVQSRQTLGSSILRSKSNFGDFGHFWNVGELGVWQQIGYVCLCPRLGLWRVLSFDSSSHFCC*

>CBG00001.1-277
MATNWLCLLVSSTWSLACSVF*

>CBG00001.1-320
MPLVSACTFHTSPLSIRSFLSKSQLQWTFSMLPLSLDSSPRF*

>CBG00001.1-330
MRIWKKRKR*

>CBG00001.1-398
MTEKNSSKTKVSAKFQSKSQTFSIGFIFFSFSRSSLRSLRSFMNLRASKIRKRRIRIVETNPRKVAT*

>CBG00001.1-467
MESGDVWKVQADTSGIFSNRNDWKSQKTEHARDQVEDTSKHSQFVAIHRVRQHSKNDQNLQNWTCSVE*

>CBG00001.1-530
MYGRCKRTPVAFSATEMTGRVKRQNTPETKSRTQANIANLLPYTEFANIPKMTKISKIGLAP*

>CBG00001.1-546
MEGASGHQWHFQQQK*

>CBG00001.1-553
MEMTTT*
'''
