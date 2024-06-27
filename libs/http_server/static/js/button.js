function get_form() {
    return document.getElementById("led-form");
}

function get_state_input() {
    return document.getElementById("state");
}

function get_current_state() {
    const state_input = get_state_input();
    const value = state_input.value;

    return value === "True";
}

function get_button() {
    return document.getElementById("led-button");
}

function change_label() {
    const current_state = get_current_state();
    get_button().innerText = current_state ? "OFF" : "ON";
    get_button().className = current_state ? "huge-button-off" : "huge-button-on";
}

function change_state(value) {
    get_state_input().value = value;
    change_label();
}

get_button().addEventListener("click", function(event) {
    event.preventDefault();

    const change_state_url = "/state/";
    const current_state = get_current_state();
    const new_state = !current_state;
    const headers = {
        "Content-Type": "application/json"
    };
    const body = JSON.stringify({
        state: new_state
    });

    fetch(change_state_url, {
        method: "POST",
        headers: headers,
        body: body
    })
    .then(response => response.json())
    .then(data => {
        change_state(data.state);
    })
    .catch((error) => {
        console.error("There was an error changing the state with button:", error);
    });
});
