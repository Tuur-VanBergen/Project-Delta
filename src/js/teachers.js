const urlParams = new URLSearchParams(window.location.search);
const username= urlParams.get('username');
const room_name = urlParams.get('room_name');
const messagebox = document.getElementById('messages');
let messages = [];
document.getElementById('title').innerHTML = "Room code: " + room_name;
function fetchData() {
    const url = "https://project-delta-backend.vercel.app/get_messages?username=" + username + "&room_name=" + room_name;
    const options = {
        method: 'GET'
    };

    fetch(url, options)
        .then(response => response.json())
        .then(data => {
            if (messages.length < data.messages.length) {
                messages = data.messages;
                messagebox.innerHTML = "";
                for (let message of messages) {
                    const sender = document.createElement("p")
                    sender.innerHTML = message.username
                    sender.classList.add("username");
                    const newMessage = document.createElement("p")
                    newMessage.innerHTML = message.message;
                    newMessage.classList.add("message");
                    const newMessageBox = document.createElement("div");
                    newMessageBox.appendChild(sender);
                    newMessageBox.appendChild(newMessage);
                    newMessageBox.classList.add("messageBox");
                    messagebox.appendChild(newMessageBox);
                }
            }
        })
        .catch(error => console.error(error));
}

setInterval(fetchData, 1000);

