document.addEventListener('DOMContentLoaded', async () => {
    const cityInput = document.getElementById('id_city');
    const citySelect = document.getElementById('citySelect');
    const warehouseSelect = document.getElementById('warehouse');
    addSelectOptionPlaceholder(warehouseSelect)
    await loadLocalStorage();
    const warehouseInput = document.getElementById('id_warehouse');
    const nova_post_fullinfo = JSON.parse(localStorage.getItem("data"));
    const hashTableNovaPostInfo = await fillHashTableAsync(nova_post_fullinfo);


    async function fillHashTableAsync(data) {

        return new Promise((resolve, reject) => {
            setTimeout(() => {
                const hashTable = {};
                for (const obj of data) {
                    const { cityRef } = obj;
                    hashTable[cityRef] = obj;
                }
                resolve(hashTable);
            }, 1000);
        });
    }

    // Функция для загрузки городов и их областей
    async function searchCities(query) {
        try {
            const response = await axios.post('https://api.novaposhta.ua/v2.0/json/', {
                apiKey: '2b36e4b9d576535e55d1ed2a20e96a14',
                modelName: 'Address',
                calledMethod: 'searchSettlements',
                methodProperties: {
                    CityName: query,
                    Limit: 5,
                    page: 1
                },
            });


            citySelect.innerHTML = '';
            const search_info = response.data.data;
            console.log(search_info)
            if (search_info.length){
                citySelect.disabled = false
                addSelectOptionPlaceholder(citySelect)

            search_info[0].Addresses.forEach(address => {
                const option = new Option(`${address.Present}`, address.DeliveryCity);
                citySelect.add(option);
                warehouseSelect.disabled = true
            });

            citySelect.style.display = 'block';
            }
            else {
                const errorOption = new Option('Помилка', 'empty');

                citySelect.add(errorOption);
                citySelect.disabled = true
                citySelect.style.display = 'block';
            }
            } catch (error) {
            console.error(error.message);
        }
    }

    // Функция для загрузки отделений выбранного города
    function loadWarehouses(cityRef) {
        try {
            warehouseSelect.disabled = false
            warehouseSelect.innerHTML = '';

            const warehouses = hashTableNovaPostInfo[cityRef].warehouses;
            console.log(warehouses)
            warehouses.forEach(warehouse => {
                const option = new Option(warehouse.name, warehouse.name);
                warehouseSelect.add(option);
            });
        } catch (error) {
            console.error(error.message);
        }
    }




    // Обработчик изменения значения в поле ввода города
    cityInput.addEventListener('input', () => {
        const query = cityInput.value.trim();
        warehouseSelect.disabled = true
        addSelectOptionPlaceholder(warehouseSelect)
        if (query.length >= 2) {
            searchCities(query);
        } else {
            citySelect.style.display = 'none';
        }
    });


    cityInput.addEventListener("focus", function() {
        if (cityInput.length===0 && cityInput.value===''){
            citySelect.style.display = "block";
            citySelect.style.display = 'none';

        }

    });


    // Обработчик выбора города из выпадающего списка
    citySelect.addEventListener('change', () => {
        const selectedCityName = citySelect.options[citySelect.selectedIndex].text;
        cityInput.value = selectedCityName
        const selectedCityRef = citySelect.value;
        loadWarehouses(selectedCityRef);
        addSelectOptionPlaceholder(warehouseSelect)
        // вписать плейсхолдер на віділення виберіть віділення

    });

    warehouseSelect.addEventListener('change', () => {
        const selectedWarehouseName = warehouseSelect.options[warehouseSelect.selectedIndex].value;
        warehouseInput.value = selectedWarehouseName
        console.log(warehouseInput)
    })


    function addSelectOptionPlaceholder (select){
        const emptyOption = new Option('Виберіть н/п', 'empty');
                select.add(emptyOption);
                emptyOption.disabled = true
                emptyOption.selected = true
                emptyOption.hidden = true

    }



});

 async function loadLocalStorage() {
    const jsonFilePath = staticJsonFilePath;
    if (localStorage.getItem('data')){
     localStorage.removeItem('data')
    }
    return fetch(jsonFilePath)
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка при чтении файла JSON');
            }
            return response.json();
        })
        .then(data => {
            localStorage.setItem('data', JSON.stringify(data));
            console.log('Данные успешно добавлены в localStorage.');
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
}