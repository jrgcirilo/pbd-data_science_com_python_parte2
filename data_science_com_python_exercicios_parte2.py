from collections import defaultdict

users = [
    {"id": 0, "name": "Hero", "age": 18, "genre": "Male", "genre interest": "Female" },
    {"id": 1, "name": "Dunn", "age": 19, "genre": "Male", "genre interest": "Female"},
    {"id": 2, "name": "Chi", "age": 20, "genre": "Male", "genre interest": "Female"},
    {"id": 3, "name": "Thor", "age": 21, "genre": "Male", "genre interest": "Female"},
    {"id": 4, "name": "Clive", "age": 22, "genre": "Male", "genre interest": "Female"},
    {"id": 5, "name": "Sue", "age": 18, "genre": "Female", "genre interest": "Male"},
    {"id": 6, "name": "Kate", "age": 19, "genre": "Female", "genre interest": "Male"},
    {"id": 7, "name": "Anna", "age": 20, "genre": "Female", "genre interest": "Male"},
    {"id": 8, "name": "Carolina", "age": 21, "genre": "Female", "genre interest": "Male"},
    {"id": 9, "name": "Daisy", "age": 22, "genre": "Female", "genre interest": "Male"},
]

friendships = [
    (0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6),
    (3, 7), (3, 8), (4, 9), (4, 0), (5, 1), (5, 2),
    (6, 3), (6, 4), (7, 5), (7, 6), (8, 7), (8, 8),
    (9, 9), (9, 0)
]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),(1, "Postgres"), 
    (2, "Python"), (2, "Scikit-Learn"), (2, "Scipy"),(2, "Numpy"), (2, "Statsmodel"), (2, "Pandas"), 
    (3, "R"), (3, "Python"),(3, "Statistics"), (3, "Regression"), (3, "Probability"),
    (4, "Machine Learning"), (4, "Regression"), (4, "Decision Trees"),(4, "Libsvm"), 
    (5, "Python"), (5, "R"),(5, "Java"), (5, "C++"),(5, "Haskell"), (5, "Programming Languages"), 
    (6, "Theory"),(7, "Machine Learning"), (7, "Scikit-Learn"), 
    (7, "Mahout"),(7, "Neural Networks"), (8, "Neural Networks"), (8, "Deep Learning"),(8, "Big Data"), (8, "Artificial Intelligence"), (8, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data"),  ]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends_by_genre (user,genre):
    cont = 0
    for friend in user['friends']:
        if(friend['genre']==genre):
            cont=cont+1
    return cont  

#for user in users:
#	print({user['id']: (number_of_friends_by_genre(user,'Male'), number_of_friends_by_genre(user,'Female')) 
#    })     

user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
def users_with_common_interests(user):
    return set([
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    ])

def users_with_common_genre_interest(identify):
    return set([
        user["id"]
        for user in users
        if user["id"] != identify["id"] and (identify["genre interest"] == user["genre"])
    ])
    
def users_with_common_interests_and_genre_interest(user):
    return set([
        interests_and_genre_interest_user_id
        for interests_and_genre_interest_user_id in users_with_common_genre_interest(user)
        if interests_and_genre_interest_user_id in users_with_common_interests(user)
    ])

print (users_with_common_interests(users[0]))

print (users_with_common_genre_interest(users[0]))

print (users_with_common_interests_and_genre_interest(users[0]))