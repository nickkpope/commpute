criteria = [
    {
        'name': 'Price',
        'inc': "Two thousand dollars is a lot of Ramen.",
        'just': "A high price tag will be a deal breaker no matter what."
    },
    {
        'name': 'User Rating',
        'inc': "User ratings indicate reliability and general satisfaction of previous customers.",
        'just': "This is the only way to determine quality without testing each laptop."
    },
    {
        'name': 'Weight',
        'inc': "The last thing you want is to carry a dumbbell around campus.",
        'just': "The cold, hard truth is you will spend more time carrying your laptop than using it."
    },
    {
        'name': 'Screen Size',
        'inc': "You can Facebook and program at the same time!",
        'just': "Being able to see multiple objects makes you far more effective."
    },
    {
        'name': 'Power',
        'inc': "Some of your programs are computationally intensive with high memory usage.",
        'just': "It is nice, but for the most part it doesn't make a difference in your life."

    },
    {
        'name': 'Storage',
        'inc': "In some programs you will produce lots of data and waiting for it to save is boring. ",
        'just': "Load and save time is relatively insignificant."
    },
    {
        'name': 'Battery Life',
        'inc': "A laptop is useless if you can't use it on the go. But there are plenty of outlets on campus.",
        'just': "The only time an outlet might not be available is during a lecture."
    }
]


ranking = [
    {
        'name' : "HP Envy 15t Quad Edition",
        'rank': 71.6
    },
    {
        'name' : "Dell Inspiron i15RV-1435BLK",
        'rank': 69.6
    },
    {
        'name' : "Toshiba Satellite C55-A5245",
        'rank': 69.1
    },
    {
        'name' : "Lenovo IdeaPad U430",
        'rank': 64.7
    },
    {
        'name' : "MacBook Air 13\"",
        'rank': 63.5
    },
    {
        'name' : "MacBook Pro 13\" with Retina Display",
        'rank': 62.9
    },
    {
        'name' : "ASUS ROG 6750JM-DS71",
        'rank': 57.7
    }
]

algorithm = [
    {
        'name': 'Price',
        'weight': 30,
        'formula': "img/price_formula.gif",
        'assumption': "$2000 is likely the most a student will be willing to pay for a laptop."
    },
    {
        'name': 'User Rating',
        'weight': 25,
        'formula': "img/user_rating_formula.gif",
        'assumption': "User Ratings are from 1 to 5."
    },
    {
        'name': 'Weight',
        'weight': 20,
        'formula': "img/weight_formula.gif",
        'assumption': "10 pounds is the most a laptop should weigh to be reasonable for a student."
    },
    {
        'name': 'Screen Size',
        'weight': 10,
        'formula': "img/screen_size_formula.gif",
        'assumption': "The largest reasonable laptop screen size is 17 inches."
    },
    {
        'name': 'Power',
        'weight':7,
        'formula': "img/power_formula.gif",
        'assumption': "Quad core, 3 GHz, and 8Gb of RAM are reasonable limits for a student."

    },
    {
        'name': 'Storage',
        'weight': 5,
        'formula': "img/storage_formula.gif",
        'assumption': "An SSD is roughly equivalent to a  10,000 rpm optical disk and 512 Gb is a reasonable upper bound on hard drive space."
    },
    {
        'name': 'Battery Life',
        'weight': 3,
        'formula': "img/battery_life_formula.gif",
        'assumption': "15 hours is the largest reasonable battery life of a laptop."
    }
]

breakdown = {
    'row_headings': ["Price", "User Rating", "Weight", "Screen Size", "Power", "Storage", "Battery Life"],
    'col_headings': ["HP Envy 15t Quad", "Dell Inspiron i15RV", "Toshiba Satellite C55", "Lenovo IdeaPad U430", "MacBook Air 13\"", "MacBook Pro 13\"", "ASUS ROG 6750JM"],
    'rows': [
        [19.5, 20.5,  8.8,  9.2, 5.6, 6.2, 1.9],
        [24.3, 20.0, 10.1,  9.2, 1.5, 3.8, 0.8],
        [23.7, 20.5,  9.2,  9.2, 1.9, 3.8, 0.8],
        [19.5, 19.0, 11.6,  8.2, 1.5, 3.8, 1.1],
        [15.8, 20.5, 14.1,  6.5, 1.2, 3.1, 2.4],
        [ 9.0, 23.5, 13.1,  7.8, 4.0, 3.8, 1.8],
        [10.5, 21.5,  0.2, 10.2, 8.4, 6.2, 0.7]
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
        'name':'Lenovo IdeaPad U430',
        'url': 'http://media.engadget.com/img/products/488/ah7w/ah7w-800.jpg',
        'pro': 'Powerful\nTouch screen',
        'con': 'No SSD'
    },
    {
        'name':'MacBook Air 13"',
        'url': 'http://images.apple.com/macbook-air/images/techspecs_headline_13inch.jpg',
        'pro': 'Weight\nSuper thin\nHas SSD',
        'con': 'Expensive\nScreen Size'
    },
    {
        'name':'MacBook Pro 13" with Retina Display',
        'url': 'http://cdn0.sbnation.com/products/large/7406/retina13.jpg?1382468345',
        'pro': 'Retina display\nPowerful\nThin & light\nHas SSD',
        'con': 'Expensive\nSmall Screen'
    },
    {
        'name':'ASUS ROG 6750JM-DS71',
        'url': 'http://ecx.images-amazon.com/images/I/41eUTqGvDpL._SL160_SL150_.jpg',
        'pro': 'Very powerful\n1 TB hard drive\nGaming',
        'con': 'Extremely heavy\nVery poor battery life\nNo SSD'
    }
]

specs = [
#     Price Rating Weight  ScreenSize           Power       RAM    Hard Drive            BL
    ["$702", 4.1, "5.6 lbs", "15.6\"", "4 cores 2.4 clock with 8Gb of RAM", "5400 rpm 11000 Gb", "9.5 hrs"],
    ["$379", 4.0, "4.9 lbs", "15.6\"", "2 cores 1.8 clock with 4Gb of RAM", "5400 rpm 500 Gb", "4 hrs"],
    ["$419", 4.1, "5.4 lbs", "15.6\"", "2 cores 2.3 clock with 4Gb of RAM", "5400 rpm 500 Gb", "4 hrs"],
    ["$699", 3.8, "4.2 lbs", "14.0\"", "2 cores 1.8 clock with 4Gb of RAM", "5400 rpm 500 Gb", "5.5 hrs"],
    ["$949", 4.1, "2.9 lbs", "11.0\"", "2 cores 1.4 clock with 4Gb of RAM", "10000 rpm 128 Gb", "12 hrs"],
    ["$1399", 4.7, "3.4 lbs", "13.3\"", "2 cores 2.4 clock with 8Gb of RAM", "10000 rpm 256 Gb", "9 hrs"],
    ["$1299", 4.3, "9.9 lbs", "17.3\"", "4 cores 2.4 clock with 12Gb of RAM", "5400 rpm 1000 Gb", "3.5 hrs"]
]

