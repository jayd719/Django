`-------------------------------------------------------
Django: Cookie Consent Pop Up Message
-------------------------------------------------------
Author: JD
ID: 91786
Uses: 
Version: 1.0.8
__updated__ = Thu Jan 09 2025
-------------------------------------------------------`


// Function to create and display a cookie consent popup
function cookieConsentPopup() {
    // Create the main popup container
    const cookiePopup = document.createElement("div");
    cookiePopup.id = "cookie-popup";
    cookiePopup.className = "fixed bottom-0 left-0 right-0 bg-gray-100 p-4 shadow-lg flex flex-col sm:flex-row items-center justify-between gap-4 m-4";

    // Create the decline button
    const declineButton = document.createElement("button");
    declineButton.className = "px-4 py-2 bg-gray-200 text-gray-800 rounded hover:bg-gray-300 transition-colors";
    declineButton.innerText = "Decline";
    declineButton.addEventListener("click", () => {
        cookiePopup.remove(); // Remove popup when declined
    });

    // Create the accept button
    const acceptButton = document.createElement("button");
    acceptButton.className = "px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors";
    acceptButton.innerText = "Accept";
    acceptButton.addEventListener("click", () => {
        document.cookie = "cookieConsent=true; path=/; max-age=31536000"; // Set a 1-year cookie
        cookiePopup.remove(); // Remove popup after acceptance
    });

    // Create a div for buttons
    const buttonContainer = document.createElement("div");
    buttonContainer.className = "flex gap-4";
    buttonContainer.append(declineButton, acceptButton);

    // Create text container with message
    const textContainer = document.createElement("div");
    textContainer.className = "container mx-auto max-w-6xl";
    textContainer.innerHTML = `<p class="text-sm text-gray-700">
        We use cookies to enhance your browsing experience and analyze our traffic. 
        By clicking "Accept", you consent to our use of cookies.
    </p>`;

    // Append elements to the popup
    cookiePopup.append(textContainer, buttonContainer);

    // Append popup to the document body
    document.body.appendChild(cookiePopup);
}

// Check if the user has already accepted cookies before displaying the popup
if (!document.cookie.includes("cookieConsent=true")) {
    cookieConsentPopup();
}
