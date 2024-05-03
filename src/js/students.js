const sendButton = document.getElementById("questionSend");
const urlParams = new URLSearchParams(window.location.search);
const username= urlParams.get('username');
const room_name = urlParams.get('room_name');

const sendMessage = () => {
    const message = document.getElementById('question');
    const body = {"username": username, "room_name": room_name, "message": message.value};
    const url = "https://project-delta-backend.vercel.app/send_message";
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
            if (data.status === "message sent") {
                message.value = "";
            }
        })
        .catch((error) => console.log(error));
}


sendButton.addEventListener("click", function () {
    const message = document.getElementById('question');
    if (message.value !== "") {
        sendMessage()
    }
})