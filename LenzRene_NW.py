from Bio import SeqIO
from Bio.Seq import Seq
from argparse import ArgumentParser
from Bio.Alphabet import generic_dna
import sys


parser = ArgumentParser()
parser.add_argument('--match', default=1,
                    help='matchinig score (default = 1)')
parser.add_argument('--missmatch', default=-1,
                    help='missmatch score (default = -1)')
parser.add_argument('--gap', default=-2,
                    help='gap score (default = -2)')

args = parser.parse_args()

input_sequence = SeqIO.parse(sys.stdin, "fasta")

i = 0
for seq in input_sequence:
    if i == 0:
        seq1 = seq.seq
        id1 = seq.id
    elif i == 1:
        seq2 = seq.seq
        id2 = seq.id
    else:
        exit("Error: fasta file has more than 2 sequences")
    i+=1

scoring_matrix = [[0]]
pat = [[" "]]

nrow = len(seq1) + 1
ncol = len(seq2) + 1

for i in range(1,ncol,1): #fill first line of scoring matrix and path matrix
    scoring_matrix[0].append(scoring_matrix[0][i - 1] + args.gap)
    pat[0].append("r")

it1 = 0
it2 = 0

for row in range(1,nrow,1):
    scoring_matrix.append([scoring_matrix[row - 1][0] + args.gap])
    pat.append(["u"])
    for col in range(1,ncol,1):
        vertical = scoring_matrix[row - 1][col] + args.gap
        horizontal = scoring_matrix[row][col - 1] + args.gap
        if (seq1[it1] == seq2[it2]):
            diagonal = scoring_matrix[row - 1][col - 1] + args.match
        else:
            diagonal = scoring_matrix[row - 1][col - 1] + args.missmatch

        if horizontal >= vertical and horizontal > diagonal:
            scoring_matrix[row].append(horizontal)
            pat[row].append("r")
        elif vertical > horizontal and vertical > diagonal:
            scoring_matrix[row].append(vertical)
            pat[row].append("u")
        elif diagonal >= horizontal and diagonal >= vertical:
            scoring_matrix[row].append(diagonal)
            pat[row].append("d")
        else:
            exit("Error: horizontal not larger smaller or equal to vertical!")
        it2 += 1
    it1 +=1
    it2 = 0

print("Similarity score", scoring_matrix[len(seq1)][len(seq2)], file=sys.stderr)

col = len(pat[0]) - 1
row = len(pat) - 1
path = ""

while(row > 0 or col > 0):
    if pat[row][col] == "d":
        path += "d"
        row -= 1
        col -= 1
    elif pat[row][col] == "u":
        path += "u"
        row -= 1
    elif pat[row][col] == "r":
        path += "r"
        col -= 1
    elif pat[row][col] == " ":
        break
    else:
        print("Unknown element")
path = path[::-1]

alignment = ["","",""]
it1 = 0
it2 = 0
for step in path:
    if step == "d":
        alignment[0] += seq1[it1]
        alignment[1] += seq2[it2]
        if seq1[it1] == seq2[it2]:
            alignment[2] += "*"
        else:
            alignment[2] += " "
        it1 += 1
        it2 += 1
    elif step == "u":
        alignment[0] += seq1[it1]
        alignment[1] += "-"
        alignment[2] += " "
        it1 += 1
    elif step == "r":
        alignment[0] += "-"
        alignment[1] += seq2[it2]
        alignment[2] += " "
        it2 += 1

rec1 = SeqIO.SeqRecord(Seq(alignment[0], generic_dna), id1)

rec2 = SeqIO.SeqRecord(Seq(alignment[1], generic_dna), id2)

rec3 = SeqIO.SeqRecord(Seq(alignment[2]),"")
rec = [rec1, rec2, rec3]


SeqIO.write(rec,sys.stdout, "clustal")