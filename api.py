from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import poker_calculator as pc

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
    print(hand_cards)
    print(pc.get_cards_from_frontend(hand_cards, community_cards))
    return {'message': f'Hand cards updated successfully: {hand_cards}'}

@app.post("/update_community_cards")
async def update_community_cards(cards: list):
    global community_cards 
    community_cards = cards
    print(community_cards)
    return {'message': f'Community cards updated successfully: {community_cards}'}

@app.post("/test")
async def dummy():
    
    return {'message': 'Test'}
