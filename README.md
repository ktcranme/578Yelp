# Installation

1. Install Python 3.6 or up
2. Install python libraries [you could create a virtualenv if you want to]

        pip install -r requirements.txt

3. Download spacy en corpus

        python -m spacy download en

3. Install mongodb
4. Create database `yelp` with collections `reviews` and `business`

# Import Yelp dataset and clean and create indices

1. Run mongoimport command to read json into your local mongo collections

        $ mongoimport -d yelp -c business <yelp_academic_dataset_business.json>

        $ mongoimport -d yelp -c reviews <path to yelp_academic_dataset_review.json>

2. Delete business data which are not restaurants or canadian or closed
        
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

        db.checkins.deleteMany({'business_id: {$in: food_ids}})
        db.reviews.deleteMany({'business_id': {$in: food_ids}})
        db.business.deleteMany({'business_id': {$in: food_ids}})

# Run app

1. Run the flask server and head to localhost:5000

        python run.py 

