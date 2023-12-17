import pickle
number_of_data = int(input('Enter the number of data : '))
data = []

for i in range(number_of_data):
    raw = input('Enter data '+str(i)+' : ')
    data.append(raw)

# open a file, where you ant to store the data
file = open( 'stuff', 'wb')

# dump information to that file
pickle.dump(data, file)

# close the file
