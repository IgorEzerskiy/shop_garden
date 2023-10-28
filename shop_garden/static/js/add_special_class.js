// Function to add or remove the CSS class based on screen width
function addOrRemoveClass() {
    const targetElement = document.getElementById('nav-ul');
    const loginBTN = document.getElementById('nav-login')
    const screenWidth = window.innerWidth;
    
    if (screenWidth < 1200) {
        // Add the CSS class if the screen width is less than 1200 pixels
        targetElement.classList.add('list-group-horizontal');
        targetElement.classList.add('nav-margin');
        loginBTN.classList.remove('ms-2');
    } else {
        // Remove the CSS class if the screen width is 1200 pixels or more
        targetElement.classList.remove('list-group-horizontal');
        targetElement.classList.remove('nav-margin');
        loginBTN.classList.add('ms-2');
    }
}

// Initial check on page load
addOrRemoveClass();

// Listen for the window resize event and update the class
window.addEventListener('resize', addOrRemoveClass);
