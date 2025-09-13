let inputRub = document.querySelector('#rub');
let inputUsd = document.querySelector('#usd');
let inputEuro = document.querySelector('#euro');

inputRub.addEventListener('input', () => {
    let request = new XMLHttpRequest();
    request.open("GET", 'curs.json');
    request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    request.send();

    request.addEventListener('load', () => {
        if(request.status == 200){
            console.log(request.response);
            let data = JSON.parse(request.response);
            console.log(data);
            inputUsd.value = (inputRub.value / data.current.usd).toFixed(2);
            inputEuro.value = (inputRub.value / data.current.euro).toFixed(2);
        } else{
            inputUsd.value = 'Что-то пошло не так'
            inputEuro.value = 'Что-то пошло не так'
        }
    })
})