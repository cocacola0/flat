from Dataset.GetDataFromFacebookDataset import data, categories
from Parser import arguments
from Usefull import GetTransformedString,GetCategoryIndex
from Statistics import MakeDiscreteImpact, MakeContinuousImpact
#input features => category, total likes, type, month, hour, weekday, paid
#output features

action = GetTransformedString(arguments.action)
input = GetTransformedString(arguments.input)
output = GetTransformedString(arguments.output)

if action == "Impact":
    input_index = GetCategoryIndex(input)
    output_index = GetCategoryIndex(output)

    if input_index == -1:
        print('Error! The input was not found in the category list! Type --help for more info')
    else:
        if output_index == -1:
            print('Error! The output was not found in the category list! Type --help for more info')
        else:
            if input_index == 0:
                print(categories[input_index] + '  ' + categories[output_index])
                MakeContinuousImpact(input_index,output_index)
            else:
                print(categories[input_index] + '  ' + categories[output_index])
                MakeDiscreteImpact(input_index,output_index)

