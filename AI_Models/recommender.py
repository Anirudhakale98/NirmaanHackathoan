import pymongo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import json

# Connect to MongoDB 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]  # Change to your database name
events_collection = db["events"]  # Collection name (table equivalent)
groups_collection = db["groups"]
listings_collection = db["listings"]  
users_collection = db["users"]

# Fetch All Events, Groups,Posts & User and store it as text data
events_data = events_collection.find({}, {
    "_id": 1,  # Keep UID
    "name": 1,
    "description": 1,
    "objectives": 1,
    "rules": 1,
    "prizes": 1,
    "location": 1
})

event_texts = []
event_ids = []  
for event in events_data:
    text = f"{event.get('name', '')} {event.get('description', '')} {event.get('objectives', '')} {event.get('rules', '')} {event.get('prizes', '')} {event.get('location', '')}"
    event_texts.append(text)
    event_ids.append(str(event["_id"]))  


groups_data = groups_collection.find({}, {
    "_id": 1,  # Keep UID
    "name": 1,
    "description": 1,
    "tags": 1
})

group_texts = []
group_ids = [] 
for group in groups_data:
    text = f"{group.get('name', '')} {group.get('description', '')} {' '.join(group.get('tags', []))}"
    group_texts.append(text)
    group_ids.append(str(group["_id"]))  

listings_data = listings_collection.find({}, {
    "_id": 1,  # Keep UID
    "title": 1,
    "description": 1,
    "category": 1,
    "location": 1
})

listing_texts = []
listing_ids = []  
for listing in listings_data:
    text = f"{listing.get('title', '')} {listing.get('description', '')} {listing.get('category', '')} {listing.get('location', '')}"
    listing_texts.append(text)
    listing_ids.append(str(listing["_id"]))  
    
# Fetch the user data
user_input_json = sys.argv[1]
user_data = json.loads(user_input_json) 

user_id = user_data.get("_id")
user_record = users_collection.find_one({"_id": user_id})
user_text = f"{user_record.get('description', '')} {' '.join(user_record.get('interests', []))}"

def recommend(corpus_texts, corpus_ids, top_n=10):
    # Create TF-IDF matrix
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([user_text] + corpus_texts)

    # Train KNN model
    knn = NearestNeighbors(n_neighbors=top_n + 1, metric="cosine")
    knn.fit(tfidf_matrix[1:])  # Exclude user text from training

    # Find nearest neighbors
    distances, indices = knn.kneighbors(tfidf_matrix[0])  # Query user text

    # Return top-N recommended IDs
    return [corpus_ids[i] for i in indices[0]]

recommended_events = recommend(user_id, event_texts, event_ids, top_n=10)
recommended_groups = recommend(user_id, group_texts, group_ids, top_n=10)
recommended_listings = recommend(user_id, listing_texts, listing_ids, top_n=10)

print("Recommended Events:", recommended_events)
print("Recommended Groups:", recommended_groups)
print("Recommended Listings:", recommended_listings)

