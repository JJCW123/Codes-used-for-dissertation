from math import log10
import os
import linecache

# Creating an isotopic abundance list and a proper one as well as two lists for atomic mass numbers
abundance_list = []
abundance_list_proper = []
atomic_m_num_list = []
atomic_m_num_list_proper = []

# Creating a second set of lists to ratio against the first set of lists
abundance_list2 = []
abundance_list_proper2 = []
atomic_m_num_list2 = []
atomic_m_num_list_proper2 = []

# Changing the directory to the original rate datas trajectory
os.chdir('C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment'
         '/Original data no reaction changes/f1a5mcr1.5md2e-5/N_Traj_rmin=2.5444E+06')

# A loop going over every single isotope stored in the data file
for x in range(5241):
    # Skipping the first 10 lines using continue as they are of use
    if x < 10:
        continue
    else:
        # Taking the relevant line number from the flux files and storing it
        linerequired = linecache.getline('C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment/Original data no reaction changes/f1a5mcr1.5md2e-5/N_Traj_rmin=2.5444E+06/iso_massf00330 orig.DAT', x)

        # Atomic m num list for storing the line of the file
        atom_m_num = linerequired
        # Removing all irrelevant characters left of the data
        linerequired = linerequired[24:]
        # Removing all irrelevant characters right of the data
        linerequired = linerequired[:11]
        # Append the relevant data into the flux data list
        abundance_list.append(linerequired)

        # Storing the atomic mass numbers in the appropriate list
        atom_m_num = atom_m_num[39:]
        atomic_m_num_list.append(atom_m_num)

# Changing directory to the reduced rate trajectory location
os.chdir('C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment'
         '/With 22Mg25Al reaction decreased by 2/f1a5mcr1.5md2e-5/N_Traj_rmin=2.5444E+06')

# The same loop used above to append the second isomass files data into the corresponding lists
for x in range(5241):
    if x < 10:
        continue
    else:
        # Taking the relevant line number from the flux files and storing it
        linerequired2 = linecache.getline(
            'C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment/With 22Mg25Al reaction decreased by 2/f1a5mcr1.5md2e-5/N_Traj_rmin=2.5444E+06/22mg_dby_2_rmin_2p5444_iso_massf00330.DAT', x)
        atom_m_num2 = linerequired2
        # Removing all irrelevant characters left of the data
        linerequired2 = linerequired2[24:]
        # Removing all irrelevant characters right of the data
        linerequired2 = linerequired2[:11]
        # Append the relevant data into the flux data list
        abundance_list2.append(linerequired2)


        atom_m_num2 = atom_m_num2[39:]
        atomic_m_num_list2.append(atom_m_num2)

# Moving all abundances that arent 0 over to the 'proper' lists
for i in range(len(atomic_m_num_list2)):
    if abundance_list2[i] == '1.00000E-99' and abundance_list[i] == '1.00000E-99':
        continue
    else:
        abundance_list_proper.append(abundance_list[i])
        atomic_m_num_list_proper.append(atomic_m_num_list[i])
        abundance_list_proper2.append(abundance_list2[i])
        atomic_m_num_list_proper2.append(atomic_m_num_list2[i])

# Changing directory to where the user wants the data text files to be stored
os.chdir('C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment')

# Creating the second summed abundance list
summed_abundance_list2 = []

# Converting all values to floats in order to log them later
for i in range(len(abundance_list_proper)):
    abundance_list_proper[i] = float(abundance_list_proper[i])
    abundance_list_proper2[i] = float(abundance_list_proper2[i])

# Converting the atomic m num lists into integers for math operations
for i in range(len(abundance_list_proper)):
    atomic_m_num_list_proper[i] = int(atomic_m_num_list_proper[i])
    atomic_m_num_list_proper2[i] = int(atomic_m_num_list_proper2[i])

# Creating the first summed abundance list
summed_abundance_list = []

# Creating the loop to the maximum mass number and sum the abundances of each consecutive A
for j in range(213):
    # Summing variable
    summ = 0
    # Going over every single isotope in the mass number lists
    for d in range(len(atomic_m_num_list_proper2)):
        # If the mass number is equal to the counting variable j
        if atomic_m_num_list_proper2[d] == j:
            # Store the abundance of the corresponding isotope into the temporary variable
            temp = abundance_list_proper2[d]
            # Summ the temporary value
            summ = summ + temp

    # Append the summed abundance of each A to the summed abundance list
    summed_abundance_list.append(summ)

# Performing the exact same loop for the second isomass files data
for j in range(213):
    summ1 = 0
    for d in range(len(atomic_m_num_list_proper)):
        if atomic_m_num_list_proper[d] == j:
            temp1 = abundance_list_proper[d]
            summ1 = summ1 + temp1

    summed_abundance_list2.append(summ1)

# Removing the first 2 values from both summed abundance lists as they are not of use
summed_abundance_list2.pop(0)
summed_abundance_list2.pop(0)
summed_abundance_list.pop(0)
summed_abundance_list.pop(0)

# Creating the ratio list
ratio_list = []

# A loop taking the ratio of both lists values against one another unless they are 0
for m in range(len(summed_abundance_list)):
    if summed_abundance_list2[m] == 0 or summed_abundance_list[m] == 0:
        ratio_list.append(0)
    else:
        ratio_list.append(summed_abundance_list[m] / summed_abundance_list2[m])

# Logging all of the values within the ratio'd abundance lists
for d in range(len(ratio_list)):
    if ratio_list[d] == 0:
        continue
    else:
        ratio_list[d] = log10(ratio_list[d])

# Creating the final used ratio list
ratio_list_proper = []
# Print checking list for the atomic mass numbers
atomic_m_num_list_proper_print = []

# If the log value of an A number abundance is greater than log10(6) or log10(-6) it is not appended into the
# proper list
for z in range(len(ratio_list)):
    if ratio_list[z] > 6 or ratio_list[z] < -6:
        continue
    else:
        ratio_list_proper.append(ratio_list[z])
        atomic_m_num_list_proper_print.append(atomic_m_num_list_proper[z])

# Creating the final manually made atomic m num list
final_atomic_m_list2 = list(range(2, 213))

# Creating a text file with the below name that stores the data into a text file in two columns
file = open("Summed_22Mgdby2_rmin_2p5444.txt", "w")
for index1 in range(len(ratio_list_proper)):
     file.write(str(ratio_list[index1]) +'\t'+ str(final_atomic_m_list2[index1]) + '\n')
file.close()
