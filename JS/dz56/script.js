
let but = document.querySelector('input[type="button"]');
but.addEventListener('click', smsUser);

function smsUser(){
    let sms = document.querySelector('textarea').value;
    let name = document.querySelector('input[type="text"]').value;
    console.log(but);
    let reg = /([\w.]+@[\w.]+\.[a-z]{2,3})/ig;
    sms = sms.replace(reg, "<span style='color: blue'>$1</span>")
    // document.writeln(`
    //     <fieldset>
    //         <legend>${name}</legend>
    //         <div>${sms}<div>
    //     </fieldset>
    // `)
    let form = document.querySelector('form');
    form.insertAdjacentHTML('beforeend', `
         <fieldset>
             <legend>${name}</legend>
             <div>${sms}<div>
         </fieldset>`)
}