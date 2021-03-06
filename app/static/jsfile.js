// function needed by google maps api
function initMap() {
}

// number of map
let mapID = 0;

let message;

let address;

let welcome = "Bonjour mon ptit! Ta maman m'a dit que ton sens de l'orientation était proche du zéro absolu! Si tu as" +
    " besoin de te rendre quelque part, demande-moi, je sais tout! Enfin presque... T'aurais pas vu mon dentier? ";

receivedMessage({'message' : welcome});

// Get current date and format it
function getDate() {
    const monthNames =  [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
        "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ];
    let date = new Date();
    let hh = date.getHours();
    let mm = date.getMinutes();
    let dd = date.getDate();
    let MM = monthNames[date.getMonth()];

    hh = hh.toString();
    mm = mm.toString();

    // If hour of minutes has only one character, add a "0" before.
    if (hh.length !== 2) {
        hh = "0" + hh
    }

    if (mm.length !== 2) {
        mm = "0" + mm
    }

    return dd + " " + MM + " | " + hh + ":" + mm
}

// Message sent by user
function outgoingMessage() {
    let inputText = document.getElementById("inputText");
    message = inputText.value;

    if (!message) {
        return
    }

    // Empty input value
    inputText.value = null;

    let outgoing = document.createElement("div");
    outgoing.className = "outgoing-chats";

    let outgoingMsg = document.createElement("div");
    outgoingMsg.className = "outgoing-chats-msg";

    let answer = document.createElement("p");
    answer.textContent = message;

    let datetime = document.createElement("span");
    datetime.className = "time";
    datetime.textContent = getDate();

    let outgoingChatImg = document.createElement("div");
    outgoingChatImg.className = "outgoing-chats-img";

    let outgoingProfile = document.createElement("img");
    outgoingProfile.className = "profile-img";
    outgoingProfile.src = "../static/user.png";
    outgoingProfile.alt = "user";

    let msgPage = document.getElementById("chat-zone");
    outgoingMsg.appendChild(answer);
    outgoingMsg.appendChild(datetime);
    outgoingChatImg.appendChild(outgoingProfile);
    outgoing.appendChild(outgoingMsg);
    outgoing.appendChild(outgoingChatImg);
    msgPage.appendChild(outgoing);

    // Scroll to message
    outgoing.scrollIntoView()
}


// Message sent by server
function receivedMessage(dict_answer) {
    let received = document.createElement("div");
    received.className = "received-chats";

    let receivedMsg = document.createElement("div");
    receivedMsg.className = "received-msg";

    let receivedInbox = document.createElement("div");
    receivedInbox.className = "received-msg-inbox";

    let answer = document.createElement("p");
    answer.textContent = dict_answer['message'];
    answer.className = "received-answer";

    let datetime = document.createElement("span");
    datetime.className = "time";
    datetime.textContent = getDate();

    let receivedChatImg = document.createElement("div");
    receivedChatImg.className = "received-chats-img";

    let receivedProfile = document.createElement("img");
    receivedProfile.className = "profile-img";
    receivedProfile.src = "../static/Grandpa.jpeg";
    receivedProfile.alt = "grandpy";

    let msgPage = document.getElementById("chat-zone");

    // Create a map if location is found
    if (('location' in dict_answer)&&('lat' in dict_answer['location'])&&(dict_answer['location']['lat']))  {
        let map = document.createElement("div");
        map.className = "map";
        map.id = "map" + mapID;
        msgPage.appendChild(map);

        let c_map = new google.maps.Map(document.getElementById('map' + mapID), {
            mapDiv: '100',
            center: {lat: dict_answer['location']['lat'], lng: dict_answer['location']['lng']},
            zoom: 15
        });

        let marker = new google.maps.Marker({position: {lat: dict_answer['location']['lat'], lng: dict_answer['location']['lng']},
        map: c_map});

        mapID += 1;
    }
    receivedInbox.appendChild(answer);
    receivedInbox.appendChild(datetime);
    receivedMsg.appendChild(receivedInbox);
    receivedChatImg.appendChild(receivedProfile);
    received.appendChild(receivedChatImg);
    received.appendChild(receivedMsg);
    msgPage.appendChild(received);

    // Scroll only to first message sent by server
    if ('scroll' in dict_answer) {
        received.scrollIntoView()
    }
    else if (answer.textContent.startsWith('Quoi')) {
        msgPage.scrollTo(0, msgPage.scrollHeight);
    }
}

let clickQuestion = document.getElementById("outgoing-form");

clickQuestion.addEventListener("submit", function (event) {
    fetch("/question", {
        method: "POST",
        body: JSON.stringify(message)
    })
        .then(answer => answer.json())
        .then(answer => {
            let latitude;
            let longitude;
            if (answer.coordonates[0]  !== undefined) {
                latitude = parseFloat(answer.coordonates[0].lat);
                longitude = parseFloat(answer.coordonates[0].lng);
                address = answer.address;
                message = "L'adresse est " + address;
                receivedMessage({'message': message, 'scroll': true})
            }
            message = answer.message;
            receivedMessage({
                'location': {'lat': latitude, 'lng': longitude},
                'message': message
            });
        });

    event.preventDefault();
});
