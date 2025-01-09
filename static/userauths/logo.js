`-------------------------------------------------------
Django: Clone LOGO Css
-------------------------------------------------------
Author: JD
ID: 91786
Uses: 
Version: 1.0.8
__updated__ = Thu Jan 09 2025
-------------------------------------------------------`
function cloneLogoStyles(id) {
    const loginFormLogo = document.getElementById(id);
    const logo = document.getElementById('headerlogo');

    if (!loginFormLogo || !logo) {
        console.warn("One or both logo elements not found.");
        return;
    }

    // Copy class names
    loginFormLogo.className = `${logo.className} text-7xl text-center mb-5`;

    // Clone inner content
    loginFormLogo.innerHTML = logo.innerHTML;
}


