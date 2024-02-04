
# Wall Street Guess

An online game its humans vs AI competing in who can guess more stocks correctly if they will increase higher or lower within 24 hrs

# How to play

1. Create an account with an email and password
2. Look at the stock of the day and it's price
3. Guess if the stock will be up or down by 3pm the next calander day
4. Your stats will be recorded and represented in the accounts tab, try to get the longest streak possible
5. The AI's guess and streak will appear, try to beat it!

# Aim
The results of this game will provide banks, scientists, and corporations data regarding the confidence level of a certain stock per geographical location.

This is partiuclarly interesting for banks and corporate companies to contribute funding to the project to have their chosen stock appear for the day to achieve data that they would like.

# Machine Learning
Integrated a machine learning model, specifically a Random Forest Classifier, into our project. This model has been trained on an S&P500 dataset to make predictions based on historical stock price data. It predicts at a high accuracy if the stock price will close higher or lower than the live price pulled from the finhubb API. Additionally, the model takes in voters' predictions as a parameter to continually improve performance.



