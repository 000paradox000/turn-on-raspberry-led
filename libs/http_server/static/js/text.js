function get_text() {
    return document.getElementById("text_input");
}

function get_label() {
    return document.getElementById("text_state_label");
}

function change_label() {
    const current_state = get_current_state();
    get_label().className = current_state ? "text_state_label-on" : "text_state_label-off";
}

function change_state(value) {
    get_state_input().value = value;
    change_label();
}

get_form().addEventListener("submit", function(event) {
    event.preventDefault();

    const change_state_url = "/text-input/";
    const value = get_text().value;
    const headers = {
        "Content-Type": "application/json"
    };
    const body = JSON.stringify({
        value: value
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
