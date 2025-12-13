import csv
import random

categories = ['Electronics', 'Home & Kitchen', 'Fitness', 'Clothing', 'Books']

adjectives = ['Premium', 'High-Performance', 'Eco-Friendly', 'Durable', 'Wireless', 'Ergonomic', 'Vintage', 'Smart']
nouns = ['Headphones', 'Coffee Maker', 'Yoga Mat', 'Running Shoes', 'Desk Lamp', 'Blender', 'Smart Watch', 'Backpack']
features = ['with noise cancellation', 'made from organic materials', 'with 24-hour battery life', 'water-resistant design', 'compatible with iOS and Android']

# Generate 100 fake products
data = []
for i in range(1, 101):
    cat = random.choice(categories)
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    feat = random.choice(features)
    
    title = f"{adj} {noun} - {cat} Essentials"
    description = f"Experience the ultimate {noun.lower()} with our {adj.lower()} design. Featuring {feat}, this product is perfect for daily use. Top rated in {cat}."
    
    data.append([i, title, cat, description])

# Write to CSV
with open('data/products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['product_id', 'title', 'category', 'description'])
    writer.writerows(data)

print(f"Successfully generated {len(data)} products in data/products.csv")
