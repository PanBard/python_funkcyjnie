
dictionary = {"Marus":89 , "Karolina":100 , "Kowid":23 , "Tymon":56 }

print(f"Dictionary (size dict: {len(dictionary)}) before adding new item: ",dictionary)

dictionary["Malecki"] = 2000

print(f"Dictionary (size dict: {len(dictionary)}) after adding new item: ",dictionary)

del dictionary["Marus"]

print(f"Dictionary (size dict: {len(dictionary)}) before deleting first item: ",dictionary)