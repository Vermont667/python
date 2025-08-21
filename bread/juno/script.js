document.addEventListener("mousemove", function(event){
    let c = document.querySelector('#elem');
    let x = event.clientX
    let y = event.clientY
    c.textContent = 'X = ' + x + ", Y = " + y;

    c.addEventListener('dblclick', function(event){
        event.target.style.background='red'
    })
})

// let cont = document.getElementById('text1');
// function showText(text){
//     document.querySelectorAll('.over').forEach(img => img.style.display = 'none');
//     document.getElementById('ov').style.display = 'block';
//}


let cont = document.getElementById('text1');
function showText(text){
    
    let a = cont.innerHTML = text
    
    // cont.innerHTML = '<img src="1677023540_zefirka-club-p-razdeliteli-dlya-amino-profilya-48.png" alt="" class="ray">' + text 
}

document.addEventListener('DOMContentLoaded', function() {
    const main = document.getElementById('riy');
    const over = document.getElementById('ray');
    main.addEventListener('click', function(){
        over.style.display = 'block';
        setTimeout(function(){
            over.style.display = 'none';
        }, 2000)
    })
})


// let n = document.getElementsByClassName('ray');
// n.addEventListener('click', function() {
//     n.style.display = 'none';
//     setTimeout(function() {
//         n.style.display = 'block';
//     }, 60000);
// })

// function fadeIn(){
//     cont.classList.add('visible')
// }

// const image = document.querySelector('re');
// const over = document.querySelector('overlay');

// image.addEventListener('click', (event) => {
//     const xi = event.clientX = rect.left;
//     const yi = event.clientY = rect.top;
//     if(xi > 174 && xi < 204 && yi > 560 && yi < 589) {
//         over.classList.add('active');
//         setTimeout(() => {
//             over.classList.remove('active');
//         }, 500)
//     }
// })