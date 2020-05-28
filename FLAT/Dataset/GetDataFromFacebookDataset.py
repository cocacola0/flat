import pandas

# We export the data using a list of lists
data = []

categories = ["Page Total Likes","Type", "Category", "Post Month", "Post Weekday", "Post Hour", "Paid", "Lifetime Post Total Reach",
              "Lifetime Post Total Impressions", "Lifetime Engaged Users", "Lifetime Post Consumers", "Lifetime Post Consumptions",
              "Lifetime Post Impressions by People Who Liked Your Page", "Lifetime Post Reach by People who Liked Your Page",
              "Lifetime People who have liked your Page and engaged with your post", "Comment", "Like", "Share", "Total Interactions"]


# We open the file as a data-frame using pandas, than convert it to numpy array
df = (pandas.read_csv('Dataset/dataset_Facebook.csv')).to_numpy()


for row in df:

    # We take every numpy array obtained previously and convert it to a string in order to remove any unnecessary
    # characters, than be split the string using ';' as a delimiter.

    row = str(row)

    row = row.replace("[" ,"")
    row = row.replace("'","")
    row = row.replace("]","")

    row = row.split(';')

    # Than we convert the rest of the array to int, and were we find missing spots in the data we fill in 0
    for i in range(0,len(row)):
        if i!=1:
            if row[i] == "":
                row[i] = 0
            else:
                row[i] = int(row[i])

    # We group the data based on category in lists
    data.append(row)