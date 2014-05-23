criteria = [
    {
        'name': 'Price',
        'inc': "What college student wants to blow three grand on a laptop?",
        'just': "A high price tag will be the deal breaker no matter what."
    },
    {
        'name': 'User Rating',
        'inc': 'User rating gives us a way to quantify satisfaction with the product holistically.',
        'just': 'Ratings often quantify reliability, which is a must in your major.'
    },
    {
        'name': 'Weight',
        'inc': 'The last thing you want is a dumbbell to carry across campus.',
        'just': 'Most of the time with your computer will involve walking rather than programming. '
    },
    {
        'name': 'Screen Size',
        'inc': 'A large screen allows you to look at documents or help pages while having your terminal visible. ',
        'just': 'Being able to see multiple objects at once on your screen greatly increases your effectiveness. '
    },
    {
        'name': 'Power',
        'inc': 'Some of the methods you program have large numbers of computations and high memory usage is unavoidable.',
        'just': "While on those occasions extra power is nice, for the most part it doesn't make a difference in your activities."

    },
    {
        'name': 'Storage',
        'inc': 'You will write programs that produce large amounts of data and want to save it quickly.',
        'just': 'It is nice not to wait forever load and save but it is very little of your overall time.'
    },
    {
        'name': 'Battery Life',
        'inc': 'There are enough power outlets on campus to compensate for poor battery life.',
        'just': 'The only time an outlet might not be available is during lecture which is at most 3 hours straight.'
    }
]

ranking = [
    {
        'name' : "HP Envy 15t Quad Edition",
        'rank': 77.2
    },
    {
        'name' : "Dell Inspiron i15RV-1435BLK",
        'rank': 71.1
    },
    {
        'name' : "Toshiba Satellite C55-A5245",
        'rank': 71.0
    },
    {
        'name' : "MacBook Pro 13\" with Retina Display",
        'rank': 66.9
    },
    {
        'name' : "Lenovo IdeaPad U430",
        'rank': 66.2
    },
    {
        'name' : "ASUS ROG 6750JM-DS71",
        'rank': 66.1
    },
    {
        'name' : "MacBook Air 13\"",
        'rank': 64.7
    },
]

algorithm = [
    {
        'name': 'Price',
        'weight': 30,
        'formula': "img/price_formula.gif",
        'assumption': "$2000 is likely the most a student will be willing to pay for a laptop"
    },
    {
        'name': 'User Rating',
        'weight': 25,
        'formula': "img/user_rating_formula.gif",
        'assumption': "User Ratings are from 1 to 5"
    },
    {
        'name': 'Weight',
        'weight': 20,
        'formula': "img/weight_formula.gif",
        'assumption': "10 lbs is the most a laptop should weigh to be reasonable for a student"
    },
    {
        'name': 'Screen Size',
        'weight': 10,
        'formula': "img/screen_size_formula.gif",
        'assumption': "The largest reasonable laptop screen size is 17 inches"
    },
    {
        'name': 'Power',
        'weight':7,
        'formula': "img/power_formula.gif",
        'assumption': "Quad core, 3 GHz, and 8Gb of RAM are reasonable limits for a student (2*3*8=48)"

    },
    {
        'name': 'Storage',
        'weight': 5,
        'formula': "img/storage_formula.gif",
        'assumption': "An SSD is roughly equivalent to a  10000 rpm optical disk and 512 Gb is a reasonable upper bound on hard drive space"
    },
    {
        'name': 'Battery Life',
        'weight': 3,
        'formula': "img/battery_life_formula.gif",
        'assumption': "15 hours is the largest reasonable battery life of a laptop"
    }
]

breakdown = {
    'row_headings': ["Price", "Rating", "Weight", "Screen Size", "Power", "Storage", "Battery Life"],
    'col_headings': ["HP Envy 15t Quad Edition", "Dell Inspiron i15RV-1435BLK", "Toshiba Satellite C55-A5245", "MacBook Pro 13\" with Retina", "Lenovo IdeaPad U430", "ASUS ROG 6750JM-DS71", "MacBook Air 13\""],
    'rows': [
        [19.5, 20.5, 8.8, 9.2, 11.2, 6.2, 1.9],
        [24.3, 20.0, 10.1, 9.2, 3.0, 3.8, 0.8],
        [23.7, 20.5, 9.2, 9.2, 3.8, 3.8, 0.8],
        [9.0, 23.5, 13.1, 7.8, 7.9, 3.8, 1.8],
        [19.5, 19.0, 11.6, 8.2, 3.0, 3.8, 1.1],
        [10.5, 21.5, 0.2, 10.2, 16.8, 6.2, 0.7],
        [15.8, 20.5, 14.1, 6.5, 2.3, 3.1, 2.4],
    ]
}

proscons = [
    {
        'name':'HP Envy 15t Quad Edition',
        'url': 'http://ssl-product-images.www8-hp.com/digmedialib/prodimg/lowres/c03698047.png',
        'pro': '15.6 inch screen\nSolid power\nFour Beats audio speakers ',
        'con': 'Heavy\nNo SSD'
    },
    {
        'name':'Dell Inspiron i15RV-1435BLK',
        'url': 'http://ecx.images-amazon.com/images/I/71qmqgZmp7L._SL1500_.jpg',
        'pro': 'Inexpensive\n15.6 Inch Screen',
        'con': 'Poor battery life\nNot very powerful\nNo SSD'
    },
    {
        'name':'Toshiba Satellite C55-A5245',
        'url': 'https://www.laptopninja.org/wp-content/uploads/2014/03/Toshiba-Satellite-C55-A5245.jpg',
        'pro': 'Inexpensive\n15.6 Inch Screen',
        'con': 'Fairly heavy\nPoor battery life\nNo SSD'
    },
    {
        'name':'MacBook Pro 13" with Retina Display',
        'url': 'http://cdn0.sbnation.com/products/large/7406/retina13.jpg?1382468345',
        'pro': 'Retina display\nPowerful\nThin & light\nHas SSD',
        'con': 'Expensive\nSmall Screen'
    },
    {
        'name':'Lenovo IdeaPad U430',
        'url': 'http://media.engadget.com/img/products/488/ah7w/ah7w-800.jpg',
        'pro': 'Powerful\nTouch screen',
        'con': 'No SSD'
    },
    {
        'name':'ASUS ROG 6750JM-DS71',
        'url': 'http://ecx.images-amazon.com/images/I/41eUTqGvDpL._SL160_SL150_.jpg',
        'pro': 'Very powerful\n1 TB hard drive\nGaming',
        'con': 'Extremely heavy\nVery poor battery life\nNo SSD'
    },
    {
        'name':'MacBook Air 13"',
        'url': 'http://images.apple.com/macbook-air/images/techspecs_headline_13inch.jpg',
        'pro': 'Weight\nSuper thin\nHas SSD',
        'con': 'Expensive\nScreen Size'
    },
]