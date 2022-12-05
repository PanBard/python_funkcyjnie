import  pickle
file_path = "./txt_folder/5_14.serek"

set_1 = set([1,2,3,4,5,5,4,124,123,1,3])

print("Set 1:",set_1)

with open(file_path,'wb') as binary_file:
    pickle.dump(set_1,binary_file)
    print(type(binary_file))
print("Serlialization end")

with open(file_path, 'rb') as binary_file2:
    set_2 = pickle.load(binary_file2)
    print(type(binary_file2))

print("Deserlialization set: ",set_2," ",type(set_2))



