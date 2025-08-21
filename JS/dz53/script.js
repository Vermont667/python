function swapImages() {
    let firstNum = document.getElementById('firstNum').value;
    let secondNum = document.getElementById('secondNum').value; 

    if (firstNum < 1 || firstNum > 3 || 
        secondNum < 1 || secondNum > 3) {
        alert('Введите числа от 1 до 3');
        return;
    }
            
    if (firstNum === secondNum) {
        alert('Номера картинок должны быть разными');
        return;
    }
            
    let firstImg = document.getElementById('img' + firstNum);
    let secondImg = document.getElementById('img' + secondNum);
            
    let NoneSrc = firstImg.src;
    firstImg.src = secondImg.src;
    secondImg.src = NoneSrc;
}


