let a = document.querySelectorAll('.remove-button');
for(let i = 0; i < a.length; i++){
    a[i].addEventListener('click', () => {
        a = document.querySelector('.pane');
        a.remove()
    })
}