`-------------------------------------------------------
Django: Location Module
-------------------------------------------------------
Author: JD
ID: 91786
Uses: 
Version: 1.0.8
__updated__ = Thu Jan 07 2025
-------------------------------------------------------`

// Function to get user's geolocation
function getUserLocation() {
    return new Promise((resolve, reject) => {
        if (!("geolocation" in navigator)) {
            return reject(new Error("Geolocation is not supported by this browser."));
        }

        navigator.geolocation.getCurrentPosition(
            (position) => resolve(position.coords),
            (error) => reject(new Error(`Error getting location: ${error.message}`))
        );
    });
}

// Function to fetch city name based on latitude and longitude
async function fetchCityName(latitude, longitude) {
    const url = `https://nominatim.openstreetmap.org/reverse?lat=${latitude}&lon=${longitude}&format=json`;

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

        const data = await response.json();
        return data.address.city || data.address.town || data.address.village || "Unknown";
    } catch (error) {
        throw new Error(`Error fetching city: ${error.message}`);
    }
}

// Main function to get city name
async function getCityName() {
    try {
        const { latitude, longitude } = await getUserLocation();
        return await fetchCityName(latitude, longitude);
    } catch (error) {
        throw error; // Re-throw error for handling at higher levels
    }
}


(async function () {
    try {
        const city = await getCityName();
        document.getElementById('cityname').innerText = city;
    } catch (error) {
        console.error(error.message);
    }
})();
