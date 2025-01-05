function createHeader() {
    const header = document.createElement("header")
    header.className = "bg-white p-4 shadow-lg flex flex-wrap items-center justify-between gap-4 md:gap-6"

    // brand name 
    const brandname = document.createElement("h1")
    brandname.className = "text-3xl font-extrabold text-green-600 tracking-wide"
    brandname.innerText = "Blinkit"

    // Location Detatils 

}

// Call the function to create and add the header to the page
document.addEventListener("DOMContentLoaded", createHeader);
