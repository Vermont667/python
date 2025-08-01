let a = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];

    
document.writeln('<div id="c" class="mounth"></div>')
let d = document.querySelector('#c')   
    for(let i = 0; i < a.length; i++){
        let createColor = () => {
        let r = Math.floor(Math.random() * 256);
        let g = Math.floor(Math.random() * 256);
        let b = Math.floor(Math.random() * 256);
        d.innerHTML += `<div style="background: rgb(${r}, ${g}, ${b}); height: 40px; display: flex; align-items: center; justify-content: center"> ${a[i]} </div>`
        
    } 
    
    createColor()    
}
    

  