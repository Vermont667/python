
function Const(name, age, job, ava){
    this.name = name,
    this.age = age,
    this.job = job,
    this.ava = ava

        this.who = function(){
        document.writeln('<div id="pers">' + `<img src='${this.ava}'>` + '<div id="name">' + this.name + '</div></div>' + '<p>Я ' + '<b>' + this.name + '</b>' + ' мне ' + '<b>' + this.age + '</b>' + ' лет. Я работаю ' + '<b>' + this.job + 'ом. </b></p><br>')
    }
 
}
let img = 'https://avatars.mds.yandex.net/i?id=34c561b53f0e8a4e8f82192c2a15760818fc1e184187114b-12624586-images-thumbs&n=13'
let dmitry = new Const('Дмитрий', 26, 'Дизайнер', img);
dmitry.who()
let img2 = 'https://avatars.mds.yandex.net/i?id=85796ac307d80bff9fb7fba97e45096131b4924f-16308574-images-thumbs&n=13'
let stanislav = new Const('Станислав', 29, "Программист", img2);
stanislav.who()
let img3 = 'https://avatars.mds.yandex.net/i?id=8ffa379e8299d433c82ef62ee0644d0ebef9f501-11938745-images-thumbs&n=13'
let sergey = new Const('Сергей', 35, "Менеджер", img3);
sergey.who()
console.log(dmitry);