data_box = [2, 4, 5, 1,"Cat", "Asset"]
# You can input from user to check.
def liner_Search(databox, target):
    for loop1 in range(len(data_box)):
        if databox[loop1] == target:
            return True
        else:
            return False
            
print(liner_Search(data_box,"Asset"))
