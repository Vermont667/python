let a = document.querySelectorAll('.remove-button');
for(let i = 0; i < a.length; i++){
    a[i].addEventListener('click', () => {
        a[i].parentNode.remove();
    })
}