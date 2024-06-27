function get_text() {
    return document.getElementById("text_input");
}

function change_label() {
    const current_state = get_current_state();
    get_button().innerText = current_state ? "OFF" : "ON";
    get_button().className = current_state ? "huge-button huge-button-off" : "huge-button huge-button-on";
}
//
// function change_state(value) {
//     get_state_input().value = value;
//     change_label();
// }
//
// get_button().addEventListener("click", function(event) {
//     event.preventDefault();
//
//     const change_state_url = "/state/";
//     const current_state = get_current_state();
//     const new_state = !current_state;
//     const headers = {
//         "Content-Type": "application/json"
//     };
//     const body = JSON.stringify({
//         state: new_state
//     });
//
//     fetch(change_state_url, {
//         method: "POST",
//         headers: headers,
//         body: body
//     })
//     .then(response => response.json())
//     .then(data => {
//         change_state(data.state);
//     })
//     .catch((error) => {
//         console.error("There was an error changing the state with button:", error);
//     });
// });
