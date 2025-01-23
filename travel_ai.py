import pandas as pd
from PIL import Image

# =====================
# Recommendation Engine with Indian Destinations
# =====================
data = {
    "Destination": [
        "Manali", "Goa", "Jaipur", "Leh-Ladakh", "Kerala",
        "Varanasi", "Rishikesh", "Darjeeling", "Mysore", "Agra"
    ],
    "Category": [
        "Hill Station", "Beach", "Cultural", "Adventure", "Backwaters",
        "Spiritual", "Adventure", "Hill Station", "Cultural", "Historical"
    ],
    "Best Time to Visit": [
        "Summer", "Winter", "Winter", "Summer", "Winter",
        "Autumn", "Spring", "Summer", "Winter", "Autumn"
    ],
}

# Convert to DataFrame
df = pd.DataFrame(data)

def recommend_destinations(preference):
    """Recommend destinations based on user preference."""
    recommendations = df[df['Category'].str.contains(preference, case=False)]
    if recommendations.empty:
        return "No matching destinations found. Try a different preference!"
    return recommendations.to_string(index=False)

# =====================
# Simple Chatbot
# =====================
def chatbot():
    """Simple chatbot for travel queries."""
    responses = {
        "hello": "Hi! How can I assist you with your travel plans?",
        "recommend": "I can recommend destinations based on your preferences! Type 'recommend [preference]' (e.g., 'recommend beach').",
        "bye": "Goodbye! Have a great trip!",
    }
    
    print("Chatbot is ready! Type your message or 'exit' to end the chat.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        elif user_input.startswith("recommend"):
            _, preference = user_input.split(maxsplit=1)
            print("Recommended Destinations:")
            print(recommend_destinations(preference))
        else:
            print(responses.get(user_input, "Sorry, I didn't understand that. Try asking something else!"))

# =====================
# Basic Image Processing
# =====================
def display_image(image_path):
    """Display an image."""
    try:
        img = Image.open(image_path)
        img.show()
        print(f"Image '{image_path}' displayed successfully!")
    except Exception as e:
        print(f"Error displaying image: {e}")

# =====================
# Main Application Logic
# =====================
if __name__ == "__main__":
    print("Welcome to the Indian Travel AI System!")
    print("Choose a feature:")
    print("1. Travel Recommendation Engine")
    print("2. Image Display")
    print("3. Simple Chatbot")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        preference = input("Enter your travel preference (e.g., Hill Station, Beach, Cultural): ")
        print("Recommended Destinations:")
        print(recommend_destinations(preference))

    elif choice == "2":
        image_path = input("Enter the path to your image: ")
        display_image(image_path)

    elif choice == "3":
        chatbot()

    else:
        print("Invalid choice! Please restart the program.")
