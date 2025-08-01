let image = document.getElementById('image')

function on(){
    image.src = '6ee2054af14527f1c490797c39f6cd0e.webp'
}

function off(){
    image.src = ''
}

let a = document.querySelectorAll('a')

for(let i = 0; i < a.length; i++){
    a[i].style.fontSize = '50px';
    a[i].style.textDecoration = 'none'
    image.style.position = 'absolute'
    image.style.top = '100px'
}
