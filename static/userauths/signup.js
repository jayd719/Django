document.addEventListener("DOMContentLoaded", () => {
    applyFormStyling();
    cloneLogoStyles("loginformlogo1");
});

/**
 * Applies styling to the parent of the sign-up form.
 */
function applyFormStyling() {
    const signUpForm = document.querySelector("#signupform");

    if (!signUpForm?.parentElement) {
        console.warn("Sign-up form or its parent was not found.");
        return;
    }

    const parentElement = signUpForm.parentElement;

    // Define the desired classes to be added
    const classesToAdd = [
        "bg-white", "p-8", "rounded-lg", "shadow-xl",
        "max-w-lg", "w-full", "mx-auto", "z-[10]"
    ];

    parentElement.classList.add(...classesToAdd);
    parentElement.classList.remove("hidden", "invisible");
}
