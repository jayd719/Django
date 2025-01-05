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


