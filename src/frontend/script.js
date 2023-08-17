// Get references to HTML elements
var communityCardsContainer = document.getElementById("community-cards");
var handCardsContainer = document.getElementById("hand-cards");
var cardList = document.getElementById("card-list");

// Initialize card counts for community and hand
var communityCardCount = 0;
var handCardCount = 0;

// Arrays to store community and hand cards
var communityCardsArray = [];
var handCardsArray = [];

// Set up dragstart event listener for cards
cardList.addEventListener("dragstart", function (event) {
    // Set data for drag-and-drop
    event.dataTransfer.setData("text/plain", event.target.innerHTML);
    event.dataTransfer.setData("card-color", event.target.classList);
});

// Set up dragover and drop event listeners for community cards
communityCardsContainer.addEventListener("dragover", function (event) {
    event.preventDefault();
});

communityCardsContainer.addEventListener("drop", function (event) {
    event.preventDefault();
    // Check if there's space for a new card
    if (communityCardCount < 5) {
        var card = event.dataTransfer.getData("text/plain");
        var cardColor = event.dataTransfer.getData("card-color");
        
        // Create a new card element
        var cardElement = document.createElement("div");
        cardElement.className = "card";
        cardElement.classList = cardColor;
        cardElement.innerHTML = card;
        
        // Set up click event listener for removing the card
        cardElement.addEventListener("click", function () {
            communityCardsContainer.removeChild(cardElement);
            communityCardCount--;
            enableCard(cardElement.innerHTML);
            removeFromCommunityArray(cardElement.innerHTML); 
        });

        // Check if the card already exists in the community
        var existingCards = Array.from(communityCardsContainer.getElementsByClassName("card"));
        var isCardExisting = existingCards.some(function (existingCard) {
            return existingCard.innerHTML === cardElement.innerHTML;
        });

        // Add the card to the community if it's not already there
        if (!isCardExisting) {
            communityCardsContainer.appendChild(cardElement);
            communityCardCount++;
            disableCard(cardElement.innerHTML);
            addToCommunityArray(cardElement.innerHTML); 
        }
    }
});

// Set up dragover and drop event listeners for hand cards
handCardsContainer.addEventListener("dragover", function (event) {
    event.preventDefault();
});

handCardsContainer.addEventListener("drop", function (event) {
    event.preventDefault();
    // Check if there's space for a new card
    if (handCardCount < 2) {
        var card = event.dataTransfer.getData("text/plain");
        var cardColor = event.dataTransfer.getData("card-color");
        
        // Create a new card element
        var cardElement = document.createElement("div");
        cardElement.className = "card";
        cardElement.classList = cardColor;
        cardElement.innerHTML = card;
        
        // Set up click event listener for removing the card
        cardElement.addEventListener("click", function () {
            handCardsContainer.removeChild(cardElement);
            handCardCount--;
            enableCard(cardElement.innerHTML);
            removeFromHandArray(cardElement.innerHTML); 
        });

        // Check if the card already exists in the hand
        var existingCards = Array.from(handCardsContainer.getElementsByClassName("card"));
        var isCardExisting = existingCards.some(function (existingCard) {
            return existingCard.innerHTML === cardElement.innerHTML;
        });

        // Add the card to the hand if it's not already there
        if (!isCardExisting) {
            handCardsContainer.appendChild(cardElement);
            handCardCount++;
            disableCard(cardElement.innerHTML);
            addToHandArray(cardElement.innerHTML); 
        }
    }
});

// Function to disable a card by adding "disabled" class
function disableCard(card) {
    var cards = Array.from(cardList.getElementsByClassName("card"));
    cards.forEach(function (cardElement) {
        if (cardElement.innerHTML === card) {
            cardElement.classList.add("disabled");
            cardElement.removeAttribute("draggable");
        }
    });
}

// Function to enable a card by removing "disabled" class
function enableCard(card) {
    var cards = Array.from(cardList.getElementsByClassName("card"));
    cards.forEach(function (cardElement) {
        if (cardElement.innerHTML === card) {
            cardElement.classList.remove("disabled");
            cardElement.setAttribute("draggable", "true");
        }
    });
}

function arraysEqual(arr1, arr2) {
    return arr1[0] === arr2[0] && arr1[1] === arr2[1];
}

function addToCommunityArray(card) {
    card = convertColour(card);
    if(!communityCardsArray.some(arr => arr[0] === card[0] && arr[1] === card[1])) {
        communityCardsArray.push(card);
        communityCardsAPI();
    }
}

function removeFromCommunityArray(card) {
    card = convertColour(card);
    communityCardsArray = communityCardsArray.filter(arr => !arraysEqual(arr, card));
    communityCardsAPI();
}

function addToHandArray(card) {
    card = convertColour(card);
    if(!handCardsArray.some(arr => arr[0] === card[0] && arr[1] === card[1])) {
        handCardsArray.push(card);
        handCardsAPI();
    }
}

function removeFromHandArray(card) {
    card = convertColour(card);
    handCardsArray = handCardsArray.filter(arr => !arraysEqual(arr, card));
    handCardsAPI();
}

function convertColour(card) {
    // Index for symbols is 2 because of the Blank Character
    switch(card[0]) {
        case "\u2665": // Hearts
            card = ["Hearts", card[2]]; 
            break;
        case "\u2666": // Diamonds
            card = ["Diamonds", card[2]];
            break;
        case "\u2663": // Clubs
            card = ["Clubs", card[2]];
            break;
        case "\u2660": // Spades
            card = ["Spades", card[2]];
            break;    
    }

    if(card[1] === "1") card[1] = "10"; // Special Case: 10 has 2 indices

    return card;
}

// Function to update hand cards using API
async function handCardsAPI() {
    const data = handCardsArray;

    const response = await fetch("http://localhost:8000/update_hand_cards", {                           
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })           
            .catch(error => {
                console.error("Error: ", error);
            });

    if(response.ok) {
        const result = JSON.parse(await response.text());
        console.log(result);
        for(const key of Object.keys(result)) {
            document.getElementById(key).innerHTML = result[key];
        }
    }
}

// Function to update community cards using API
async function communityCardsAPI() {
    const data = communityCardsArray;

    const response = await fetch("http://localhost:8000/update_community_cards", {                          
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .catch(error => {
                console.error("Error: ", error);
            });

    if(response.ok) {
        const result = JSON.parse(await response.text());
        console.log(result);
        for(const key of Object.keys(result)) {
            document.getElementById(key).innerHTML = result[key];
        }
    }
}
