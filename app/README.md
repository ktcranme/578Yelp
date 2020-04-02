# Installation

1. Install Python 3.6 or up
2. Install python libraries [you could create a virtualenv if you want to]

        pip install -r requirements.txt

3. Install mongodb
4. Create database `yelp` with collections `reviews` and `business`

# Import Yelp dataset
1. Run mongoimport command to read json into your local mongo collections

        $ mongoimport -d yelp -c business <yelp_academic_dataset_business.json>

        $ mongoimport -d yelp -c reviews <path to yelp_academic_dataset_review.json>

2. Create an index on the date column. Use mongo cli or Robo3T

        db.reviews.createIndex({'date':1})

# Run app

1. Run the flask server and head to localhost:5000

        python run.py 


