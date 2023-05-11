from math import log10
import os
import linecache

# Creating all the required abundance lists and the atomic mass number lists
jenn_abundance_list = []
atomic_m_num_jenn_list = []
abundance_list = []
atomic_m_num_list = []
abundance_list2 = []
atomic_m_num_list2 = []
abundance_list_proper2 = []
atomic_m_num_list_proper2 = []
summed_list = []
summed_abundance_list = []

# A loop for appending all the XRB data into the required lists
for x in range(5241):
    # Skipping all irrelevant values
    if x < 3 or x > 83:
        continue
    else:
        # Taking the relevant line number from the flux files and storing it
        line_required = linecache.getline(
            'C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/'
            'Test Environment/2022HIG4.results', x)

        # Element required is used to store the line number for the isotopes
        element_required1 = line_required
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

        # Performing the same operation for a second isotope to be done at once
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

        # Performing the same operation for a third isotope to be done at once
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

        # Performing the same operation for a fourth isotope to be done at once
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

# Repeating the entire same process as above however this time for an XRB rate called JENN which I thought was
# the normal rate which later I found out to be the REC rate
for x in range(5241):
    if x < 3 or x > 83:
        continue
    else:
        # Taking the relevant line number from the flux files and storing it
        line_required5 = linecache.getline(
            'C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/'
            'Test Environment/2022JENN4.results', x)

        element_required_jenn = line_required5
        atomic_m_num_jenn = line_required
        atomic_m_num_jenn = atomic_m_num_jenn[4:]
        atomic_m_num_jenn = atomic_m_num_jenn[:3]
        # Removing all irrelevant characters left of the data
        element_required_jenn = element_required_jenn[10:]
        # Removing all irrelevant characters right of the data
        element_required_jenn = element_required_jenn[:8]
        # Append the relevant data into the flux data list
        jenn_abundance_list.append(element_required_jenn)
        atomic_m_num_jenn_list.append(atomic_m_num_jenn)

        element_required2_jenn = line_required5
        atomic_m_num2_jenn = line_required5
        atomic_m_num2_jenn = atomic_m_num2_jenn[22:]
        atomic_m_num2_jenn = atomic_m_num2_jenn[:3]
        # Removing all irrelevant characters left of the data
        element_required2_jenn = element_required2_jenn[28:]
        # Removing all irrelevant characters right of the data
        element_required2_jenn = element_required2_jenn[:8]
        # Append the relevant data into the flux data list
        jenn_abundance_list.append(element_required2_jenn)
        atomic_m_num_jenn_list.append(atomic_m_num2_jenn)

        element_required3_jenn = line_required5
        atomic_m_num3_jenn = line_required5
        atomic_m_num3_jenn = atomic_m_num3_jenn[40:]
        atomic_m_num3_jenn = atomic_m_num3_jenn[:3]
        # Removing all irrelevant characters left of the data
        element_required3_jenn = element_required3_jenn[46:]
        # Removing all irrelevant characters right of the data
        element_required3_jenn = element_required3_jenn[:8]
        # Append the relevant data into the flux data list
        jenn_abundance_list.append(element_required3_jenn)
        atomic_m_num_jenn_list.append(atomic_m_num3_jenn)

        element_required4_jenn = line_required5
        atomic_m_num4_jenn = line_required5
        atomic_m_num4_jenn = atomic_m_num4_jenn[58:]
        atomic_m_num4_jenn = atomic_m_num4_jenn[:3]
        # Removing all irrelevant characters left of the data
        element_required4_jenn = element_required4_jenn[64:]
        # Removing all irrelevant characters right of the data
        element_required4_jenn = element_required4_jenn[:8]
        # Append the relevant data into the flux data list
        jenn_abundance_list.append(element_required4_jenn)
        atomic_m_num_jenn_list.append(atomic_m_num4_jenn)

# Removing the first value of all the lists as they are deuterium values
abundance_list.pop(0)
atomic_m_num_list.pop(0)
jenn_abundance_list.pop(0)
atomic_m_num_jenn_list.pop(0)

# The exact same list process as above however this time for the CE data
for x in range(5241):
    if x < 10:
        continue
    else:
        # Taking the relevant line number from the flux files and storing it
        linerequired2 = linecache.getline(
            'C:/Users/jjosh/PycharmProjects/pythonProject/Project-20230320T094000Z-001/Project/FluxVsTime/Test'
            ' Environment/Original data no reaction changes/f1a5mcr1.5md2e-5/N_Traj_rmin=4.9695E+06/iso_massf00330.DAT',
            x)
        atom_m_numa2 = linerequired2
        # Removing all irrelevant characters left of the data
        linerequired2 = linerequired2[24:]
        # Removing all irrelevant characters right of the data
        linerequired2 = linerequired2[:11]
        # Append the relevant data into the flux data list
        abundance_list2.append(linerequired2)

        atom_m_numa2 = atom_m_numa2[39:]
        atomic_m_num_list2.append(atom_m_numa2)

# Converting all atominc mass number values to integers
for i in range(len(atomic_m_num_list)):
    atomic_m_num_list[i] = int(atomic_m_num_list[i])

# Removing all abundances that are virtually 0 and moving the correct values to the proper value
for i in range(len(atomic_m_num_list2)):
    if abundance_list2[i] == '1.00000E-99':
        continue
    else:
        abundance_list_proper2.append(abundance_list2[i])
        atomic_m_num_list_proper2.append(atomic_m_num_list2[i])

# Converting all abundances to float values for logarithms to be taken
for i in range(len(abundance_list)):
    abundance_list[i] = float(abundance_list[i])
    jenn_abundance_list[i] = float(jenn_abundance_list[i])

# The same process as above but for the second abundance list
for i in range(len(abundance_list_proper2)):
    abundance_list_proper2[i] = float(abundance_list_proper2[i])

# A list for the summed values of the abundance list
jenn_abundance_list_summed = []

# Now to create the summed value abundance lists
# Setting j to count to the max isotope mass number
for j in range(max(atomic_m_num_list)+1):
    # Creating two summ variables
    summ = 0
    summ_jenn = 0
    for d in range(len(atomic_m_num_list)):
        # If d = the current atomic mass number store the abundance value to a temporary variable
        if atomic_m_num_list[d] == j:
            temp = abundance_list[d]
            # Summ for a first set of data
            summ = summ + temp

            temp_jenn = jenn_abundance_list[d]
            # Summ for the jenn rate value
            summ_jenn = summ_jenn + temp_jenn

    # Appending the values into the correct value
    jenn_abundance_list_summed.append(summ_jenn)
    summed_abundance_list.append(summ)

# Removing the first two values from each list
jenn_abundance_list_summed.pop(0)
jenn_abundance_list_summed.pop(0)
summed_abundance_list.pop(0)
summed_abundance_list.pop(0)
# Creating a list to the correct XRB mass number value
final_atomic_m_list = list(range(2, 108))

# Making all values turn unto integers for operations
for i in range(len(atomic_m_num_list_proper2)):
    atomic_m_num_list_proper2[i] = int(atomic_m_num_list_proper2[i])

# Summed abundance abundance list two being created
summed_abundance_list2 = []

# The same summing operation as previously used creating abundance lists for the second abundance list
for j in range(213):
    summ1 = 0
    for d in range(len(atomic_m_num_list_proper2)):
        if atomic_m_num_list_proper2[d] == j:
            temp1 = abundance_list_proper2[d]
            summ1 = summ1 + temp1

    summed_abundance_list2.append(summ1)

# Again manually creating a consecutive number list
final_atomic_m_list2 = list(range(2, 213))
# Removing the first two values from the second value summed abundance list
summed_abundance_list2.pop(0)
summed_abundance_list2.pop(0)

# Ratios of the XRB rates lists being made and another list for the common envelope data
divided_summed_XRB_rates = []
divided_summed_CE_comparison = []

# If the value in the summed abundance list isnt 0 then ratios are created between CE and XRB data and XRB and XRB data
for x in range(len(summed_abundance_list)):
    if summed_abundance_list[x] == 0:
        continue
    else:
        divided_summed_XRB_rates.append(summed_abundance_list[x] / jenn_abundance_list_summed[x])
        divided_summed_CE_comparison.append(summed_abundance_list2[x] / jenn_abundance_list_summed[x])

# Taking the logarithm values of each value in both abundance lists
abundance_list = [log10(x) for x in abundance_list]
abundance_list_proper2 = [log10(x) for x in abundance_list_proper2]

# Taking the logarithms all of all non-zero values in the summed abundance lists
for k in range(len(summed_abundance_list)):
    if summed_abundance_list[k] == 0:
        continue
    else:
        summed_abundance_list[k] = log10(summed_abundance_list[k])

# The same as above for the second summed abundance list
for k in range(len(summed_abundance_list2)):
    if summed_abundance_list2[k] == 0:
        continue
    else:
        summed_abundance_list2[k] = log10(summed_abundance_list2[k])

# The same again for the ratio of XRB to XRB data sets and XRB to CE data sets
for u in range(len(divided_summed_XRB_rates)):
    if divided_summed_XRB_rates[u] == 0:
        continue
    else:
        divided_summed_XRB_rates[u] = log10(divided_summed_XRB_rates[u])

    if divided_summed_CE_comparison[u] == 0:
        continue
    else:
        divided_summed_CE_comparison[u] = log10(divided_summed_CE_comparison[u])

# Creating a text file that stores the abundance and mass numbers in two columns
file = open("CE_ratio_abundances_summed_rmin_4p9695.txt", "w")
for index1 in range(len(divided_summed_CE_comparison)):
   file.write(str(divided_summed_CE_comparison[index1]) + ' ' + str(final_atomic_m_list[index1]) + '\n')
file.close()

# file = open("XRB_abundances_summed_REC_ratio_JENN.txt", "w")
# for index2 in range(len(divided_summed_XRB_rates)):
#     file.write(str(divided_summed_XRB_rates[index2]) + ' ' + str(final_atomic_m_list[index2]) + '\n')
# file.close()

