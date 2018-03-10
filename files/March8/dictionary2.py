ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        }, {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}
#getRamit
print ramit['email']

#interests
print ramit['interests']

#jasmineemail
print ramit['friends'][1]['email']

#second of Jan's interest
print ramit['friends'][1]['interests'][1]

