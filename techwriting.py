criteria = [
    {
        'name': 'Price',
        'inc': "The majority of college students are extremely sensitive to spending money, especially when purchasing something worth hundreds of dollars. Because of this, the price of a laptop will strongly influence whether or not a student will purchase it.",
        'just': "The price of a laptop will be the strongest consideration in our evaluation because most students have a tight budget and will compromise in other areas in order to save money."
    },
    {
        'name': 'User Rating',
        'inc': 'One of the most difficult things about a laptop to quantify is its quality: Is it enjoyable to use? How long will it be useful? Is it well-made? How easily will it break? In order to account for these qualitative questions, we will consider the average user rating of each laptop in our evaluation of data.',
        'just': 'For most students, a good recommendation from previous users is worth more than the best marketing claims. Conversely, very rarely can great marketing convince a student to purchase a poorly reviewed laptop. Because students rely so heavily on user reviews when making a purchase, it will be the second standard we use to judge the laptops.'
    },
    {
        'name': 'Weight',
        'inc': 'While as a CS major you might hope that most of the time with your computer is programming, the fact of the matter is most of the time it will be in your backpack. Being in college involves lots of walking, especially getting to school and between classes. The last thing you want is to carry a dumbbell across campus.',
        'just': 'Weight is very important. As previously said most of the time with your computer will involve walking or lifting, rather than programming. Especially when combined with other books it can be quite a burden. When you move off campus you will be very glad that you have a laptop that is light weight. After 10 lbs we assume that you really do not care about weight and so all get a score of 0 beyond this point.'
    },
    {
        'name': 'Screen Size',
        'inc': 'A large screen allows you to look at documents or help pages while having your terminal visible. A small screen leaves you looking at help pages on a screen and hen changing back to programming a few lines on a very small terminal',
        'just': 'By being able to see multiple objects at once on your screen greatly increases your effectiveness. With large screens you can read the instructions while you program.'
    },
    {
        'name': 'Power',
        'inc': 'As a CS major you will write some code that will max out your computer. While there are many things you will learn that will optimize your code, with some methods large numbers of computations and high memory usage is unavoidable.',
        'just': "While power in a laptop is important, very little of your time will involve writing code that will max out your computer. So while on those occasions extra power is nice, for the most part it doesn't make a difference in your major."

    },
    {
        'name': 'Storage',
        'inc': 'We all want to save our work and as the years have progressed file sizes have become larger and larger. You want room to store all of this and you want it done quickly.',
        'just': 'This is more of a nitpick issue. It is nice  not to wait forever load and save but as mentioned this will be very little of the overall time with your computer.'
    },
    {
        'name': 'Battery Life',
        'inc': 'Battery life is what differentiates a laptop from a desktop. On nice days you can be with your computer outside instead of trapped indoors. While the other criteria are more important this is certainly one to consider as well.',
        'just': 'While battery life is a necessity in a phone it is less important in a laptop. You can always plug your computer into the wall during long programming sessions. The only time an outlet might not be available is during lecture which is at most 3 hours straight.'
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
