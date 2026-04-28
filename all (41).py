# cook your dish here
def print_list(list,idx):
    if idx==len(list):
        return 
    print(list[idx])
    print_list(list,idx+1)

fruits=["apple","mango","bananna","stobary","lichi"]
print(fruits,0)