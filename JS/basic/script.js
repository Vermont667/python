'use strict';

/* let message;  // let, const, var
message = 'Hello';
console.log(message)

let a = 10;
a = 3.5;

let b, c;
let d = 5, e = 2;

let firstName = 'Irina'
console.log(firstName) */ 


// const week = 7;

/* let str1 = "Двойные кавычки";
let str2 = 'Одинарные кавычки';
let str3 = `Обратные ${5 + 9} и ${str2}
    кав   ыч   ки`;

console.log(str1);
console.log(str2);
console.log(str3); */

/* let firstName = 'Ivan';
alert(`Hello, ${firstName}`); */


/* let day = 365;
let planet = 'Земля';
let num = '7 млрд.';
let sone = 'Солнце';

alert(`Мы живём на планете ${planet}, она делает один оборот вокруг ${sone} за ${day}. Население нашей планеты составляет примерно ${num} человек`) */


// let res = confirm('Знаете ли вы HTML?');
// console.log(res); // OK => true   Отмена => false

// if(res){
//     alert('Пора учить JavaScript')
// } else{
//     alert('Нужно выучить')
// }

/* ТИпы данных 
- number
- string
- boolean
- null (object)
- undefined

- object
*/

// let number = 13;
// console.log(number, typeof number);
// console.log(number, typeof (number));

// let a = 23.56;
// console.log(a, number, typeof (a));

// let b = 'hello';
// console.log(b, number, typeof (b));

// let c = true;
// console.log(c, number, typeof (c));

// let d = null;
// console.log(d, number, typeof (d));

// let e = undefined;
// console.log(e, number, typeof (e));


// let res = prompt('Ваше имя:', 'Значение по умолчанию');
// console.log(res)  // OK => string, Отмена => null

// let a = 12;
// let b = 8;

// console.log('+:', a + b)
// console.log('-:', a - b)
// console.log('*:', a * b)
// console.log('/:', a / b)
// console.log('%:', a % b)
// console.log('**:', a ** b)

// NanN - Not a Number (error)

// let a = '23';
// let b = '6a';
// console.log(a - b); 


// let a = +prompt('Введите первое число:', 5);
// let b = parseInt(prompt('Введите второе число:', 3));
// // a = parseInt(a);
// // b = parseInt(b);
// alert('Результат:' + (a + b));


// console.log(parseInt('21.84'));  // 21 Number
// console.log(parseFloat('21.84'));  // 21.84 Number
// console.log(parseFloat('21.843232').toFixed(2));  // 21.84 String
// console.log(Number('21.84'));  // 21.84 Number
// console.log(+'21.84');  // 21.84 Number
// // console.log(+1*'21.84');  // 21.84 Number
// console.log(+true);  // 1
// console.log(+false);  // 0


// let a = 0, b = 0;
// a++;  // a += 1
// b--;  // a -= 1
// console.log(a);
// console.log(b);

// let a = 0, b = 0;
// ++a; //1
// b++; //1
// console.log(a);
// console.log(b);

// let a = 0, b = 0;
// let c = a++ + 2;  // 2 = 0 + 2, a = 1
// let d = ++b + 2;  //  3 = 1 + 2
// console.log(a);  //1
// console.log(b);  //1
// console.log(c);  //2
// console.log(d);  //3

// let a = 1;
// let b = a++;  // b = 1, a = 2
// let c = b + 5 + a;  // 8 = 1 + 5 + 2
// console.log(c); // 8

// a++ Или a += 1 или a = a + 1

// let a = 1;
// let b = ++a;  // b = 2
// let c = b + 5 + a;  // 9 = 2 + 5 + 2
// console.log(c); // 9

// let num = 10;
// num += 5;
// console.log(num);  //15
// num -= 7;
// console.log(num)  //8

// console.log(5 > 3);  //true
// console.log(5 < 3);  //false
// console.log(5 <= 5);  //true
// console.log(5 >= 5);  //true
// console.log(5 == '5');  //true
// console.log(5 === '5');  //false
// console.log(5 != '5');  //false
// console.log(5 !== '5');  //true

// 7 > 3 ? alert('7') : alert('3');  // 7  // 7 = true
// 7 < 3 ? alert('7') : alert('3');  // 3  // 3 = false

// let ch = prompt('Угадайте число от 1 до 10');
// let num = 7;
// // (ch == num) ? alert('Угадали') : alert('Не угадали')
// (ch == num) ? alert('Угадали') : (ch < num) ? alert('Загаданное число больше') : alert('Загаданное число меньше');

// if (условие){
//     блок истина
// } else {
//     блок ложь
// }

/* 
false => 0, 0.0, '', false, null, undefined, NaN
*/
// a = 0;
// if (a){
//     console.log('TRUE');
// } else {
//     console.log('FALSE');
// }

// let a = +prompt('Введите первое число:', 5);
// let b = +prompt('Введите второе число:', 0);

// if(b != 0)
//     alert(a / b);  
// else
//     alert('На ноль делить нельзя');  // infinity


// let a = 12;
// let b = 12;

// if (a > b){
//    alert(a + ' > ' + b);
//  
// if (a < b){
//    alert(a + ' < ' + b);
//  
// if (a == b) {
//    alert(a + ' == ' + b);
// 

// if (a > b){
//     alert(a + ' > ' + b);
// } 
// else if (a < b) {
//     alert(a + ' < ' + b);
// }
// else {
//     alert(a + ' == ' + b);
// }


// let login = prompt('Введите логин: ', 'admin');
// if(login) {
//     if(login == 'admin'){
//         let psw = prompt('Введите пароль: ');
//         if(psw){
//             if(psw == 'password'){
//                 alert('Добро пожаловать!')
//             } else {
//                 alert('Пароль не верен')
//             }
//         } else {
//             alert('Вход отменен')
//         }
//     } else {
//         alert('Я вас не знаю');
//     }
// }else {
//     alert('Вход отменен');
// }

// if(5 == 5 || 5 > 8) {
//     console.log('true');
// } else {
//     console.log('false');
// }

// console.log(!9);  // 9 => !true => false
// console.log(!0);  // 0 => !false => true
// console.log(!!0);  // 0 => !!false => !true => false

// let age = prompt('Введите возраст: ');
// if (age > 17 && age < 70) {
//     alert('Вы можете получать права')
// } else {
//     alert('Права не давать');
// }

// let age = prompt('Введите возраст: ');
// if (age < 18 || age > 69) {
//     alert('Права не давать')
// } else {
//     alert('Вы можете получать права');
// }

// switch (условие) {
//     case значение_1:
//         блок кода;
//         break;
//     case значение_n:
//         блок кода;
//         break;
//     default:
//         блок кода;
// }

// let a = +prompt('Введите результат "2 + 2": ');
// switch(a){  // a === 3
//     case 4:
//         alert('Верно');  
//         break 
//     case 3:
//     case 5:
//         alert('Не верно'); 
//         break
//     default:
//         alert("Я таких значений не знаю");
// }

// let m = +prompt('Введите номер месяца');
// let n;
// switch(m){
//     case 1: n='Январь'; break;
//     case 2: n='Февраль'; break;
//     case 3: n='Март'; break
//     case 4: n='Апрель'; break;
//     case 5: n='Май'; break
//     case 6: n='Июнь'; break
//     case 7: n='Июль'; break
//     case 8: n='Август'; break;
//     case 9: n='Сентябрь'; break;
//     case 10: n='Октябрь'; break;
//     case 11: n='Ноябрь'; break;
//     case 12: n='Декабрь'; break;
//     default: n='Неправильный номер месяца';
// }
// alert("Вы ввели: " + n);

// document.writeln('Текст выведен в браузер');
// document.writeln('<p>Текст <b>выведен</b> в браузер</p>');
// document.writeln('<img src="1.jpg" />')


// let i = 5;
// do {
//     document.writeln('Это номер: ' + i + '<br>');
//     i++;
// } while(i < 5);

// document.writeln('<br><br>Второй цикл');

// let j = 5;
// while (j < 5){
//     document.writeln('Это номер: ' + j + '<br>');
//     j++;
// }

// let i = 1;
// do {
//     document.writeln('Квадрат: ' + i + ' равен ' + i ** 2 + '<br>');
//     i++;
// } while(i < 8);


// let ch, pr=1;

// do{
//     ch = prompt('Введите число: ', 10);
//     if(ch < 0){
//         break
//     }
//     if(ch == 0){
//         continue
//     }
//     pr *= ch;
// }while(true);

// alert(pr);


// for(инициализация_переменной; проверка_условия; изменение_переменной){
//     тело цикла;
// }

// for(let i = 1; i < 6; i++){
//     document.writeln(i + '<br>');
// }

// document.writeln('<br><br>Второй цикл<br>');
// let j = 1;
// while(j < 6){
//     document.writeln(j + '</br>');
//     j++;
// }

// let i = 1;
// for(;;){
//     if(i == 6){
//         break
//     }
//     document.writeln(i + '<br>');
//     i++;
// }

// for(var i = 1; i < 6; i++){
//     document.writeln(i + '<br>');
// }

// document.writeln('i = ' + i + '<br>');

// for(let i = 0; i < 4; i++){
//     document.writeln('+++ <br>');
//     for(let j = 0; j < 2; j++){
//         document.writeln('--- <br>')
//     }
// }

// let tr = prompt("Введите кол-во строк");
// let td = prompt("Введите кол-во столбцов");
// let symbol = prompt('Введите символ');

// document.writeln('<table border="1">');
// for(let i = 0; i < tr; i++){
//     document.writeln('<tr>');
//     for(let j = 0; j < td; j++){
//         document.writeln('<td>' + symbol + '</td>');
//     }
//     document.writeln('</tr>');
// }
// document.writeln('</table>');


// document.writeln('<table border="1" width="240">');
// for(let i = 1; i < 11; i++){
//     document.writeln('<tr align="center">');
//     for(let j = 1; j < 11; j++){
//         if(i % 2 == 0){
//         document.writeln('<td bgcolor="red">' + i * j + '</td>');
//     } else{
//         document.writeln('<td bgcolor="yellow">' + i * j + '</td>');
//     }
//     }
//     document.writeln('</tr>');
// }
// document.writeln('</table>');


// Массив

// let arr1 = new Array(2, 6, 8);
// let arr2 = new Array(5);

// let arr3 = [1, 3, 7];
// let arr4 =[5]

// console.log(arr1)
// console.log(arr2)
// console.log(arr3)
// console.log(arr4)
// console.log(arr3.length)

// document.writeln(arr1);
// alert(arr1);

// let f = [1, 2, 3, 4, 5, 6, 7];
// console.log(f);
// console.table(f)
// console.log('Length: ', f.length)

// f.length = 3;
// console.log(f);
// console.log('Length: ', f.length)

// f.length = 7;
// console.log(f);
// console.log('Length: ', f.length)

// f.length = 0;
// console.log(f);
// console.log('Length: ', f.length)


// let arr = new Array();
// arr[0] = 15;
// arr[1] = 20;
// arr[2] = 56;
// arr[3] = 12;
// arr[5] = 6;
// console.log(arr);

// for(let i = 0; i < arr.length; i++){
//     document.writeln(arr[i] + '<br>');
// }

// let arr = new Array(6);

// for(let i = 0; i < arr.length; i++){
//     arr[i] = prompt('Введите ' + (i + 1) + ' элемент массива')
// }

// console.log(arr);

// for(let i = 0; i < arr.length; i++){
//     document.writeln(arr[i] + '<br>');
// }

// let arr = [2, 6, 7, 'hui', 1.5, true];
// console.log(arr);

// let mas = [[2, 1, 1], [6, 3, 7], [8, 5, 6]];
// console.log(mas);
// console.table(mas)

// console.log(mas[1][2])

// document.writeln(mas + '<br>');


// let questions = ['На ноль делить можно?', "Волга впадает в каспийское море", "Атмосферное давление увеличивается с высотой", "2х2 будет 8", "Дельфины это рыбы", "Мадонна это настоящее имя певицы", "Первая мировая война началачь 1 сентября 1939 года"];

// let correct_answer = [false, true, false, false, false, false, false];

// let sum = 0;
// let res = new Array();

// for(let i = 0; i < questions.length; i++){
//     let answer = confirm(questions[i]);
//     if(answer == correct_answer[i]){
//         res[i] = 10;
//         sum += res[i]
//     } else {
//         res[i] = 0;
//     }
// }

// console.log(res);
// console.log(sum);

// document.writeln('<table border="1" width="500"');

// document.writeln('<tr>');
// document.writeln('<th>Вопрос</th>')
// document.writeln('<th>Баллы</th>')
// document.writeln('</tr>');

// for(let i = 0; i < questions.length; i++){
//     document.writeln('<tr>');
//     document.writeln('<td>' + questions[i] + '</td>');
//     document.writeln('<td>' + res[i] + '</td>');
//     document.writeln('</tr>');
// }

// document.writeln('<tr>');
// document.writeln('<th>Итого</th>')
// document.writeln('<th>' + sum + '</th>')
// document.writeln('</tr>');

// document.writeln('</table>');


// let text1 = document.getElementById('text_1');
// console.log(text1);
// console.log(text1.textContent);

// text1.textContent = 'Новое значение';

// let text2 = document.getElementById('text_2');
// text2.innerHTML = 'Новое содержимое <b> c HTML</b>'

// let res = +prompt('Выберите изображение: ', '1-собака, 2-кот, 3-птица, 4-рыба');
// document.writeln('<div id="image"></div>');
// let img = document.getElementById("image");

// switch(res){
//     case 1:
//         img.innerHTML = "<img src='img/dog.jpg'>";
//         break;
//         case 2:
//             img.innerHTML = "<img src='img/cat.jpg'>";
//             break;
//         case 3:
//             img.innerHTML = "<img src='img/bird.jpg'>";
//             break;
//         case 4:
//             img.innerHTML = "<img src='img/fish.jpg'>";
//             break;
//         default:
//             alert('Такого изображения нет')
// }

// let teg = document.getElementsByTagName('p')[2];
// console.log(teg);
// teg.innerHTML = 'Hello teg';
// teg.style.background = 'silver';
// teg.style.padding = '10px 20px';
// teg.style.color = 'blue';
// teg.style.fontWeight = 'bold';

// teg.id = 'test';
// teg.className = 'x';


// let q = document.getElementsByClassName('a');
// console.log(q);
// q[1].style.color = 'red';
// q[0].style.color = 'blue';


// document.querySelector(css);
// document.querySelectorAll(css);

// // let select_class = document.querySelector('.a');
// let select_class = document.querySelectorAll('.a')[1];
// console.log(select_class);

// let select_tag = document.querySelector('p');
// let select_tag = document.querySelectorAll('p')[1];
// console.log(select_tag);

// let select_id = document.querySelector('#text_1');
// let select_id = document.querySelectorAll('#text_1')[0];
// console.log(select_id);
// select_id.style.color = 'red'


// let el = document.querySelector("h2");
// el.style.color = 'red';

// let el1 = document.querySelectorAll('h2')[1];
// el1.style.color = 'purple'

// let lists = document.querySelectorAll('li');
// console.log(lists);

// for(let i = 0; i < lists.length; i++){
//     lists[i].innerHTML += ' - фрукт';
// }

// let purples = document.querySelectorAll('.purple li');
// for(let i = 0; i < purples.length; i++){
//     purples[i].innerHTML += '!!!'
// }

// // let m = document.querySelectorAll('.red li')[1];
// let m = document.getElementsByClassName('red')[0].getElementsByTagName('li')[1];
// m.style.color = 'pink'


// document.writeln("<div id='divSample'></div>");
// let div = document.querySelector('#divSample');
// div.innerHTML = 'Дюбель — конструктивный элемент, который используется для укрепления винта или предмета на стене, на потолке или на полу в помещении или под открытым небом в различных материалах (бетон, кирпич и прочее). Сам дюбель удерживается в конструкции при помощи сил трения. С некоторого времени элементы связи и укрепления, дюбели и винт (шуруп) объединяют в одно целое и используются, прежде всего, для тяжёлых нагрузок. Дюбели предлагаются в различных величинах, которые руководствуются диаметром дюбеля (и соответственно необходимых отверстием), измеренным в миллиметрах.'

// div.style.background='#f0f';
// div.style.color='#99ffff';
// div.style.width='50%';
// // div.style.outline='10px dotted #000';
// div.style.border='10px dotted #000';

// div.className = 'resetFont';

// let res = document.querySelector('.resetFont');
// res.style.fontSize = '12px';
// res.style.fontWeight = 'bold';
// res.style.textDecoration = 'line-through';


let js = ['нужно', "учить", "JavaScript"];
console.log(js);

// конец массива
console.log(js.pop());
console.log(js);

js.push("JavaScript", '!');
console.log(js);

// начало массива
console.log(js.shift());
console.log(js);

js.unshift('Почему', "нужно");
console.log(js);

// срез
let arr = js.slice(1, 3);
console.log(arr);
console.log(js.slice(1));

// любая часть массива
js.splice(0, 1);
console.log(js);

js.splice(0, 2, 'Мы', "изучаем");  //замена элементов начиная с индекса
console.log(js);

js.splice(2, 0, 'сложный', "язык")  //добавление элементов начиная с индкса
console.log(js);

js.splice(-3, 0, "но", "очень", "интересный");  // начиная с -3 удалчет 0 элементов
console.log(js);



