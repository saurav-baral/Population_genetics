
import matplotlib.pyplot as plt
import random

def allele_frequency(individual_allele_list, population_size):
    A_allele,B_allele,a_allele,b_allele = 0,0,0,0
    # for i in allele_list:
        
    for i in range(population_size):
        for j in range(2):
            for k in range(2):
                if individual_allele_list[i][j][k] == "a":
                    a_allele += 1
                elif individual_allele_list[i][j][k] == "A":
                    A_allele += 1
                elif individual_allele_list[i][j][k] == "b":
                    b_allele += 1
                elif individual_allele_list[i][j][k] == "B":
                    B_allele += 1
                else:
                    print("Some Issue")
                    print(individual_allele_list[i][j][k])
                
    return(A_allele,B_allele,a_allele,b_allele)

def biallele_frequency(individual_allele_list, population_size):
    AB_allele,Ab_allele,aB_allele,ab_allele = 0,0,0,0
    for i in range(population_size):
        for j in range(2):
            # print(individual_allele_list[i][j])
            if individual_allele_list[i][j] == ["A","B"]:
                AB_allele += 1
            elif individual_allele_list[i][j] == ["A","b"]:
                Ab_allele += 1
            elif individual_allele_list[i][j] == ["a","B"]:
                aB_allele += 1
            elif individual_allele_list[i][j] == ["a","b"]:
                ab_allele += 1
            else:
                print("Some Issue")
                print(individual_allele_list[i][j])
            # print(AB_allele,Ab_allele,aB_allele,ab_allele)
    return(AB_allele,Ab_allele,aB_allele,ab_allele)

population_size = 100
chr_h1 = ["A","B"]
chr_h2 = ["a","B"]
individual_allele_list = []

for i in range(population_size):
    individual_chromosome_1 = chr_h1
    individual_chromosome_2 = chr_h2
    
    individual_allele_list.append([individual_chromosome_1,individual_chromosome_2])


# print(individual_allele_list)
random_number  = int(random.uniform(0, population_size))
# print(random_number)
# print(individual_allele_list[random_number][0])
individual_allele_list[random_number][1] = [individual_allele_list[random_number][1][0],"b"]
# print(individual_allele_list[random_number][0])
# print(individual_allele_list)

A_allele,B_allele,a_allele,b_allele = allele_frequency(individual_allele_list, population_size)
print(f"A_freq = {A_allele/(population_size*2)}, B_freq = {B_allele/(population_size*2)}, a_freq = {a_allele/(population_size*2)}, b_freq = {b_allele/(population_size*2)}")

AB_allele,Ab_allele,aB_allele,ab_allele = biallele_frequency(individual_allele_list, population_size)
print(f"AB_freq = {AB_allele/(population_size*2)}, ab_freq = {ab_allele/(population_size*2)}, aB_freq = {aB_allele/(population_size*2)},  Ab_freq = {Ab_allele/(population_size*2)}")


recombination_frequency = 10
A_allele_freq,B_allele_freq,a_allele_freq,b_allele_freq = [],[],[],[]
AB_allele_freq,ab_allele_freq,aB_allele_freq,Ab_allele_freq = [],[],[],[]
disequlibrium = []

iteration = 10

for i in range(iteration):
    allele_pool = []
    
    for i in range(population_size):
        
        random_number = random.uniform(0, 50)
        
        if random_number > recombination_frequency:
        
            for j in range(2):
                allele_pool.append((individual_allele_list[i][j]))
            
        else:
            # print("recombination")
            # print([[individual_allele_list[i][0][0],individual_allele_list[i][1][1]],[individual_allele_list[i][1][0],individual_allele_list[i][0][1]]])
            recombinant_alleles = [[individual_allele_list[i][0][0],individual_allele_list[i][1][1]],[individual_allele_list[i][1][0],individual_allele_list[i][0][1]]]
            # print(recombinant_alleles)
            allele_pool.append(recombinant_alleles[0])
            allele_pool.append(recombinant_alleles[1])
    
    # print(allele_pool)
    individual_allele_list = []
    for i in range(population_size):        
        individual_allele_list.append([random.choice(allele_pool), random.choice(allele_pool)])
    # print(individual_allele_list)
    
    A_allele,B_allele,a_allele,b_allele = allele_frequency(individual_allele_list, population_size)
    
    # print(f"A_freq = {A_allele/(population_size*2)}, B_freq = {B_allele/(population_size*2)}, a_freq = {a_allele/(population_size*2)}, b_freq = {b_allele/(population_size*2)}")
    
    A_allele_freq.append(A_allele/(population_size*2))
    B_allele_freq.append(B_allele/(population_size*2))
    a_allele_freq.append(a_allele/(population_size*2))
    b_allele_freq.append(b_allele/(population_size*2))

    
    
    AB_allele,Ab_allele,aB_allele,ab_allele = biallele_frequency(individual_allele_list, population_size)
    print(f"AB_freq = {AB_allele/(population_size*2)}, ab_freq = {ab_allele/(population_size*2)}, aB_freq = {aB_allele/(population_size*2)},  Ab_freq = {Ab_allele/(population_size*2)}")
    
    AB_allele_freq.append(AB_allele/(population_size*2))
    ab_allele_freq.append(ab_allele/(population_size*2))
    aB_allele_freq.append(aB_allele/(population_size*2))
    Ab_allele_freq.append(Ab_allele/(population_size*2))
    disequlibrium_now = ((AB_allele/(population_size*2)) - (A_allele/(population_size*2)*B_allele/(population_size*2)))
    print(disequlibrium_now)
    disequlibrium.append(disequlibrium_now)
    # print(f"AB_allele_frequencey = {(AB_allele/(population_size*2))}, A_allele_frequencey = {(A_allele/(population_size*2))}, B_allele_freq  = {B_allele/(population_size*2)}")
    if b_allele == 0:
        random_number  = int(random.uniform(0, population_size))
        # print(random_number)
        # print(individual_allele_list[random_number][0])
        (individual_allele_list[random_number][0])[1] = "b"
        # print(individual_allele_list[random_number][0])
        # print(individual_allele_list)

x = range(iteration)
plt.plot(x, AB_allele_freq, label='AB')
plt.plot(x, ab_allele_freq, label='ab')
plt.plot(x, aB_allele_freq, label='aB')
plt.plot(x, Ab_allele_freq, label='Ab')
plt.plot(x, disequlibrium, label='Disequlibrium')

plt.legend()
plt.show()