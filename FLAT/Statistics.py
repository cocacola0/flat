from Dataset.GetDataFromFacebookDataset import data,categories
import matplotlib.pyplot as plt

def MakeDiscreteImpact(input,output):

    States = []

    for row in data:
        found = False
        for i in States:
            if i == row[input]:
                found = True

        if not found:
            States.append(row[input])

    States.sort()

    Values = []

    for i in range(0,len(States)):
        Values.append([])


    for row in data:
        for i in range(0,len(States)):
            if States[i] == row[input]:
                pos = i

        Values[pos].append(row[output])

    Mean = []

    for i in Values:
        s = 0
        for j in i:
            s = s + j
        s = s/len(i)

        Mean.append(s)


    plt.figure(figsize=(12,4))

    print(States)
    print(Mean)

    plt.bar(States,Mean)
    plt.xticks(States,States)

    plt.xlabel(categories[input])
    plt.ylabel(categories[output])

    plt.show()

def MakeContinuousImpact(input,output):

    input_val = []
    output_val = []

    for row in data:
        input_val.append(row[input])
        output_val.append(row[output])

    plt.plot(input_val,output_val,'ro')
    plt.xlabel(categories[input])
    plt.ylabel(categories[output])
    plt.show()