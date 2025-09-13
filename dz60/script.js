let form = document.form1;

let message = {
    loading: 'Загрузка',
    success: 'Спасибо! Скоро мы с вами свяжемся',
    failure: 'Что-то пошло не так...'
};

form.addEventListener('submit', event => {
    event.preventDefault();

    let msg = document.createElement('div');
    msg.classList.add('styl')
    let di = document.querySelector('.d');
    msg.textContent = message.loading;
    di.appendChild(msg)
    
    let request = new XMLHttpRequest();
    request.open('POST', 'server.php');

    let formData = new FormData(form);
    request.send(formData);

    request.addEventListener('load', function(){
        if(request.status == 200){
            console.log(request.response);
            msg.textContent = message.success;
        } else {
            msg.textContent = message.failure;
        }
        form.reset();
        setTimeout(() => msg.remove(), 3000);
    })
})