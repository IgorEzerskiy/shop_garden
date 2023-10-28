function cartClass() {
    const cartContainer = document.querySelectorAll('#product-container > div > div > div');
    const cartButtonsGroup = document.querySelectorAll('#product-container > div > div > div > div:nth-child(2)')
    const screenWidth = window.innerWidth;

    if (screenWidth < 580) {
        // Add the CSS class if the screen width is less than 1200 pixels
        for (let elem of cartContainer) {
            elem.classList.add('flex-column');
        }
        for (let elem of cartButtonsGroup) {
            elem.classList.add('mt-3')
        }
    } else {
        // Remove the CSS class if the screen width is 1200 pixels or more
        for (let elem of cartContainer) {
            elem.classList.remove('flex-column');
        }
        for (let elem of cartButtonsGroup) {
            elem.classList.remove('mt-3')
        }
    }
}

// Initial check on page load
cartClass();

// Listen for the window resize event and update the class
window.addEventListener('resize', cartClass);
