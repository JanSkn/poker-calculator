from fastapi import FastAPI,  Request
from fastapi.responses import JSONResponse
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
    print(pc.update_cards(hand_cards, community_cards))
    return {'message': f'Hand cards updated successfully: {hand_cards}'}

@app.post("/update_community_cards")
async def update_community_cards(cards: list):
    global community_cards 
    community_cards = cards
    result = pc.update_cards(hand_cards, community_cards)
    print(result)
    return {'message': f'Community cards updated successfully: {community_cards}'}

