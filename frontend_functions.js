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

// Add card to the community array
function addToCommunityArray(card) {
    if (communityCardsArray.indexOf(card) === -1) {
        communityCardsArray.push(card);
        communityCardsAPI();
    }
}

// Remove card from the community array
function removeFromCommunityArray(card) {
    var index = communityCardsArray.indexOf(card);
    if (index !== -1) {
        communityCardsArray.splice(index, 1);
        communityCardsAPI();
    }
}

// Add card to the hand array
function addToHandArray(card) {
    if (handCardsArray.indexOf(card) === -1) {
        handCardsArray.push(card);
        handCardsAPI();
    }
}

// Remove card from the hand array
function removeFromHandArray(card) {
    var index = handCardsArray.indexOf(card);
    if (index !== -1) {
        handCardsArray.splice(index, 1);
        handCardsAPI();
    }
}

function handCardsAPI() {
    const data = handCardsArray;

    fetch("http://localhost:8000/update_hand_cards", {                           // HTTP-Anfrage an URL
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())              // warten auf Response
            .catch(error => {
                console.error("Error:", error);
            });
}

function communityCardsAPI() {
    const data = communityCardsArray;

    fetch("http://localhost:8000/update_community_cards", {                           // HTTP-Anfrage an URL
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())              // warten auf Response
            .catch(error => {
                console.error("Error:", error);
            });
}