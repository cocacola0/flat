import argparse
from Dataset.GetDataFromFacebookDataset import categories

input_display = "1 for category, 2 for total likes, 3 for types, 4 for month, 5 for hour, 5 for weekday, 7 for paid"

output_display = ""


parser = argparse.ArgumentParser()

parser.add_argument('--action', type=str, help = 'The action you want to do: Impact',default='impact')

parser.add_argument('--input',type=str, help = 'Enter the feature you want to use: ' + str(categories[:6]),nargs='+')
parser.add_argument('--output',type=str, help = 'Enter the output you want to correlate the input to ' + str(categories[7:]),nargs='+')

arguments = parser.parse_args()