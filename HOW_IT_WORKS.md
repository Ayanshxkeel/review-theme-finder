# Understand and extend Review Theme Finder

## The problem
Reading many comments one by one is slow. This app groups comments with similar wording so a person can inspect recurring themes.

## Code path
1. `pd.read_csv` reads either the sample or an uploaded CSV.
2. The chosen column is cleaned: blank and very short reviews are removed.
3. `TfidfVectorizer` converts each review into a numerical vector of words and two-word phrases.
4. `KMeans` groups vectors around a selected number of centers. The top-weighted phrases and example reviews help a person name each group.
5. The app exports each review with its assigned theme number.

## Try it yourself
With the sample file, choose three themes: setup, price, and delivery should each have four comments. Then choose two themes and observe that two topics get merged. Upload a CSV of your own with a review column.

## A useful change you could make
Add a minimum theme size or let a user rename themes before export. Try a real dataset and record where the grouping is wrong.

## Interview questions
Why do you choose the number of themes? K-means needs that number in advance. Are the top phrases ground truth? No, they are hints; a person must read the comments. What happens to mixed-topic reviews? They may land in an imperfect group.
