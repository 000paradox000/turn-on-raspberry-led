function get_form() {
    return document.getElementById("led-form");
}

function get_state_input() {
    return document.getElementById("state");
}

function get_current_state() {
    const state_input = get_state_input();
    const value = state_input.value;

    return value === "true";
}

document.addEventListener("DOMContentLoaded", function() {
});
