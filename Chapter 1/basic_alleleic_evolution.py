# -*- coding: utf-8 -*-
"""
Created on Sat May 27 22:13:27 2023

@author: Bhrigu
"""



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



population_size = 1000
alleles_A = ["A","a"]
alleles_B = ["B","B"]
individual_allele_list = []

for i in range(population_size):
    individual_chromosome_1 = [random.choice(alleles_A), random.choice(alleles_B)]
    individual_chromosome_2 = [random.choice(alleles_A), random.choice(alleles_B)]
    
    individual_allele_list.append([individual_chromosome_1,individual_chromosome_2])




A_allele,B_allele,a_allele,b_allele = allele_frequency(individual_allele_list, population_size)
print(f"A_freq = {A_allele/(population_size*2)}, B_freq = {B_allele/(population_size*2)}, a_freq = {a_allele/(population_size*2)}, b_freq = {b_allele/(population_size*2)}")

recombination_frequency = 10
A_allele_freq,B_allele_freq,a_allele_freq,b_allele_freq = [],[],[],[]

iteration = 1000

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
    if b_allele == 0:
        random_number  = int(random.uniform(0, population_size))
        # print(random_number)
        # print(individual_allele_list[random_number][0])
        (individual_allele_list[random_number][0])[1] = "b"
        # print(individual_allele_list[random_number][0])
        # print(individual_allele_list)
x = range(iteration)
plt.plot(x, A_allele_freq, label='A')
plt.plot(x, B_allele_freq, label='B')
plt.plot(x, a_allele_freq, label='a')
plt.plot(x, b_allele_freq, label='b')

plt.legend()
plt.show()