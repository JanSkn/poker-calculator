var communityCardsContainer = document.getElementById("community-cards");
var handCardsContainer = document.getElementById("hand-cards");
var cardList = document.getElementById("card-list");

var communityCardCount = 0;
var handCardCount = 0;

var communityCardsArray = [];
var handCardsArray = [];

cardList.addEventListener("dragstart", function (event) {
    event.dataTransfer.setData("text/plain", event.target.innerHTML);
});

communityCardsContainer.addEventListener("dragover", function (event) {
    event.preventDefault();
});

communityCardsContainer.addEventListener("drop", function (event) {
    event.preventDefault();
    if (communityCardCount < 5) {
        var card = event.dataTransfer.getData("text/plain");
        var cardElement = document.createElement("div");
        cardElement.className = "card";
        cardElement.innerHTML = card;
        cardElement.addEventListener("click", function () {
            communityCardsContainer.removeChild(cardElement);
            communityCardCount--;
            enableCard(cardElement.innerHTML);
            removeFromCommunityArray(cardElement.innerHTML); // Remove from array
        });

        // Prüfen, ob die Karte bereits vorhanden ist
        var existingCards = Array.from(communityCardsContainer.getElementsByClassName("card"));
        var isCardExisting = existingCards.some(function (existingCard) {
            return existingCard.innerHTML === cardElement.innerHTML;
        });

        if (!isCardExisting) {
            communityCardsContainer.appendChild(cardElement);
            communityCardCount++;
            disableCard(cardElement.innerHTML);
            addToCommunityArray(cardElement.innerHTML); // Add to array
        }
    }
});

handCardsContainer.addEventListener("dragover", function (event) {
    event.preventDefault();
});

handCardsContainer.addEventListener("drop", function (event) {
    event.preventDefault();
    if (handCardCount < 2) {
        var card = event.dataTransfer.getData("text/plain");
        var cardElement = document.createElement("div");
        cardElement.className = "card";
        cardElement.innerHTML = card;
        cardElement.addEventListener("click", function () {
            handCardsContainer.removeChild(cardElement);
            handCardCount--;
            enableCard(cardElement.innerHTML);
            removeFromHandArray(cardElement.innerHTML); // Remove from array
        });

        // Prüfen, ob die Karte bereits vorhanden ist
        var existingCards = Array.from(handCardsContainer.getElementsByClassName("card"));
        var isCardExisting = existingCards.some(function (existingCard) {
            return existingCard.innerHTML === cardElement.innerHTML;
        });

        if (!isCardExisting) {
            handCardsContainer.appendChild(cardElement);
            handCardCount++;
            disableCard(cardElement.innerHTML);
            addToHandArray(cardElement.innerHTML); // Add to array
        }
    }
});

function disableCard(card) {
    var cards = Array.from(cardList.getElementsByClassName("card"));
    cards.forEach(function (cardElement) {
        if (cardElement.innerHTML === card) {
            cardElement.classList.add("disabled");
            cardElement.removeAttribute("draggable");
        }
    });
}

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

// Add card to the community array
function addToCommunityArray(card) {
    card = convertColour(card);
    if(!communityCardsArray.some(arr => arr[0] === card[0] && arr[1] === card[1])) {
        communityCardsArray.push(card);
        communityCardsAPI();
    }
}

// Remove card from the community array
function removeFromCommunityArray(card) {
    card = convertColour(card);
    communityCardsArray = communityCardsArray.filter(arr => !arraysEqual(arr, card));
    communityCardsAPI();
}

// Add card to the hand array
function addToHandArray(card) {
    card = convertColour(card);
    if(!handCardsArray.some(arr => arr[0] === card[0] && arr[1] === card[1])) {
        handCardsArray.push(card);
        handCardsAPI();
    }
    /*if (handCardsArray.indexOf(card) === -1) {
        card = convertColour(card);
        handCardsArray.push(card);
        handCardsAPI();
    }*/
}


// Remove card from the hand array
function removeFromHandArray(card) {
    card = convertColour(card);
    handCardsArray = handCardsArray.filter(arr => !arraysEqual(arr, card));
    handCardsAPI();

    
    /*var index = handCardsArray.indexOf(card);
    if (index !== -1) {
        handCardsArray.splice(index, 1);
        handCardsAPI();
    }*/
}

function convertColour(card) {
    // Index for symbols is 2 because of the Blank Character
    switch(card[0]) {
        case "\u2665": // Heart
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

function formatDictionary(result) {
    const cleanedResult = result.replace(/'/g, '"');
    const parsedResult = JSON.parse(cleanedResult);
    const lastKey = "Highest Card"
    var string = ""
    for (const key in parsedResult) {
        string += `${key}: ${parsedResult[key]}`;
        if(key != lastKey) string += ', ';
    }
    return string;
  }

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

    const result = await response.text();
    formatDictionary(result);
    console.log(result);
    document.getElementById("result").innerHTML = formatDictionary(result);

}

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

    const result = await response.text();
    console.log(result);
    document.getElementById("result").innerHTML = formatDictionary(result);
}