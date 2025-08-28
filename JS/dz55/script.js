let input = document.querySelector('input[type="button"]');
input.addEventListener('click', anect);

function anect(){
    let f = document.form1.ra;
    for(let i = 0; i < f.length; i++){
        if(f[i].checked){
            alert('Вы выбрали: ' + f.value)
        }
    }
}