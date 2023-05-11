# Importing the log10 function from the math module
from math import log10
# Importing os to change directories
import os
# Importing line cache in order to store the lines from the text file
import linecache

# Creating the first abundance list
abundance_list = []
# Creating a second abundance list that will be the final list
abundance_list_proper = []
# A list to contain the A number of each and every isotope
atomic_m_num_list = []
# The final list that will be used for mass number A storage
atomic_m_num_list_proper = []

# A second set of abundance and atomic number lists to store a second set of data/trajectory
abundance_list2 = []
abundance_list_proper2 = []
atomic_m_num_list2 = []
atomic_m_num_list_proper2 = []

# Changing to the first directory. The user will need to put a directory where their first trajectory is contained
os.chdir('C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment'
         '/Original data no reaction changes/f1a5mcr1.5md2e-5/N_Traj_rmin=4.9695E+06')

# A for loop that will be used in order to read all the lines of the text file and store them in the corresponding lists
for x in range(5241):
    # Skipping over the first 10 lines that are just comments with information or hydrogen and hydrogen isotopes using
    # continue
    if x < 10:
        continue
    else:
        # Taking the relevant line number from the flux files and storing it
        linerequired = linecache.getline('C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment/Original data no reaction changes/f1a5mcr1.5md2e-5/N_Traj_rmin=4.9695E+06/Orig iso_massf00330 rmin_4.9695 Ac_1e-5.DAT', x)
        # Storing the line in atomic_m_num
        atom_m_num = linerequired
        # Removing all irrelevant characters left of the data
        linerequired = linerequired[24:]
        # Removing all irrelevant characters right of the data
        linerequired = linerequired[:11]
        # Append the relevant data into the flux data list
        abundance_list.append(linerequired)
        # Applying the exact same idea to the atomic m num
        atom_m_num = atom_m_num[39:]
        # Appending to the atomic m number list
        atomic_m_num_list.append(atom_m_num)

# Changing directory to where the second trajectory is stored
os.chdir('C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment'
         '/With 22Mg25Al reaction decreased by 2/f1a5mcr1.5md2e-5/N_Traj_rmin=4.9695E+06')

# The same loop for looping over the lines
for x in range(5241):
    # Skipping the first 10 lines again
    if x < 10:
        continue
    else:
        # Taking the relevant line number from the flux files and storing it
        linerequired2 = linecache.getline(
            'C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment/With 22Mg25Al reaction decreased by 2/f1a5mcr1.5md2e-5/N_Traj_rmin=4.9695E+06/15O_dby_5 iso_massf00330 rmin_4.9695 Ac_1e-5.DAT', x)
        atom_m_num2 = linerequired2
        # Removing all irrelevant characters left of the data
        linerequired2 = linerequired2[24:]
        # Removing all irrelevant characters right of the data
        linerequired2 = linerequired2[:11]
        # Append the relevant data into the flux data list
        abundance_list2.append(linerequired2)

        # Following the same process for the atomic mass number
        atom_m_num2 = atom_m_num2[39:]
        atomic_m_num_list2.append(atom_m_num2)

# Creating a final list for the atomic mass number
correct_atom_num = []

# Only keeping consecutive numbers i.e. 1 2 3 ... For when the abundances are summed over mass number
for j in atomic_m_num_list:
    if j not in correct_atom_num:
        correct_atom_num.append(j)

# A loop for removing all abundances that are 1e-99 i.e. they are virtually zero
for i in range(len(atomic_m_num_list2)):
    if abundance_list2[i] == '1.00000E-99' and abundance_list[i] == '1.00000E-99':
        continue
    else:
        # Appending into the 'proper' lists the abundances that aren't virtually zero
        abundance_list_proper.append(abundance_list[i])
        atomic_m_num_list_proper.append(atomic_m_num_list[i])
        abundance_list_proper2.append(abundance_list2[i])
        atomic_m_num_list_proper2.append(atomic_m_num_list2[i])

# Changing to the final directory where the text files will be stored
os.chdir('C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test Environment')

# Creating a list to keep the summed second trajectory abundances in
summed_abundance_list2 = []

# Converting all values in the abundance lists to floats to store in perform logarithms
for i in range(len(abundance_list_proper)):
    abundance_list_proper[i] = float(abundance_list_proper[i])
    abundance_list_proper2[i] = float(abundance_list_proper2[i])

# Converting all values in atomic m num lists to integers for math operations
for i in range(len(abundance_list_proper)):
    atomic_m_num_list_proper[i] = int(atomic_m_num_list_proper[i])
    atomic_m_num_list_proper2[i] = int(atomic_m_num_list_proper2[i])

# Creating a summed abundances list for the first trajectory abundances
summed_abundance_list = []
# A list I used to check correctness
chec_list = []

# For j in range of the maximum mass A number
for j in range(213):
    # Create a summing variable
    summ = 0
    # For d in range of all isotopes
    for d in range(len(atomic_m_num_list_proper2)):
        # If the atomic mass number of the isotope matches j then append the abundance into the temporary variable
        if atomic_m_num_list_proper2[d] == j:
            # Store the abundance of the mass number thats the same as the counter j
            temp = abundance_list_proper2[d]
            # Summ all abundances of the isotopes with the same A number
            summ = summ + temp

    # Appending for each mass number j the summed abundances
    summed_abundance_list.append(summ)
    # The check list for checking its the correct mass number
    chec_list.append(atomic_m_num_list_proper[j])

# Creating another final atomic mass number list
correct_atom_num1 = []

# Removing all mass numbers that have no abundance
for j in atomic_m_num_list_proper:
    if j not in correct_atom_num1:
        correct_atom_num1.append(j)

# The exact same summing operation being used for the secondary list
for j in range(213):
    summ1 = 0
    for d in range(len(atomic_m_num_list_proper)):
        if atomic_m_num_list_proper[d] == j:
            temp1 = abundance_list_proper[d]
            summ1 = summ1 + temp1

    summed_abundance_list2.append(summ1)


# Removing the first two values of both lists as they are deuterium and tritium
summed_abundance_list2.pop(0)
summed_abundance_list2.pop(0)
summed_abundance_list.pop(0)
summed_abundance_list.pop(0)

# Creating a ratio list that can be used to create ratio'd data sets such as initial over final and so on
ratio_list = []

# A loop that converts all values that aren't 0 in the summed abundance lists into log 10 values
for d in range(len(summed_abundance_list)):
    if summed_abundance_list[d] == 0:
        continue
    else:
        summed_abundance_list[d] = log10(summed_abundance_list[d])

    if summed_abundance_list2[d] == 0:
        continue
    else:
        summed_abundance_list2[d] = log10(summed_abundance_list2[d])

# a proper ratio list which is the final used ratio list
ratio_list_proper = []
# Atomic m num list manually made
atomic_m_num_list_proper_print = []

# Manually listing out 2 - 213 for atomic m numbers
final_atomic_m_list2 = list(range(2, 213))

# Creating a text file that has the data outputted into two columns ready for plotting via GNUPLOT
file = open("Summed_abundance_15Odby5_4p9695_ac_1e-5.txt", "w")
for index1 in range(len(summed_abundance_list)):
     file.write(str(summed_abundance_list[index1]) +'\t'+ str(final_atomic_m_list2[index1]) + '\n')
file.close()
