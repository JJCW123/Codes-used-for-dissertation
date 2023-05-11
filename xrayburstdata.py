# The necessary modules being imported for use within the code
from math import log10
import linecache

# Creating all the needed isotopic abundance lists and atomic mass number lists
abundance_list = []
atomic_m_num_list = []
abundance_list2 = []
atomic_m_num_list2 = []
abundance_list_proper2 = []
atomic_m_num_list_proper2 = []

# A loop to go over the entire XRB isotope net work
for x in range(5241):
    # Only appending values for mass numbers that are relevant
    if x < 3 or x > 83:
        continue
    else:
        # Taking the relevant line number from the flux files and storing it
        line_required = linecache.getline(
            'C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/'
            'Test Environment/2022HIG4.results', x)

        # Element required is used to store the lines for each isotope
        element_required1 = line_required
        # Atomic mass number required is used to store the lines for each isotopes mass number
        atomic_m_num1 = line_required
        atomic_m_num1 = atomic_m_num1[4:]
        atomic_m_num1 = atomic_m_num1[:3]
        # Removing all irrelevant characters left of the data
        element_required1 = element_required1[10:]
        # Removing all irrelevant characters right of the data
        element_required1 = element_required1[:8]
        # Append the relevant data into the flux data list
        abundance_list.append(element_required1)
        atomic_m_num_list.append(atomic_m_num1)

        # Doing the same as above for a second isotope at once
        element_required2 = line_required
        atomic_m_num2 = line_required
        atomic_m_num2 = atomic_m_num2[22:]
        atomic_m_num2 = atomic_m_num2[:3]
        # Removing all irrelevant characters left of the data
        element_required2 = element_required2[28:]
        # Removing all irrelevant characters right of the data
        element_required2 = element_required2[:8]
        # Append the relevant data into the flux data list
        abundance_list.append(element_required2)
        atomic_m_num_list.append(atomic_m_num2)

        # The same as above for a third isotope
        element_required3 = line_required
        atomic_m_num3 = line_required
        atomic_m_num3 = atomic_m_num3[40:]
        atomic_m_num3 = atomic_m_num3[:3]
        # Removing all irrelevant characters left of the data
        element_required3 = element_required3[46:]
        # Removing all irrelevant characters right of the data
        element_required3 = element_required3[:8]
        # Append the relevant data into the flux data list
        abundance_list.append(element_required3)
        atomic_m_num_list.append(atomic_m_num3)

        # The same as above for the fourth isotope
        element_required4 = line_required
        atomic_m_num4 = line_required
        atomic_m_num4 = atomic_m_num4[58:]
        atomic_m_num4 = atomic_m_num4[:3]
        # Removing all irrelevant characters left of the data
        element_required4 = element_required4[64:]
        # Removing all irrelevant characters right of the data
        element_required4 = element_required4[:8]
        # Append the relevant data into the flux data list
        abundance_list.append(element_required4)
        atomic_m_num_list.append(atomic_m_num4)


# Removing the deuterium values from each list
abundance_list.pop(0)
atomic_m_num_list.pop(0)

# The same loop used to go over the iso mass abundance files for the common envelope data
for x in range(5241):
    if x < 10:
        continue
    else:
        # Taking the relevant line number from the flux files and storing it
        linerequired2 = linecache.getline(
            'C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/'
            'Test Environment/Original data no reaction changes/f1a5mcr1.5md2e-5/N_Traj_rmin=4.9695E+06/'
            'iso_massf00330.DAT', x)
        atom_m_numa2 = linerequired2
        # Removing all irrelevant characters left of the data
        linerequired2 = linerequired2[24:]
        # Removing all irrelevant characters right of the data
        linerequired2 = linerequired2[:11]
        # Append the relevant data into the flux data list
        abundance_list2.append(linerequired2)

        atom_m_numa2 = atom_m_numa2[39:]
        atomic_m_num_list2.append(atom_m_numa2)


# Removing all null abundance values from the abundance lists and placing the correct values into the proper list
for i in range(len(atomic_m_num_list2)):
    if abundance_list2[i] == '1.00000E-99':
        continue
    else:
        abundance_list_proper2.append(abundance_list2[i])
        atomic_m_num_list_proper2.append(atomic_m_num_list2[i])

# Converting all values to floats for logarithms to be taken
for i in range(len(abundance_list)):
    abundance_list[i] = float(abundance_list[i])

# Doing the same as above for the second abundance list
for i in range(len(abundance_list_proper2)):
    abundance_list_proper2[i] = float(abundance_list_proper2[i])

# Taking the logarithms of all values in both abundance lists
abundance_list = [log10(x) for x in abundance_list]
abundance_list_proper2 = [log10(x) for x in abundance_list_proper2]


# Creating a text file to store all the data into two columns of mass and the corresponding mass number
file = open("XRB_abundances_REC.txt", "w")
for index2 in range(len(abundance_list)):
    file.write(str(abundance_list[index2]) + ' ' + str(atomic_m_num_list[index2]) + '\n')
file.close()

