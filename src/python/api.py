from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from combinations import update_cards

hand_cards = []
community_cards = []

app = FastAPI()

# Cross Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/update_hand_cards")
async def update_hand_cards(cards: list):
    global hand_cards
    hand_cards = cards
    result = update_cards(hand_cards, community_cards)
    return result

@app.post("/update_community_cards")
async def update_community_cards(cards: list):
    global community_cards 
    community_cards = cards
    result = update_cards(hand_cards, community_cards)
    return result

