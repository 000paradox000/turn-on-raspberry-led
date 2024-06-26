document.getElementById('toggleButton').addEventListener('click', function(event) {
    event.preventDefault();
    const stateInput = document.getElementById('state');
    const currentState = stateInput.value === 'true';
    const newState = !currentState;
    stateInput.value = newState;
    event.target.innerText = newState ? 'ON' : 'OFF';
    event.target.className = newState ? 'on' : 'off';

    fetch('/state', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ state: newState })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
