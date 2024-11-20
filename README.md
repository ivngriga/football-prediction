# Predicting Football Matches using FIFA Player Ratings

### Disclaimer

This code was written by 16 year old me. It is more than likely that there are errors in my logic and mistakes were made. Treat results with a grain of salt.

### Purpose

I wanted to see if I could make meaningful match predictions, using the publicly available FIFA card ratings of football players. To do so, I created a scraper to fetch all players for serie A and their ratings and performed logistic & multivariate regression.

### Results

Couldn't discover a combination of parameters for a team that resulted in meaningful predictions with accuracy >> 50% using k-fold cross validation.
Even with 2000+ players and 100+ matches, there simply isn't enough training data collected in this repository to train the model well.

### Potential Improvements

Using bayesian analysis to determine the most meaningful parameters in the training data. Collect more training data from different leagues.