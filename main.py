import random

def news_generator(subject, action, places_or_thing):
    headline = f"Breaking News: {subject} {action} {places_or_thing}."
    return headline

subjects = [
    "Shahrukh Khan", "Aamir Khan", "Salman Khan",
    "Virat Kohli", "MS Dhoni",
    "Messi", "Ronaldo",
    "A Group of Friends",
    "Honey Singh", "Talha Anjum",
            ]
actions = [
    "is playing cricket",
    "is watching a movie",
    "launches",
    "cancels",
    "dances",
    "eats",
    "wins",
    "scores",
    "sings a song"
]
places_or_things = [
    "at the stadium",
    "in the city",
    "a new album",
    "in a match",
    "a delicious meal",
    "a trophy",
    "at Dubai",
    "In karachi local train",
    "during IPL match"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things) 

    headline = news_generator(subject, action, places_or_thing)

    print("\n" + headline)

    user_input = input("Do you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("Thank you for using the headline generator!")
