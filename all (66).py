# cook your dish here
with open("phyton.txt","r") as f:
data=f.read()
new_data=data.replace("java","phyton")
print(new_data)
with open("phytin.txt","w") as f:
    f.write(new_data)