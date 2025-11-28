print("=== Movie Ticket Booking System ===\n")


movies = {
    1: ("Mission imposiible", 0),
    2: ("Avengers: Endgame", 13),
    3: ("John Wick", 18),
    4: ("Final destination", 18)
}

# Show movies
print("Available Movies:")
for num, (name, age_req) in movies.items():
    print(f"{num}. {name} (Age {age_req}+)")


choice = int(input("\nEnter movie number: "))

if choice in movies:
    movie_name, min_age = movies[choice]
    print(f"\nYou selected: {movie_name}")
else:
    print("Invalid movie choice.")
    exit()


age = int(input("Enter your age: "))

if age < min_age:
    print(f" You cannot watch this movie.Watch at your own risk. Minimum age: {min_age}")
    exit()
else:
    print("Age verified.")


tickets = int(input("How many tickets do you want? "))
