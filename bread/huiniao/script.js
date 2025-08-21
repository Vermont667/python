document.addEventListener("mousemove", function(event){
    let c = document.querySelector('#elem');
    let x = event.clientX
    let y = event.clientY
    c.textContent = 'X = ' + x + ", Y = " + y;

    c.addEventListener('dblclick', function(event){
        event.target.style.background='red'
    })
})

function showText(text){
    let cont = document.getElementById('text1');
    let a = cont.textContent = text
    a.style.fontSize = '150px'
}

