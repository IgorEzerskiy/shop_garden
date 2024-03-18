function hideShowNavCategory() {
    const navList = document.getElementById('nav-category-list')
    const screenWidth = window.innerWidth;

    if (screenWidth < 800) {
        navList.style.display = 'none';
    } else {
        navList.style.display = '';
    }
}

function disableNavCategoryImg() {
    let imgArray = document.querySelectorAll('#nav-category-ul > li > a > div > img')
    const screenWidth = window.innerWidth;

    if (screenWidth < 980) {
        for (let elem of imgArray) {
            elem.style.display = 'none';
        }
    } else {
        for (let elem of imgArray) {
            elem.style.display = '';
        }
    }
}

function checkLoaded() {
    if (document.readyState === "complete") {
        hideShowNavCategory();
        disableNavCategoryImg();
    } else {
        setTimeout(checkLoaded, 15);
    }
}

window.addEventListener('resize', checkLoaded);
window.addEventListener('load', checkLoaded);
