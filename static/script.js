function submitText() {
    const inputText = document.getElementById('textbox').value;

    // Display the "Please wait..." message
    document.getElementById('wait-message').style.display = 'block';

    // Clear the existing content in the result section
    document.getElementById('result').textContent = '';

    fetch('/query', {
        method: 'POST',
        body: new URLSearchParams({ input_text: inputText }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Replace the "Please wait..." message with the actual response
        document.getElementById('wait-message').style.display = 'none';
        document.getElementById('result').textContent = data;
    });
}
