function getQueryParameters(url) {
    if (url.indexOf('?') === -1) {
        return {};
    }

    const queryString = url.split('?')[1];
    const queryParams = queryString.split('&');

    const params = {};

    queryParams.forEach(param => {
        const [key, value] = param.split('=');
        params[decodeURIComponent(key)] = decodeURIComponent(value);
    });

    return params;
}

function checkLoaded() {
    if (document.readyState === "complete") {
        const currentURL = window.location.href;
        const queryParams = getQueryParameters(currentURL);

        let sort_array = document.querySelectorAll('select[name="sort"] > option')
        let discount = document.querySelector("input[name='discount']")

        for (let elem of sort_array){
            if (elem.value === queryParams['sort']){
                elem.selected = 'selected';
            }
        }

        if (queryParams['discount'] === 'on'){
            discount.checked = true;
        }

        console.log(queryParams['min']);
    } else {
        setTimeout(checkLoaded, 15);
    }
}

window.addEventListener('load', checkLoaded);
