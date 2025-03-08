from fastapi import FastAPI
import random

app = FastAPI(title="Kenyantics", description="A collection of humorous African-themed APIs", version="1.0")

# 1. Mama Mboga Price Forecast API
@app.get("/mama-mboga-price")
def get_mama_mboga_price():
    prices = [
        {"status": "Affordable", "reason": "It’s harvest season, stock up!"},
        {"status": "Expensive", "reason": "Rain season, sukuma is now premium"},
        {"status": "Varies", "reason": "Depends on mama mboga's mood today"}
    ]
    return random.choice(prices)

# 2. African Parent Response API
@app.get("/african-parent-response")
def get_african_parent_response(question: str):
    responses = [
        "Did you finish washing the dishes?", 
        "Money doesn’t grow on trees!", 
        "Ask your father!",
        "Is this house a hotel?"
    ]
    return {"response": random.choice(responses)}

# 3. Traffic Excuse Generator API
@app.get("/traffic-excuse")
def get_traffic_excuse():
    excuses = [
        "Matatu driver decided to take a 'shortcut' through the Serengeti", 
        "Traffic lights stopped working, now we are negotiating", 
        "A boda boda convoy blocked the road!"
    ]
    return {"excuse": random.choice(excuses)}

# 4. African Wedding Contribution API
@app.get("/wedding-contribution")
def get_wedding_contribution(relation: str):
    contributions = {
        "Close Friend": "Ksh 10,000", 
        "Cousin": "Ksh 5,000", 
        "Distant Cousin": "Ksh 2,000", 
        "Workmate": "Ksh 1,000"
    }
    amount = contributions.get(relation, "Ksh 500 (If you attend)")
    return {"relation": relation, "amount": amount}

# 5. Electricity Availability Predictor API
@app.get("/electricity-status")
def get_electricity_status():
    statuses = [
        {"status": "Available", "advice": "Enjoy it while it lasts!"},
        {"status": "Unavailable", "advice": "Charge your phone and boil water now!"},
        {"status": "Intermittent", "advice": "It will be back... or maybe not."}
    ]
    return random.choice(statuses)

# 6. African Superstition Advice API
@app.get("/superstition-advice")
def get_superstition():
    superstitions = [
        {"sign": "Right palm itching", "meaning": "Money is coming!"},
        {"sign": "Left eye twitching", "meaning": "Bad luck incoming, be careful!"},
        {"sign": "Whistling at night", "meaning": "You’re calling spirits!"}
    ]
    return random.choice(superstitions)

# 7. Matatu DJ Song Predictor API
@app.get("/matatu-dj-song")
def get_matatu_song(location: str):
    songs = {
        "Nairobi CBD": "Genge bangers + unexpected reggae remix", 
        "Thika Road": "Arbantone + Afrobeats hype", 
        "Mombasa": "Coastal Taarab + Old School Bongo"
    }
    return {"location": location, "song": songs.get(location, "Something loud and unexpected!")}

# 8. African Auntie Gossip API
@app.get("/auntie-gossip")
def get_auntie_gossip():
    gossip_topics = [
        {"topic": "Your relationship status", "quote": "That one is always on the phone, but where is the wedding?"},
        {"topic": "Your weight", "quote": "You’ve either lost too much or gained too much!"},
        {"topic": "Your job", "quote": "You work online? So, you don’t have a real job?"}
    ]
    return random.choice(gossip_topics)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
