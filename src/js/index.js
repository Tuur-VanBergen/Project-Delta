let loginButton = document.getElementById("login");

const login = (username) => {
    // build request body
    const body = { "username": username };
    // URL to send data to
    const url = "https://project-delta-backend.vercel.app/login";
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
            if (data.status === "user created") {
                window.location.replace('https://p-delta.netlify.app/room?username=' + username);
            } else {
                let error = document.getElementById("error");
                error.style.opacity = "100%";
            }
        })
        .catch((error) => console.log(error));
}
loginButton.addEventListener("click", () => {
    const username = document.getElementById("username").value;
    login(username);
});