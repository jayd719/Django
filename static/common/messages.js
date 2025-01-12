`-------------------------------------------------------
Django: Message Box
-------------------------------------------------------
Author: JD
ID: 91786
Uses: 
Version: 1.0.8
__updated__ = Thu Jan 12 2025
-------------------------------------------------------`
const messageBox = document.getElementById("message-box");
const SHOWTIME = 5000

// Show the message box with a delay
setTimeout(() => {
    messageBox.classList.remove("translate-y-full", "opacity-0");
}, 800);

// Hide the message box after a delay
setTimeout(() => {
    messageBox.classList.add("translate-y-full");
}, SHOWTIME);

// Remove the element from the DOM after it has faded out
setTimeout(() => {
    messageBox.remove();
}, SHOWTIME + 400);
