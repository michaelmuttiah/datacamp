# Taken from Data Camp, Python Data Science ToolBox (Part 2)
# Be aware the file 'ind_pop_data.csv' does not exist on my Github
# You grab a copy from: https://github.com/johnashu/datacamp/blob/master/ind_pop_data.csv


# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    #Example of Chunking
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    # Pandas Dataframe
    data = pd.DataFrame()

    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        # Categorised List with conditions
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        # Merge Columns using Zip
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        #Turning Tuple into a List
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]

        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'

plot_pop('ind_pop_data.csv', 'CEB')

# Call plot_pop for country code 'ARB'

plot_pop('ind_pop_data.csv', 'ARB')
