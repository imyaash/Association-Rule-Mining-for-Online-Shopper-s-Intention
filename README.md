# Online Shoppers Intention Association Rules
This code creates association rules from the online shoppers intention dataset using the apriori algorithm. Association rules are used to identify relationships between variables in a dataset and can be used to predict outcomes.

# Dependencies
The following libraries are required to run this code:

    pandas
    matplotlib
    apyori
    utils

# Usage
To use this code, simply run the script in a Python interpreter. The association rules will be printed to the console.
In addition, the utils module is provided in this repository and must placed in the same directory as other code files.

# Data
The online shoppers intention dataset contains information about online shopping behavior and is used to predict whether a customer will make a purchase or not. The dataset includes the following columns:

    Administrative
    Administrative_Duration
    Informational
    Informational_Duration
    ProductRelated
    ProductRelated_Duration
    BounceRates
    ExitRates
    PageValues
    SpecialDay
    Month
    OperatingSystems
    Browser
    Region
    TrafficType
    VisitorType
    Weekend
    Revenue

# Association Rule Data Preparation
The associationRuleDataPrep() function is used to pre-process the data for association rule mining. It takes in a dataframe and returns a new dataframe with "Yes" and "No" values for each unique value in each column of the original dataframe. This is done by looping over the columns of the input dataframe, getting the unique values in each column, creating a list of lists where each inner list corresponds to a unique value, and then looping over each data point in the original dataframe and adding "Yes" to the corresponding inner list if the value in the current column matches the unique value, or "No" if it doesn't. The data is then added to a dictionary using the unique value as the key and a new dataframe is created from this dictionary.

# Association Rule Mining
The apriori() function from the apyori library is used to mine for association rules in the pre-processed data. The extract() function from the utils module is then used to extract the association rules that have a "revenueTrue" value. The resulting association rules are stored in a new dataframe and printed to the console.
