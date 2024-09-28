# Decision Tree Regressor with Mean Absolute Error (MAE) Calculation

This Python script uses a **Decision Tree Regressor** from the Scikit-learn library to predict house prices. It calculates the **Mean Absolute Error (MAE)** to evaluate the model's prediction accuracy and determines the best number of `max_leaf_nodes` based on the lowest MAE value.

## Script Overview:
This script does the following:

1. Reads a dataset from a CSV file containing house prices and features.
2. Trains a *Decision Tree Regressor* using different values for max_leaf_nodes.
3. Calculates the **Mean Absolute Error (MAE)** for each `max_leaf_nodes` value.
4. Displays the best `max_leaf_nodes value` *(i.e., the one that gives the lowest MAE)*.
5. Allows you to manually check the MAE for a given `max_leaf_nodes value`.

## Key Functionality

1. `max_mae(max_leaf_nodes, trainx, testx, trainy, testy)`:\
 Trains the **Decision Tree Regressor** with the specified max_leaf_nodes and returns the MAE for that model.
2. `train_test_split`:\
        Splits the dataset into training and testing sets.
3. `Looping over max_leaf_nodes values`:\
        Trains the model for multiple values of **max_leaf_nodes** and calculates the MAE for each one.

## Output
The script outputs:

1. The **MAE for each tested value**         of `max_leaf_nodes`. 
2. The **minimum MAE** and the corresponding best `max_leaf_nodes` value. 
3. The **MAE for any user-selected `max_leaf_nodes` value** within the testing range.