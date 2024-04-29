let joinButton = document.getElementById("joinButton");
let createButton = document.getElementById("createButton");
const urlParams = new URLSearchParams(window.location.search);
const username = urlParams.get('username')

const createRoom = (username) => {
    // build request body
    const body = { "username": username };
    // URL to send data to
    const url = "https://project-delta-backend.vercel.app/create_room";
    // options for the fetch() methode
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body),
        redirect: "manual"
    };

    fetch(url, options)
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            if (data.status === "room created") {
                console.log(data);
                window.location.replace('https://p-delta.netlify.app/teachers?username=' + username + '&room_name=' + data.room);
            } else {
                let error = document.getElementById("error");
                error.style.opacity = "100%";
            }
        })
        .catch((error) => console.log(error));
}

const joinRoom = (username) => {
    const roomName = document.getElementById('roomCode').value;
    // build request body
    const body = { "username": username , "room_name": roomName};
    console.log(body);
    // URL to send data to
    const url = "https://project-delta-backend.vercel.app/join_room";
    // options for the fetch() methode
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body),
        redirect: "manual"
    };

    fetch(url, options)
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            if (data.status === "room joined") {
                window.location.replace('https://p-delta.netlify.app/students?username=' + username + '&room_name=' + roomName);
            } else {
                let error = document.getElementById("error");
                error.style.opacity = "100%";
            }
        })
        .catch((error) => console.log(error));
}


createButton.addEventListener("click", () => {
    createRoom(username);
});

joinButton.addEventListener("click", () => {
    joinRoom(username);
});