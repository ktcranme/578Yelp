# Installation

1. Install Python 3.6 or up
2. Install python libraries [you could create a virtualenv if you want to]

        pip install -r requirements.txt

3. Download spacy en corpus

        python -m spacy download en

3. Install mongodb
4. Create database `yelp` with collections `reviews` and `business`

# Import Yelp dataset
1. Run mongoimport command to read json into your local mongo collections

        $ mongoimport -d yelp -c business <yelp_academic_dataset_business.json>

        $ mongoimport -d yelp -c reviews <path to yelp_academic_dataset_review.json>

2. Create an index on the date column. Use mongo cli or Robo3T

        db.reviews.createIndex({'date': 1, 'business_id': 1})
        db.reviews.createIndex({'business_id': 1, 'date': 1})

# Delete non-restaurants and canadian establishments
1. Run on mongo cli or a client
        
        var food_ids = []
        db.business.find(
            {
                '$or':[
                    {'categories': {'$not': /.*Restaurants.*/}},
                    {'state': {'$in': ['AB','BC','MB','NB','NL','NT','NS','NU','ON','PE','QC','SK','YT']}},
                    {'is_open': 0}
                ]
            },
            {'business_id': 1}
        ).forEach(row => {
             food_ids.push(row['business_id'])
        })

        db.reviews.deleteMany({'business_id': {$in: food_ids}})
        db.business.deleteMany({'business_id': {$in: food_ids}})

# Run app

1. Run the flask server and head to localhost:5000

        python run.py 

