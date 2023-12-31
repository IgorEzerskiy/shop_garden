let elems = document.querySelectorAll('div[class="card"]')
let maxHeight = 0

for (let elem of elems) {
    if (elem.id !== 'cart') {
        if (elem.offsetHeight > maxHeight) {
            maxHeight = elem.offsetHeight
        }
    }
}

for (let elem of elems) {
    if (elem.id !== 'cart') {
        elem.style.height = String(maxHeight) + 'px'
    }
}

function cardClass() {
    let cardContainer = document.getElementById('card-container')
    const screenWidth = window.innerWidth;

    if (screenWidth < 980) {
        cardContainer.classList.remove('row-cols-md-3')
        cardContainer.classList.add('row-cols-md-2')
    } else {
        cardContainer.classList.remove('row-cols-md-2')
        cardContainer.classList.add('row-cols-md-3')
    }
}

cardClass();

window.addEventListener('resize', cardClass);
