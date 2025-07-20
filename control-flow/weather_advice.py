user_input = input("What's the weather like today?")
if "sunny" in user_input.lower():
    print("Wear a t-shirt and sunglasses.")
elif "rainy" in user_input.lower():
    print("Don't forget your umbrella and a raincoat.")
elif "cold" in user_input.lower():
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
