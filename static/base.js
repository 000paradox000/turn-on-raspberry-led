document.getElementById('toggleButton').addEventListener('click', function(event) {
    event.preventDefault();
    const stateInput = document.getElementById('state');
    const currentState = stateInput.value === 'true';
    stateInput.value = !currentState;
    event.target.innerText = currentState ? 'OFF' : 'ON';
    event.target.className = currentState ? 'off' : 'on';
    event.target.closest('form').submit();
});
