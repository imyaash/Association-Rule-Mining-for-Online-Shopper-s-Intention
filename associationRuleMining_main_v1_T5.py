# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:06:49 2022

@author: imyaash-admin
"""

# Load the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import utils
from apyori import apriori

# Read the dataset from a CSV file
df = pd.read_csv("Datasets/online_shoppers_intention.csv")

# Drop the first 10 columns of the dataframe
df = df.drop(df.iloc[:, 0:10], axis = 1)

# Add new string values to several columns in the dataframe
df["OperatingSystems"] = "os" + df["OperatingSystems"].map(str)
df["Browser"] = "b" + df["Browser"].map(str)
df["Region"] = "r" + df["Region"].map(str)
df["TrafficType"] = "t" + df["TrafficType"].map(str)
df["Weekend"] = "w" + df["Weekend"].map(str)
df["Revenue"] = "revenue" + df["Revenue"].map(str)


def associationRuleDataPrep(df):
    # Create an empty dictionary to store the data for the new dataframe
    newDF = {}
    
    # Loop over the columns of the input dataframe
    for i in df.columns:
        
        # Get the unique values in the current column
        uVal = list(df[i].unique())
        
        # Create a list of lists where each inner list corresponds to a unique value in the column
        listList = [[] for i in uVal]
        
        # Loop over each unique value in the column
        for j in range(len(uVal)):
            
            # Loop over each data point in the original dataframe
            for k in df[i]:
                
                # Check if the value in the current column matches the unique value
                if k == uVal[j]:
                    # If it does, add "Yes" to the corresponding inner list
                    listList[j].append("Yes")
                else:
                    # If it doesn't, add "No" to the corresponding inner list
                    listList[j].append("No")
                    
        # Loop over each inner list in the list of lists
        for i in range(len(listList)):
            # Add the data to the dictionary using the unique value as the key
            newDF[str(uVal[i])] = listList[i]
            
    # Create a new dataframe from the dictionary
    newDF = pd.DataFrame.from_dict(newDF)
    
    # Return the new dataframe
    return newDF

#Apply associationRuleDataPrep function to the dataset
df = associationRuleDataPrep(df)

"""Association Rules"""
# Create a bar plot that shows the number of "Yes" and "No" values for each column in the input dataframe

# Count the number of "Yes" values in the dataframe
yes = (df == "Yes").sum()

# Count the number of "No" values in the dataframe
no = (df == "No").sum()

# Concatenate the "Yes" and "No" series together into a new dataframe
dfP = pd.concat([yes, no], axis = 1, keys = ["yes", "no"])

# Plot the data using the "plot.bar()" method
ax = dfP.plot.bar(stacked = True)
# Show the plot
plt.show()


"""Mining for Association Rule"""
# Pre-process the data using the "data_prepare()" function
dfT = utils.data_prepare(df)

# Find the association rules using the "apriori()" function
rules1 = list(apriori(dfT, min_support = 0.05, min_confidence = 0.05))

# Extract the association rules that have a "revenueTrue" value using the "extract()" function
associationRules_revenueT = utils.extract(rules1, "revenueTrue")

# Create a new dataframe with the association rules
dfR1 = pd.DataFrame(associationRules_revenueT, columns = ["LHS", "RHS", "Support", "Confidence", "Lift"])

# Filter the dataframe to only include rules with a "RHS" of length 1 and a "LHS" of length greater than 1
dfR_revenueT = dfR1[dfR1["RHS"].apply(lambda x: len(x) == 1)]
dfR_revenueT = dfR_revenueT[dfR_revenueT["LHS"].apply(lambda x: len(x) > 1)]

# Print the resulting dataframe
dfR_revenueT



# Pre-process the data using the "data_prepare()" function
dfT = utils.data_prepare(df)

# Find the association rules using the "apriori()" function
rules2 = list(apriori(dfT, min_support = 0.2, min_confidence = 0.2))

# Extract the association rules that have a "revenueFalse" value using the "extract()" function
associationRules_revenueF = utils.extract(rules2, "revenueFalse")

# Create a new dataframe with the association rules
dfR2 = pd.DataFrame(associationRules_revenueF, columns = ["LHS", "RHS", "Support", "Confidence", "Lift"])

# Filter the dataframe to only include rules with a "RHS" of length 1 and a "LHS" of length greater than 1
dfR_revenueF = dfR2[dfR2["RHS"].apply(lambda x: len(x) == 1)]
dfR_revenueF = dfR_revenueF[dfR_revenueF["LHS"].apply(lambda x: len(x) > 1)]

# Print the resulting dataframe
dfR_revenueF
