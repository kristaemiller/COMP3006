medID= ['0001', '0002', '0003', '0004', '0005']
MRIsafe= ['aneurysm clip', 'MRI safe pacemaker', 'aneurysm clip', 'no documented implants', 'non-MRI safe pacemaker']
cummulativeMRI= [4, 5, 10, 1, 0]

#how to append to a list
medID.append('0006')
MRIsafe.append('MRI safe pacemaker')

#zip two lists together to make ordered pairs
medID_and_MRIsafe= list(zip(medID, MRIsafe))
print(medID_and_MRIsafe)

#add multiple items to a list
medID_new= medID + ['0007', '0008', '0009', '0010']
print(medID_new)

#range function returns an object that can be converted to a list
medID_newformat= range(1, 11) #start at number 1, end at non-inclusive 11
print(list(medID_newformat))

#print first and last element from a list
first= medID_and_MRIsafe[0]
print(first)
last= medID_and_MRIsafe[-1]
print(last)

#length of a list
print(len(medID_and_MRIsafe))

#how many patients have aneurysm clips?
aneurysm_clip= MRIsafe.count('aneurysm clip')
print(aneurysm_clip)

def first_plus_last(lst):
    return lst[0]+ lst[-1]

print(first_plus_last([2,4,5,6,7,8]))

#every patient today gets another MRI, update their cummulative count
updated_cummulative= []
for patient in cummulativeMRI:
    updated_cummulative.append(patient+1)
print(updated_cummulative)

#print out a list of everyone!
for patient in medID_and_MRIsafe:
    print(patient)

#warning pop-up
warning= "Warning: This patient has non-MRI safe implant"

for i in range(3):
    print(warning)

#we want to check if any patient on today's schedule has an MRI safe pacemaker:
for patient in MRIsafe:
    if patient == 'MRI safe pacemaker':
        print ("Today we have a patient with a MRI safe pacemaker, contact cardiologist to monitor settings")
        break #will only print once instead of twice

index=0
while index< len(MRIsafe):
    print(MRIsafe[index])
    index += 1

for patient in medID_and_MRIsafe:
    for mednumber in patient:
        print(mednumber)

#list comprehensions
safe_for_MRI= [MRI for MRI in MRIsafe if MRI=='no documented implants' or MRI=='MRI safe pacemaker']
print(safe_for_MRI)

#practice I/O with this to get a dataset
