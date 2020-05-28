from Dataset.GetDataFromFacebookDataset import categories

#example of input: ['Lifetime', 'Post', 'Total', 'Reach']
#expected output Lifetime Post Total Reach

def GetTransformedString(x):
    x = str(x)
    x = x.replace("[","")
    x = x.replace("]","")
    x = x.replace("'","")
    x = x.replace("'","")
    x = x.replace(",","")

    return x

#example of input: Type
#expected output: 2
def GetCategoryIndex(x):

    for i in range(0,len(categories)):
        if categories[i] == x:
            return i
    return -1
