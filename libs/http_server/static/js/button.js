// function get_state_input() {
//     return document.getElementById("state");
// }
//
// function get_button() {
//     return document.getElementById("led-button");
// }
//
// function get_current_state() {
//     return get_state_input().value === "true";
// }
//
// function change_state(value) {
//     get_state_input().value = value;
// }
//
// function change_label() {
//     get_button().innerText = newState ? "OFF" : "ON";
//     get_button().className = newState ? "off" : "on";
//
// }
//
// document.getElementById("toggleButton").addEventListener("click", function(event) {
//     event.preventDefault();
//
//     const state_input = document.getElementById("state");
//     const current_state = state_input.value === "true";
//     const new_state = !current_state;
//     stateInput.value = newState;
//     event.target.innerText = newState ? "OFF" : "ON";
//     event.target.className = newState ? "off" : "on";
//
//     fetch("/state/", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json"
//         },
//         body: JSON.stringify({
//             state: newState
//         })
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log("Success:", data);
//     })
//     .catch((error) => {
//         console.error("Error:", error);
//     });
// });
