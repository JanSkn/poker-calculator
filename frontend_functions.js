
var communityCardsContainer = document.getElementById("community-cards");
var handCardsContainer = document.getElementById("hand-cards");
var cardList = document.getElementById("card-list");

var communityCardCount = 0;
var handCardCount = 0;

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