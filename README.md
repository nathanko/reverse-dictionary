# Reverse Dictionary
A proof-of-concept app that employs natural language processing to search the Merriam-Webster dictionary for words matching a given definition.

## Backend (`/app`)
API built using `scikit-learn`, `nltk`, and `Flask` and hosted on Heroku.
e.g. [https://reverse-dictionary.herokuapp.com/api/classify?text=cry+vehemently](https://reverse-dictionary.herokuapp.com/api/classify?text=cry+vehemently)

## Frontend (`/rd-frontend`)
Angular app hosted on my [website](https://nathanko.com/reverse-dictionary)!

## Acknowledgements
[Data](https://github.com/adambom/dictionary) for Webster's Unabridged Dictionary provided by Adam Savitzky (adambom). Used under the MIT License and Project Gutenberg License.
