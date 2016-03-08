
generefer = AGGTAAGACCCTAAGGCAT

lis = input('Enter the list of numbers (using commas, without whitespaces): ')
target = input('Enter the target number: ')

#project 1

gene = 'ACTGAT'
g = gene

g = g.replace('A', 'a')
#Use a replace A
g = g.replace('T', 'A')
#Use A replace T
g = g.replace('a', 'T')
#Use T replace a

g = g.replace('C', 'c')
#Use c replace C
g = g.replace('G', 'C')
#Use C replace G
g = g.replace('c', 'G')
#Use G replace c
print(g)


#project 2

gene = 'ACTGAT'
g = gene[::-1]
#Use this code to reverse this chain
print(g)


#project 3

gene = 'ACTGAT'
g = gene.replace('A', '')
g = g.replace('T', '')
g = g.replace('C', '')
g = g.replace('G', '')
#Replace ACTGAT with ""
lg = len(g)
#Calculate the length of gene
if lg > 0:
    print('invalid')
#If lg is bigger than 0, then print invalid
else:
    print('valid')
#Print valid in other situation

#project 4

gene1 = 'ATTCGGCTA'
gene2 = 'TAGCCGAAT'

def validity_gene(gene):
    g = gene.replace('A', '')
    g = g.replace('T', '')
    g = g.replace('C', '')
    g = g.replace('G', '')
#Define validity_gene and then use "" to replace ATCG
    lg = len(g)
#Calculate the length of the gene
    if lg > 0:
        v = 'invalid'
    else:
        v = 'valid'
    return v
#If lg is bigger then 0, then v equal invalid, otherwise, v equal valid

def match_gene(gene):
    g = gene.replace('A', 'a')
    g = g.replace('T', 'A')
    g = g.replace('a', 'T')
#Define math_gene, and replave ATa by aAT

    g = g.replace('C', 'c')
    g = g.replace('G', 'C')
    g = g.replace('c', 'G')
#Replace CGc by CcG
    return g

def reverse_gene(gene):
    g = gene[::-1]
#Use reverse_gene to reverse gene
    return g

print('Gene 1 is', validity_gene(gene1))
print('Gene 2 is', validity_gene(gene2))
#Print two genes.

if validity_gene(gene1) == 'valid' and validity_gene(gene2) == 'valid':
    if match_gene(gene1) == gene2:
        print('They represent the same DNA fragment.')
    elif match_gene(gene1) == reverse_gene(gene2):
        print('They represent the same DNA fragment.')
    else:
        print('They do not represent the same DNA fragment.')
#Print different sentences in different situations

#Project 5

gene1 = 'TCGGCTACCGTATGTGTGT'
gene2 = 'TAGCCGAATGTTAGCCGAATGTGTCCAT'

def validity_gene(gene):
    g = gene.replace('A', '')
    g = g.replace('T', '')
    g = g.replace('C', '')
    g = g.replace('G', '')
#Replace ATCG with ""
    lg = len(g)
#Calculate the length of the gene

    if lg > 0:
        v = 'invalid'
    else:
        v = 'valid'
    return v
#If lg is bigger then 0, then v equal invalid, otherwise, v equal valid

def match_gene(gene):
    g = gene.replace('A', 'a')
    g = g.replace('T', 'A')
    g = g.replace('a', 'T')
#Replace ATa with aAT
    g = g.replace('C', 'c')
    g = g.replace('G', 'C')
    g = g.replace('c', 'G')
    return g
#Replace CGc with cCG

def reverse_gene(gene):
    g = gene[::-1]
#Use reverse_gene to reverse gene
    return g

print('Gene 1 is', validity_gene(gene1))
print('Gene 2 is', validity_gene(gene2))
#Print gene 1 is with validity_gene(gene1)

if validity_gene(gene1) == 'valid' and validity_gene(gene2) == 'valid':
    lg1 = len(gene1)
    lg2 = len(gene2)

    if lg1 >= lg2:
        long_gene = gene1
        short_gene = gene2
        lg12 = lg1 - lg2 + 1
        lgshort = lg2
#In this situation, gene1 is long_gene and gene2 is short_gene. Calculate lg12 equal lg1 minus lg2 and plus 1
    else:
        long_gene = gene2
        short_gene = gene1
        lg12 = lg2 - lg1 + 1
        lgshort = lg1

    mshort = match_gene(short_gene)
    print('matchs of each case:')

    for i in range(lg12):
        n = 0
#Start with n equal 0
        for j in range(lgshort):
            if mshort[j] == long_gene[i + j]:
                n += 1
#If mshortj equal long_gene i plus j
        print(n)
        print('matchs of each case(reverse)')
    mrshort = reverse_gene(mshort)

    for i in range(lg12):
        n = 0
        for j in range(lgshort):
            if mrshort[j] == long_gene[i + j]:
                n += 1
        print(n)


#Project 6

gene1 = 'TCGGCTACCGTATGTGTGT'
gene2 = 'TAGCCGAATGTTAGCCGAATGTGTCCAT'

def validity_gene(gene):
    g = gene.replace('A', '')
    g = g.replace('T', '')
    g = g.replace('C', '')
    g = g.replace('G', '')
#Use "" to replace ATCG

    lg = len(g)

    if lg > 0:
        v = 'invalid'
    else:
        v = 'valid'
    return v
#Let v equal invalid or valid in different situations

def match_gene(gene):
    g = gene.replace('A', 'a')
    g = g.replace('T', 'A')
    g = g.replace('a', 'T')
#Replace ATa by aAT
    g = g.replace('C', 'c')
    g = g.replace('G', 'C')
    g = g.replace('c', 'G')
    return g
#Replace CGc by cCG
def reverse_gene(gene):
    g = gene[::-1]
#Use reverse_gene to reverse gene
    return g


print('Gene 1 is', validity_gene(gene1))
print('Gene 2 is', validity_gene(gene2))

if validity_gene(gene1) == 'valid' and validity_gene(gene2) == 'valid':
    lg1 = len(gene1)
    lg2 = len(gene2)

    if lg1 >= lg2:
        long_gene = gene1
        short_gene = gene2
        lg12 = lg1 - lg2 + 1
        lgshort = lg2
    else:
        long_gene = gene2
        short_gene = gene1
        lg12 = lg2 - lg1 + 1
        lgshort = lg1

    mshort = match_gene(short_gene)
    print('matchs of each case:')

    for i in range(lg12):
        n = 0
        nconse = []
        for j in range(lgshort):
            if mshort[j] == long_gene[i + j]:
                n += 1
            else:
                nconse.append(n)
                n = 0
        print(nconse)
        print('longest consecutive: ', max(nconse))
        print(sum(nconse))

    print('matchs of each case(reverse)')
    mrshort = reverse_gene(mshort)

    for i in range(lg12):
        n = 0
        nconse = []
        for j in range(lgshort):
            if mrshort[j] == long_gene[i + j]:
                n += 1
            else:
                nconse.append(n)
                n = 0
        print(nconse)
        print('longest consecutive: ', max(nconse))
        print(sum(nconse))



#Project 7

# database:
gene1 = 'TCGGCTACCGTATGTGTGT'
gene2 = 'TAGCCGAATGTTAGCCGAATGTGTCCAT'
gene3 = 'CGGTAATGGCATGCGCTACTAAGC'
genedatabase = [gene1, gene2, gene3]
genein = input('Enter the target DNA gragment string: ')

n_total_matches = []
n_longest_matches = []

def validity_gene(gene):
    g = gene.replace('A', '')
    g = g.replace('T', '')
    g = g.replace('C', '')
    g = g.replace('G', '')

    lg = len(g)

    if lg > 0:
        v = 'invalid'
    else:
        v = 'valid'
    return v

def match_gene(gene):
    g = gene.replace('A', 'a')
    g = g.replace('T', 'A')
    g = g.replace('a', 'T')

    g = g.replace('C', 'c')
    g = g.replace('G', 'C')
    g = g.replace('c', 'G')
    return g

def order_gene_len(gene_len_1, gene1, gene_len_2, gene2):
    if gene_len_1 >= gene_len_2:
        long_gene = gene1
        short_gene = gene2
        lg12 = gene_len_1 - gene_len_2 + 1
        lgshort = gene_len_2
    else:
        long_gene = gene2
        short_gene = gene1
        lg12 = gene_len_2 - gene_len_1 + 1
        lgshort = gene_len_1
    return short_gene, long_gene, lg12, lgshort

def reverse_gene(gene):
    g = gene[::-1]
    return g

def longest_match(short_gene, long_gene, lg12, lgshort):
    mshort = match_gene(short_gene)
print('matchs of each case:')

    for i in range(lg12):
        n = 0
        nconse = []
        for j in range(lgshort):
            if mshort[j] == long_gene[i + j]:
                n += 1
            else:
                nconse.append(n)
                n = 0
        longest_matches = max(nconse)
        total_matches = sum(nconse)
    print('longest consecutive: ', longest_matches)
    print('total number of matches: ', total_matches)

print('matchs of each case(reverse)')
    mrshort = reverse_gene(mshort)

    for i in range(lg12):
        n = 0
        nconse = []
        for j in range(lgshort):
            if mrshort[j] == long_gene[i + j]:
                n += 1
            else:
                nconse.append(n)
                n = 0
        longest_matches = max(nconse)
        total_matches = sum(nconse)
print('longest consecutive: ', longest_matches)
print('total number of matches: ', total_matches)
    return longest_matches, total_matches


print('Genein is', validity_gene(genein))

if validity_gene(genein) == 'valid':
    lg1 = len(gene1)
    lg2 = len(gene2)
    lg3 = len(gene3)
    lg = len(genein)

# compare to gene1:
short_gene, long_gene, lg12, lgshort = order_gene_len(len(gene1), gene1, len(genein), genein)
longest_matches, total_matches = longest_match(short_gene, long_gene, lg12, lgshort)

n_longest_matches.append(longest_matches)
n_total_matches.append(total_matches)

# compare to gene2:
short_gene, long_gene, lg12, lgshort = order_gene_len(len(gene2), gene2, len(genein), genein)
longest_matches, total_matches = longest_match(short_gene, long_gene, lg12, lgshort)

n_longest_matches.append(longest_matches)
n_total_matches.append(total_matches)

# compare to gene3:
short_gene, long_gene, lg12, lgshort = order_gene_len(len(gene3), gene3, len(genein), genein)
longest_matches, total_matches = longest_match(short_gene, long_gene, lg12, lgshort)

n_longest_matches.append(longest_matches)
n_total_matches.append(total_matches)

best_totalngene = n_total_matches.index(max(n_total_matches))
best_longestngene = n_longest_matches.index(max(n_longest_matches))

print('total: ', max(n_total_matches))
print('longest: ', max(n_longest_matches))

print('total => database gene num: ', best_totalngene + 1)
print('longest => database longset num: ', best_longestngene + 1)

print('total, reference gene: ', genedatabase[best_totalngene])
print('longest, reference gene: ', genedatabase[best_longestngene])



### ATTGCCTAGTCAAG
