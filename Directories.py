#Merge 2 directories together
#Double star means that the argument
#we are passing is a directory
def Merge(dict1, dict2):
    res ={**dict1,**dict2}
    return res

dict1 = { 'ERROR': 404, 'Thing': 888}
dict2 = { 'Luck': 777, 'Apocalypse': 666}
dict3 = Merge(dict1, dict2)
#Directory with the changes made to it
print(dict3)