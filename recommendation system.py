import random

# Sample book data (replace with your actual book data)
books_data = {
    'book1': 'gone with wind',
    'book2': 'To Kill a Mockingbird',
    'book3': 'paper towns',
    'book4': 'Pride and Prejudice',
    'book5': 'number the stars'
    # Add more books as needed
}

# Function to recommend books randomly
def recommend_books(num_recommendations=3):
    recommended_books = random.sample(list(books_data.values()), num_recommendations)
    return recommended_books

# Example usage
num_recommendations = 5
recommended_books = recommend_books(num_recommendations)
print("Randomly recommended books:")
for i, book in enumerate(recommended_books, start=1):
    print(i, ".", book)
