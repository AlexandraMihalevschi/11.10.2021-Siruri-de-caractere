with open("Prezentare.txt", 'r') as f:
    nume = f.readline()  
    profesia = f.readline()
print(f"""Încântat de cunoștință, {nume}. 
Sper că într-o zi vei deveni {profesia}!""")
