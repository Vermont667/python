class Drama{
    constructor(img, text){
        this.img = img;
        this.text = text;
    }

    reg(id){
        let out = `
            <img src='${this.img}' alt='' style='width: 250px'>
            <h3>${this.text}</h3>
        `

        document.querySelector(`#${id}`).innerHTML = out;
    }
}

let img = 'https://k-dramy.ru/uploads/posts/2025-06/memuary-rati.webp';
let drama = new Drama(img, 'Мемуары Рати');
drama.reg('drama');

let img1 = 'https://k-dramy.ru/uploads/posts/2025-03/thjem-po.webp';
let drama1 = new Drama(img1, 'Тхэм-По');
drama1.reg('drama1');

let img2 = 'https://k-dramy.ru/uploads/posts/2025-05/naslednyj-princ.webp';
let drama2 = new Drama(img2, 'Наследный принц');
drama2.reg('drama2');

let img3 = 'https://k-dramy.ru/uploads/posts/2025-05/nokaut.webp';
let drama3 = new Drama(img3, 'Нокаут');
drama3.reg('drama3');

let img4 = 'https://k-dramy.ru/uploads/posts/2025-03/malysh-s-gonok.jpg';
let drama4 = new Drama(img4, 'Малыш с гонок');
drama4.reg('drama4');

let img5 = 'https://k-dramy.ru/uploads/posts/2025-03/zatmenie.jpg';
let drama5 = new Drama(img5, 'Затмение');
drama5.reg('drama5');

let img6 = 'https://k-dramy.ru/uploads/posts/2025-03/glubokaja-noch.jpg';
let drama6 = new Drama(img6, 'Глубокая ночь');
drama6.reg('drama6');

let img7 = 'https://k-dramy.ru/uploads/posts/2025-03/ne-ja.jpg';
let drama7 = new Drama(img7, 'Не я');
drama7.reg('drama7');

let img8 = 'https://k-dramy.ru/uploads/posts/2025-03/ljubov-vitaet-v-vozduhe.jpg';
let drama8 = new Drama(img8, 'Любовь витает в воздухе');
drama8.reg('drama8');
