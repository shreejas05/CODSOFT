// Function to append values to the display
function appendToDisplay(value) {
    const display = document.getElementById("display");
    if (display.innerText === '0') {
        display.innerText = value;
    } else {
        display.innerText += value;
    }
}

// Function to clear the display
function clearDisplay() {
    document.getElementById("display").innerText = '0';
}

// Function to delete the last character
function deleteLast() {
    const display = document.getElementById("display");
    display.innerText = display.innerText.slice(0, -1) || '0';
}

// Function to calculate the result
function calculate() {
    const display = document.getElementById("display");
    try {
        display.innerText = eval(display.innerText) || '0';
    } catch (error) {
        display.innerText = 'Error';
    }
}
