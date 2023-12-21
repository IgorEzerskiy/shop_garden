function profilePaginationStart() {
    let tr_list = document.querySelectorAll("tbody#orders > tr")
    let showMoreBtn = document.getElementById('show-more-btn')

    showMoreBtn.setAttribute('data-paginator', '5')

    for (let i = 0; i <= tr_list.length - 1; i++) {
        if (i > 5) {
            tr_list[i].style.display = 'none';
        }
    }
}

function profilePaginationEventMore() {
    let tr_list = document.querySelectorAll("tbody#orders > tr")
    let showMoreBtn = document.getElementById('show-more-btn')
    let paginatorValue = Number(showMoreBtn.getAttribute('data-paginator'))
    let i = paginatorValue

    for (i; i <= paginatorValue + 5; i++) {
        if (i <= tr_list.length - 1) {
            if (tr_list[i].style.display === 'none') {

                tr_list[i].style.display = '';
            }
        } else {
            showMoreBtn.setAttribute('data-action', 'less')
            let changeIcon = document.querySelector('#show-more-btn > i')
            changeIcon.classList.remove('fa-angles-down')
            changeIcon.classList.add('fa-angles-up')
            break
        }
    }
    paginatorValue = i
    showMoreBtn.setAttribute('data-paginator', String(paginatorValue))
}

function profilePaginationEventLess() {
    let tr_list = document.querySelectorAll("tbody#orders > tr")
    let showLessBtn = document.getElementById('show-more-btn')

    showLessBtn.setAttribute('data-paginator', '5')

    for (let i = 5; i <= tr_list.length - 1; i++) {
        if (i > 5) {
            tr_list[i].style.display = 'none';
        }
    }
    showLessBtn.setAttribute('data-action', 'more')
    let changeIcon = document.querySelector('#show-more-btn > i')
    changeIcon.classList.remove('fa-angles-up')
    changeIcon.classList.add('fa-angles-down')
}

function mapping() {
    if (showBtn.getAttribute('data-action') === 'more') {
        profilePaginationEventMore()
    } else if (showBtn.getAttribute('data-action') === 'less') {
        profilePaginationEventLess()
    }
}

profilePaginationStart();

let showBtn = document.getElementById('show-more-btn')

showBtn.addEventListener('click', mapping)
