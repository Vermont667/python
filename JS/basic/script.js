'use strict';

// const { createElement } = require("react");

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


// let js = ['нужно', "учить", "JavaScript"];
// console.log(js);

// // конец массива
// console.log(js.pop());
// console.log(js);

// js.push("JavaScript", '!');
// console.log(js);

// // начало массива
// console.log(js.shift());
// console.log(js);

// js.unshift('Почему', "нужно");
// console.log(js);

// // срез
// let arr = js.slice(1, 3);
// console.log(arr);
// console.log(js.slice(1));

// // любая часть массива
// js.splice(0, 1);
// console.log(js);

// js.splice(0, 2, 'Мы', "изучаем");  //замена элементов начиная с индекса
// console.log(js);

// js.splice(2, 0, 'сложный', "язык")  //добавление элементов начиная с индкса
// console.log(js);

// js.splice(-3, 0, "но", "очень", "интересный");  // начиная с -3 удалчет 0 элементов
// console.log(js);

// let str = js.join(" ");
// console.log(str)

// js.reverse();  // Разворачивает массив
// console.log(js);

// js.sort();
// console.log(js);

// let n = [1, 5, 15, 2];
// n.sort((a, b) => a - b);
// console.log(n);

// let st = ["Фамилия", "Имя", "Отчество"]
// let fio = new Array(3);

// for(let i = 0; i < fio.length; i++){
//     // fio[i] = prompt('Введите данные:\n' + st[i]);
//     fio[i] = prompt('Введите данные:', st[i]);  
// }

// alert(fio.join(' '))


// Функции

// Fuction Declaration

// function caption(a, b, c){
//     let res = a + b + c;
//     return res;
// }

// let test = caption(10, 20, 30);
// console.log(test);


// function showArrayContent(arrayToShow) {
//     if(arrayToShow.length == 1){
//         return arrayToShow;
//     } else {
//         let last = arrayToShow.pop();
//         let str = arrayToShow.join(', ');
//         let res = str + ' и ' + last;
//         return res; 
//     }
// }
// let a = new Array('Текст');
// let b = new Array('день', 'ночь');
// let c = new Array('зима', 'весна', 'лета', 'осень');

// alert(showArrayContent(a)); // Выводим содержимое массивов,
// alert(showArrayContent(b)); // используя созданную выше функцию.
// alert(showArrayContent(c));


// function Expression

// let sum1 = function(a, b){  
//     return a + b;
// }

// alert(sum1(2, 3));


// Immediately Invoken Function Expression (IIFE) - самовызывающаяся функция (анонимная функция)

// (function(){
//     alert('Привет мир')
// }());

// (function(n){
//     alert(n * n);
// })(4)


// Arrow Function

// // let test = (a, b, c) => a + b + c; 
// let test = (a, b, c) => {
//     let res = a + b + c;
//     return res;
// }

// alert(test(10, 20, 30));


// let hello = () => alert('hello');
// hello();

// let hello = n => alert('hello, ' + n);
// hello('Igor');



// document.writeln(Math.floor(7.9) + '<br>');  // округление вниз
// document.writeln(Math.ceil(7.1) + '<br>');  // округление вверх
// document.writeln(Math.round(7.1) + '<br>');  // по законам математики


// (function(min, max){
//     document.writeln(Math.floor(Math.random() * (max - min) + min) + '<br>');  // по умолчанию random случайное число от 0 до 1(не включая)
// })(2, 9);

// document.writeln(Math.floor(Math.random() * 9)+ '<br>');  // от 0 до 9
// document.writeln(Math.floor(Math.random() * 7 + 2)+ '<br>');  // от 2 до 9
// document.writeln(Math.floor(Math.random() * 8 + 7) + '<br>'); // от 7 до 15


// let randMas = ["Цикл", "Массив", "Условие", "Функция"];
// document.writeln(pickRandom(randMas))

// function pickRandom(mas){
//     return mas[parseInt(Math.random() * mas.length)];
// }


// области видимости

// let j = 2;  // глобальная

// if(true){
//     let i = 1;  // локальная
//     console.log(j);
// }

// console.log(i)

// let j = 2;

// if(true){
//     j = 1; 
// }

// console.log(j)

// let j = 2;

// function ch(){
//     j = 1; 
// }

// ch()
// console.log(j)



// document.writeln('<div id="block"></div>');
// let id = document.getElementById("block");

// id.style.width = '100px';
// id.style.height = '100px';
// // id.style.background = 'rgb(255, 0, 0)';

// let createColor = () => {
//     let r = Math.floor(Math.random() * 256);
//     let g = Math.floor(Math.random() * 256);
//     let b = Math.floor(Math.random() * 256);
//     // id.style.background = 'rgb(' + r + ', ' + g + ', ' + b + ')';
//     id.style.background = `rgb(${r}, ${g}, ${b})`;
// }

// createColor();


// function test(a, b){
//     alert('a='+5+', b='+b);
// }

// test(1);
// test(1, 2);
// test(1, 2, 3);

// function test(){
//     console.log(arguments[0]);
//     console.log(arguments[1]);
//     console.log(arguments[2]);
//     console.log(arguments[3]);
// }

// test(1, 2, 3);


// function sum(){
//     let res = 0;
//     for(let i = 0; i < arguments.length; i++){
//         res += arguments[i];
//     }
//     let a = 'hello';
//     return [res, a];
// }

// document.writeln(sum() + '</br>');
// document.writeln(sum(1) + '</br>');
// document.writeln(sum(1, 2) + '</br>');
// document.writeln(sum(1, 2, 3) + '</br>');
// document.writeln(sum(1, 2, 3, 4) + '</br>');
// document.writeln(sum(1, 2, 3, 4, 5) + '</br>');


// function hello(name='незнакомец'){
//     // name = name || 'незнакомец';
//     document.writeln('Привет, ' + name + '! <br>');
// }

// hello('Катя');
// hello();


// function square(width=300, height=200, fon='green'){
//     document.writeln('<div id="shape"></div>');
//     let div = document.querySelector('#shape');

//     div.style.background = fon;
//     div.style.width = width + 'px';
//     div.style.height = height + 'px';
// }

// square(350, 450, 'gold');
// square(150, 100);
// square(150);
// square();


// function hello(){
//     alert("Привет");
// }

// alert(hello);


// let str = 'I\"m a JavaScript \'programmer\''

// document.writeln(str + '<br>');
// document.writeln(str.length + '<br>');
// document.writeln(str [2] + '<br>');

// // str[2] = 'y'
// str = str[2] + 'y';
// document.writeln(str + '<br>');


// let s = "абббабввбабвбвббабвббабв";
// counterLetters(s);

// function counterLetters(str){
//     let letters = ["а", "б", "в"];
//     for(let i = 0; i < letters.length; i++){
//         let count = 0;
//         for(let j = 0; j < str.length; j++){
//             if(str[j] == letters[i]){
//                 count++;
//             }
//         }
//         document.writeln("Символ '" + letters[i] + "' встретился " + count + " раз<br>");
//     }
// }


// let str = "I\'m a JavaScript \"programmer\""
// document.writeln(str[6] + '<br>');
// document.writeln(str.charAt(6) + '<br>');

// document.writeln(str.toLowerCase() + '<br>');  //нижний регистр
// document.writeln(str.toUpperCase() + '<br>');  //верхний регистр
// document.writeln(str + '<br>');


// let n = prompt("Введите имя", "ниКиТа");
// alert(first(n));

// function first(str){
//     let firstLetter = str.charAt(0).toUpperCase();
//     for(let i = 1; i <str.length; i++){
//         firstLetter += str[i].toLowerCase();
//     }
//     return firstLetter;
// }


// let str = "I\'m a JavaScript \"programmer\"";
// let str1 = 'Я учу JavaScript. Мне нравится JavaScript.';
// str = str.concat(str1);
// document.writeln(str + '<br>');

// document.writeln(str.indexOf("JavaScript", 7) + '<br>');
// document.writeln(str.lastIndexOf("JavaScript") + '<br>');

// let email;
// do{
//     email = prompt('Введите email: ');
//     if(email.indexOf('@') == -1){
//         alert("Некорректно. Повторите операцию");
//         continue;
//     }
//     break;
// }while(true)

// alert("Спасибо за сотрудничество")

// document.writeln(str.split(".") + "<br>");
// console.log(str.split(".", 2))

// document.writeln(str.slice(0, 3) + '<br>');
// document.writeln(str.slice(3, 0) + '<br>');
// document.writeln(str.slice(-23, -10) + '<br>');
// document.writeln(str.substring(0, 3) + '<br>');
// document.writeln(str.substring(3, 0) + '<br>');
// document.writeln(str.substring(-10) + '<br>');


// let style = prompt('Введите свойство CSS', 'list-style-type');
// alert(replace(style));

// function replace(str){
//     let mas = str.split("-");  // ["background", "color"]
//     for(let i = 1; i < mas.length; i++){
//         mas[i] = mas[i].charAt(0).toUpperCase() + mas[i].slice(1);
//     }
//     return mas.join('');
// }


// function loadStr(){
//     alert('Страница была загружена');
// }

// let m = document.getElementById('mes');

// function over(){
//     m.style.color='red';
// }

// function out(){
//     m.style.color='blue';
// }

// function change(){
//     let id = document.getElementById('title');
//     id.style.color='blue';
// }

// function randomBg(){
//     document.body.style.background=`rgb(${rand()}, ${rand()}, ${rand()})` 
// }

// function rand(){
//     return Math.floor(Math.random()*256);
// }

// let image = document.getElementById('image')
// function on(){
//     image.src = 'night.png'
// }

// function off(){
//     image.src = 'day.png'
// }


// but.onclick = function(){
//     alert('спасибо')
// }


// function change(id){
//     id.innerHTML = 'Новый текст';
// }


// function setColor(elem){
//     document.body.style.background = elem.className
// }


// let el = document.querySelector('#but');

// el.addEventListener('click', function(){
//     el.innerHTML='Новый текст';
// });

// el.addEventListener('contextmenu', setColor)
    
// function setColor(){
//     el.style.color = 'green';
//     el.style.background = 'yellow'
// }


// document.addEventListener("mousemove", function(event){
//     let c = document.querySelector('#elem');
//     let x = event.clientX
//     let y = event.clientY
//     c.textContent = 'X = ' + x + ", Y = " + y;

//     c.addEventListener('dblclick', function(event){
//         event.target.style.background='red'
//     })
// })


// let el = document.querySelector('#but');

// el.addEventListener("click", handler);

// function handler(){
//     alert("Thanks")
//     el.removeEventListener("click", handler)
// }


// setTimeout(функция, задержка)

// setTimeout('alert("Текст")', 3000);

// setTimeout(hello, 1000, 'Привет', 'Друг');

// function hello(h, n){
//     alert(h + ", " + n + '!');
// }


// document.writeln("<div id='dt'>Создание анимированного текста</div>");

// let id = document.querySelector("#dt");  // "<div id='dt'>Создание анимированного текста</div>"
// let text = document.querySelector("#dt").innerHTML;  //Создание анимированного текста

// let i = 0;

// window.addEventListener('load', animText);

// function animText(){
//     id.innerHTML = text.substring(0, i);
//     i++;
//     if(i > text.length){
//         i = 0;
//     }
//     setTimeout(animText, 50)
// }


// let d = new Date();
// document.writeln(d + '<br>');
// document.writeln(d.toDateString() + '<br>');
// document.writeln(d.getFullYear() + '<br>');  // 2025
// document.writeln(d.getMonth() + '<br>');  // 7, от 0 по 11
// document.writeln(d.getDate() + '<br>');  // 1
// document.writeln(d.getDay() + '<br>');  // 5, от 0 - воскресенье, 6 - суббота


// let mounth = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"];
// let day = ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"];

// let d = new Date();
// let fullDate = 'Сегодня: ' + d.getDate() + ' ' + mounth[d.getMonth()] + ' ' + d.getFullYear() + ' год, ' + day[d.getDay()];

// document.writeln(fullDate);



// setInterval(функция, интервал)

// document.writeln("<input type='button' value='Start / Stop'>");
// document.querySelector("input").addEventListener('click', startStop);

// let act, run;
// function startStop(){
//     if(!run){
//     act = setInterval(setColor, 1000);
//     // run = true;
//     }else{
//     clearInterval(act);
//     // run = false;
//     }
//     run = !run;
// }

// function setColor(){
//     let x = document.body;
//     x.style.background = x.style.background == "yellow" ? "orange" : "yellow"
// }



// document.writeln("<div id='text'>Текущее время</div>");

// window.addEventListener('load', () => setInterval(time, 1000));

// function time(){
//     let d = new Date();
//     let hour = d.getHours();
//     let min = d.getMinutes();
//     let sec = d.getSeconds();

//     if(hour<10){
//         hour = '0' + hour;
//     }
//     if(min<10){
//         min = '0' + min;
//     }
//     if(sec<10){
//         sec = '0' + sec;
//     }

//     let times = hour + ":" + min + ":" + sec;
//     document.querySelector('#text').innerHTML = times;
// }



// let imgTime = ['c0.gif', 'c1.gif', 'c2.gif', 'c3.gif', 'c4.gif', 'c5.gif', 'c6.gif', 'c7.gif', 'c8.gif', 'c9.gif'];

// let t = document.querySelectorAll('#clock img');

// clock();

// function clock(){
//     let time =  new Date();
//     let hours = time.getHours();
//     let mins = time.getMinutes();
//     let seconds = time.getSeconds();

//     getImg(hours, mins, seconds);
//     setTimeout(clock, 1000)
// }

// function getImg(h, m, s){  // 11 / 10 => 1.1
//     t[0].src = imgTime[parseInt(h / 10)]
//     t[1].src = imgTime[h % 10]
//     t[3].src = imgTime[Math.floor(m / 10)]
//     t[4].src = imgTime[m % 10]
//     t[6].src = imgTime[parseInt(s / 10)]
//     t[7].src = imgTime[s % 10]
// }



// document.writeln(`
//     <input type='text' size='4' id='timer' value='0.0'>
//     <input type='button' value='Start / Stop'>
//     <input type='button' value='Clear'>    
// `);

// document.querySelector("input[value='Start / Stop']").addEventListener('click', startTimer);

// document.querySelector("input[value='Clear']").addEventListener('click', resetTime)

// let id, flag;

// function startTimer(){
//     if(!flag){
//         id = setInterval(incTimer, 100);
//     }else{
//         clearInterval(id);
//     }
//     flag = !flag;
// }

// let tsec = 0;
// function incTimer(){
//     tsec++;
//     let t = tsec/10.0;
//     if(tsec%10==0){
//         t+='.0';
//     }
//     document.getElementById('timer').value = t;
// }

// function resetTime(){
//     document.getElementById('timer').value = '0.0';
//     tsec = 0;
// }



// let a = document.querySelector("#cl");
// a.addEventListener('click', myMove);

// function myMove(){
//     let elem = document.getElementById('animate');
//     let pos = 0;
//     let id = setInterval(frame, 5);

//     function frame(){
//         // a.style.visibility='hidden';
//         if(pos == 350){
//             // a.style.visibility='visible';
//             a.addEventListener('click', myMove);
//             clearInterval(id)
//         }else{
//             a.removeEventListener('click', myMove)
//             pos++;
//             elem.style.top = pos + 'px';
//             elem.style.left = pos + 'px';
//         }
//     }
// }



// document.image.border = 1;
// document.writeln('<br>Ширина изображения: ' + document.image.width + '<br>');
// document.writeln('<br>Высота изображения: ' + document.image.height + '<br>');

// document.image.src='blue_star.png'



// let array = new Array('2.jpg', '3.jpg', '4.jpg');
// document.writeln('<input type="button" value="<" name="left">');

// document.writeln("<img src='" + array[0] + "'>")

// document.writeln('<input type="button" value=">" name="right">');

// document.getElementsByName('right')[0].addEventListener('click', arrowRight);
// document.getElementsByName('left')[0].addEventListener('click', arrowLeft);

// let image = document.querySelector('img');
// let i = 0;

// function arrowRight(){
//     i++
//     if(i == array.length){
//         i = 0;
//     }
//     image.src = array[i];
// }

// function arrowLeft(){
//     i--;
//     if(i < 0){
//         i = array.length - 1;
//     }
//     image.src = array[i];
// }



// let a = 5;
// let b = 10;
// let c;

// console.log('a = ', a);
// console.log('b = ', b);

// c = a;  // c = 5
// a = b;  // a = 10
// b = c;  // b = 5

// console.log('a = ', a);
// console.log('b = ', b);


// document.writeln("<input type='number' min='1' max='3'>");
// document.writeln("<input type='button' class='btn' value='кнопка'>");

// let btn = document.querySelector('.btn');

// btn.addEventListener('click', function(){
//     let el = document.querySelector('input').value;
//     console.log(el)
// })



// alert(document.documentElement.innerHTML);
// alert(document.body.innerHTML);

// let myTitle = document.querySelector('h1').innerHTML;
// console.log(myTitle);

// // let par = document.querySelector('p').firstChild.nodeValue;
// // let par = document.querySelector('p').childNodes[0].nodeValue;
// // let par = document.querySelector('p').nodeName;
// let par = document.querySelector('p').firstChild.nodeType;
// console.log(par)


// let elem = document.querySelector('#root');
// let tag = document.createElement("p");  // <p></p>
// let node = document.createTextNode("Новый текст!!!"); // Новый текст!!!
// tag.append(node);  // <p>Новый текст!!!</p>
// elem.append(tag); // добавляет новый элемент последним дочерним элементом внутри родительского
// elem.prepend(tag); // добавляет новый элемент первым дочерним элементом внутри родительского
// elem.before(tag);  // добавляет новый элемент до выбранного id
// elem.after(tag);  // добавляет новый элемент после выбранного id
// elem.replaceWith(tag);  //заменяет новым элементом выбранный id 



// let list = document.querySelector('ul');
// let newItem = document.createElement('li');
// newItem.innerHTML = 'Новый <i>элемент списка</i>';
// list.append(newItem);


// document.querySelector('#move').addEventListener('click', change);
// document.querySelector('#add').addEventListener('click', add);
// let i = 1;

// function add(){
//     let elem = document.createElement('li');
//     elem.innerHTML = 'Water ' + i;
//     document.querySelector('#list2').append(elem);
//     // list2.append(elem)
//     i++;
// }

// function change(){
//     let elem = document.querySelector('#list2').lastChild;
//     document.querySelector('#list1').append(elem);
// }



// let div = document.querySelector('#root');
// div.insertAdjacentHTML('beforebegin', '<p>До выбранного элемента</p>');
// div.insertAdjacentHTML('afterend', '<p>после выбранного элемента</p>');
// div.insertAdjacentHTML('afterbegin', '<p>Первым внутри выбранного выбранного элемента</p>')
// div.insertAdjacentHTML('beforeend', '<p>Последним внутри выбранного выбранного элемента</p>')

// let first = document.querySelector('#p1');
// // first.remove()
// let second = document.querySelector('#p2');
// second.after(first)



// let ul = document.querySelector('ul');
// let clone = ul.cloneNode(true);

// clone.querySelector('li').innerHTML = 'Начало мклонируемых элментов';
// ul.after(clone);


// let list = document.querySelector('.list');
// list.insertAdjacentHTML('beforebegin', '<h2>Список <h2><hr>');
// let list_inner = document.querySelector('h2');
// list_inner.insertAdjacentText('beforeend', 'планет');
// list.insertAdjacentHTML('afterend', '<hr>');
// let hr = document.querySelectorAll('hr')[1];
// let h4 = document.createElement('h4');
// h4.innerHTML = 'Конец списка';
// hr.insertAdjacentElement('afterend', h4);

// let idRemove = setInterval(function(){
//     let li = document.querySelector('.list > li:last-child');
//     if(li === null){
//         clearInterval(idRemove);
//         // alert('Список удален')
//         list.insertAdjacentHTML('afterbegin', '<li>Список удален</li>')
//     }else{
//         li.remove(); 
//     }
    
// }, 500);



// let div = document.querySelector('div');
// div.className = 'alert';
// let activeDiv = document.querySelector('.active');
// activeDiv.classList.add('hidden');
// // activeDiv.classList.remove('hidden');
// activeDiv.classList.toggle('hidden');
// activeDiv.classList.replace('active', 'alert');



// let frogImg = document.querySelector('#greenFrog');
// console.log(frogImg.id);
// console.log(frogImg.className);
// console.log(frogImg.alt);
// console.log(frogImg.title);
// console.log(frogImg.src);

// frogImg.title = 'Новый текст подсказки';
// console.log(frogImg.getAttribute('src'));
// console.log(frogImg.getAttribute('data-frog'));

// frogImg.setAttribute('src', '4.jpg');
// frogImg.removeAttribute('src');

// console.log(frogImg.hasAttribute('src'));



// document.form1.style.background = 'silver';
// document.forms[0].style.padding = '16px';
// document.forms['form1'].style.margin = '20px';
// document.forms.form1.style.border = '2px dotted gray';

// document.form1.name1.style.color = 'blue';
// document.form1['name1'].style.background = 'aqua';

// let but = document.querySelector('button');
// let txt = document.querySelector('#text1');

// but.addEventListener('click', content);

// function content(){
//     // alert(txt.value);
//     console.log(txt.value);
    
// }



// let input = document.querySelectorAll('input');
// let form1 = document.forms.form1;
// // console.log(input.length);
// // console.log(form1.length);

// for(let i = 0; i < form1.length; i++){
//     input[i].addEventListener('click', checkAll);
// }

// let num;
// function checkAll(){
//     num = 0;
//     for(let i = 0; i < form1.length; i++){
//         if(input[i].checked && input[i].type == 'checkbox'){
//             num++;
//         }
//     }
//     if(num == 3){
//         for(let i = 0; i < form1.length; i++){
//             if(!input[i].checked && input[i].type == 'checkbox'){
//                 input[i].disabled = true
//             }
//         }
//     }else{
//         for(let i = 0; i < form1.length; i++){
//             input[i].disabled = false
//         }
//     }
//     console.log(num)
// }

// let input = document.querySelectorAll('input[type="checkbox"]');
// let form1 = document.forms.form1;
// // console.log(input.length);
// // console.log(form1.length);

// for(let i = 0; i < input.length; i++){
//     input[i].addEventListener('click', checkAll);
// }

// let num;
// function checkAll(){
//     num = 0;
//     for(let i = 0; i < input.length; i++){
//         if(input[i].checked){
//             num++;
//         }
//     }
//     if(num == 3){
//         for(let i = 0; i < input.length; i++){
//             if(!input[i].checked){
//                 input[i].disabled = true
//             }
//         }
//     }else{
//         for(let i = 0; i < input.length; i++){
//             input[i].disabled = false
//         }
//     }
//     console.log(num)
// }



// let choose = document.querySelector('input[type="button"]');
// choose.addEventListener('click', chooseColor);

// function chooseColor(){
//     let f = document.form3.radio2;

//     // console.log(f.length);

//     // for(let i = 0; i < f.length; i++){
//     //     if(f[i].checked){
//     //         document.body.style.background = f[i].value;
//     //     }
//     // }
//     document.body.style.background = f.value;

// }



// Свойства select:
/* 
select.options - коллекция из подэлементов <option> (массив)
select.value - значение выбранного в данный момент <option>
select.selectedIndex - номер выбранного <option> (index)
*/

// let city = document.querySelector('#city');
// city.addEventListener('change', setImage);

// function setImage(){
//     let citis = city.selectedIndex;
//     // console.log(citis);  // Индекс
//     let options = city.options
//     // console.log(options);  // массив
//     let code = options[citis].value
//     // console.log(code);
    
//     let div = document.querySelector('#image');
//     div.innerHTML = '<img src="img/'+ code +'.png">'
// }



// let gas = document.querySelectorAll('.petrol');
// for(let i = 0; i < gas.length; i++){
//     gas[i].addEventListener('click', function(){
//         let gallons = document.querySelector('.gallons').value;
//         let amount = gas[i].getAttribute('data-price');
//         let res = gallons * amount;
//         let sum = document.querySelector('.sum');
//         sum.innerHTML = res;
//     });
// }



// let reg = document.querySelector('.register');
// reg.addEventListener('submit', function(){
//     let login = reg.login.value;
//     let psd1 = reg.password1.value;
//     let psd2 = reg.password2.value;
    
//     if(!(login && psd1 && psd2)){
//         alert('Все поля должны быть заполненны');
//     }
//     if(psd1 != psd2){
//         alert('Пароль не совпадает')
//     }
//     if(psd1.length < 6){
//         alert('Слишком короткий пароль')
//     }
// })



/* 
search() - возвращает позицию, на которой регулярное выражение совпадает с вызывающей сторой. Возвращает -1, если совпадение не найдено

match() - получить все совпадения с регулярным выражением

replace() - поиск и замена

split() - делит строку на массив, разбивая ее по указанной подстроке

test() - выполняет поиск совпадения регулярного выражения с подстрокой и возвращает true либо false
*/

// let regexp = new RegExp('шаблон');
// let regexp1 = /шаблон/;
// let regexp2 = /шаблон/gmi;

// let str = 'Я ищу совпадения в 2025 году. Hello. Ёжик 1234_56789';
// let exp = /ищу/g;
// document.writeln(str + '<br>');
// document.writeln(str.search(exp) + '<br>');
// document.writeln(str.match(exp) + '<br>');
// document.writeln(exp.test(str) + '<br>');

// [...] - искать один из заданных символов, но только один раз
// let exp = /[0256]/g;
// document.writeln(str.match(exp) + '<br>');

/* Флаги
g (global) - глобальный поиск
i (ignoreCase) - регистронезависимый поиск
m (multiline) - многострочный поиск
*/

// let exp = /[я]/gi;
// document.writeln(str.match(exp) + '<br>');

/* Диапазон
[0-9] - одна любая цифра ([3-7])
[A-Z] - заглавные буквы
[a-z] - строчные буквы
[A-Za-z]
[А-ЯЁ] - заглавные буквы
[а-яё] - строчные буквы
[А-яЁё]
*/

// let exp = /[0-9]/g;
// document.writeln(str.match(exp) + '<br>');

// [^abc] - исключающий диапазон, ни один из указанных символов
// let exp = /[^0-9]/g;
// document.writeln(str.match(exp) + '<br>');

/* 
{3} - кол-во символов идущих подряд
{1,} - от 1 до любого кол-ва повторений
{2,5} - от 2 до 5 повторений
*/
// let exp = /[0-9]{2,3}/g;
// document.writeln(str.match(exp) + '<br>');


// let html = `
//     <table>
//         <tr>
//             <td bgcolor='#CCC'>
//                 <img src='222.png'>
//             </td>
//             <td bgcolor='#003399'>
//                 <img src='1f3.png'>
//             </td>
//             <td bgcolor='#00ccdd'>
//                 <img src='FFF.png'>
//             </td>
//         </tr>
//     </table>
// `;

// let reg = /#([0-9a-f]{3}){1,2}/gi;
// document.writeln(html.match(reg) + '<br>');

/* 
\d (digit) - любая цифра
\s (space) - пробельный символ, включая табуляции и перевод строки
\w (word) - любая цифра, буква(только английские, регистронезависимый) или символ подчеркивания
*/
/* 
\D - всё кроме цифр
\S - не пробел, включая табуляцию и перевод строки
\W - все кроме цифр, букв(англ) или сомволоы подчеркивания
*/
/* 
^ - начало строки (перед последовотельностью ничего не должно быть)
$ - конец строки (после последовательности ничего не должно быть)
*/

// str = '909'
// let exp = /^\d{3}$/;
// document.writeln(str.match(exp) + '<br>');

// точка - один любой символ

// let exp = /\d.\d/g;
// document.writeln(str.match(exp) + '<br>');

/* 
+ - от 1 до любого кол-ва повторений {1,}
* - от 0 до любого кол-ва повторений {0,}
? - от 0 до 1 повторения {0,1}
*/
// let exp = /\d?/g;
// document.writeln(str.match(exp) + '<br>');


// let html = `
//     <p>Text
//         <img src='222.jpg'>
//         <img src='dsdad222.png'>
//         <span>else. New Text</span>
//         <img src='RRR.jpeg'>
//         <img src='uio.gif'>
//     </p>
// `
// let exp = /(\w+)\.(gif|jpg|jpeg|png|bmp)/g;
// document.writeln(html.match(exp) + '<br>');


// document.writeln('aaa'.replace('a', 'b') + '<br>');
// document.writeln('aaa'.replace(/a/g, 'b') + '<br>');

// let text = 'I kill you black dog';
// document.writeln(text + '<br>');
// let exp = /(book|kill|black)/ig;
// text = text.replace(exp, '***');
// document.writeln('<p>' + text + '</p>');

// let text = 'John Smith';
// // let exp = /(John) Smith/;
// // document.writeln(text.match(exp) + '<br>');
// let exp = /(\w+)\s(\w+)/;
// document.writeln(text.replace(exp, '$2 $1') + '<br>');

// let text = 'red color: #F00 and green: #090';
// document.writeln(text + '<br>');
// let exp = /(#[a-f0-9]{3})/ig;
// text = text.replace(exp, '<span style="color: $1">$1</span>');
// document.writeln('<p>' + text + '</p>');

// let text = 'I like yandex.ru';
// document.writeln(text + '<br>');
// let exp = /(([a-z0-9-]{2,}\.)+[a-z]{2,4})/i;
// text = text.replace(exp, '<a href="https://$1">$1</a>');
// document.writeln('<p>' + text + '</p>');

// let str = "+7 (999) 123-45-78    ";
// str = str.replace(/[\s()-]/g, '');
// alert(">" + str + "<")

// let str = "+7 (999) 123 45 78"
// let str = "01-09-2025 25.09.2024 12/03/2003"
// let re = str.split(/[-./\s]/);
// document.writeln(re + "<br>");
// console.log(re);



// let car = new Object();
// let car1 = {};

// let car = new Object();
// car[10] = "BMW";
// car[true] = "false";
// car[[true, false]] = "all";
// car['color'] = 'white';
// car['color brand'] = 'white';
// document.writeln(car['color brand'] + ' ' + car[10]);
// console.log(car);

// let car = new Object();
// car.type = 'BMW';
// car.color = 'white';
// document.writeln(car.color + ' ' + car.type);
// console.log(car);


// let menu1 = {};
// menu1.width = 300;
// menu1.height = 200;
// menu1.title = 'Menu';
// document.writeln(menu1.title + ': ' + menu1.width + ' x ' + menu1.height + '<br>')
// console.log(menu1);


// let menu = {
//     width: 300,
//     height: 200,
//     title: 'Menu'
// };
// // delete(menu.width);
// delete menu.width;
// // document.writeln(menu.title + ': ' + menu.width + ' x ' + menu.height)
// let count = 0;
// menu.age = 25;
// for(let i in menu){
//     document.writeln(i + ': ' + menu[i] + '<br>');
//     count++;
// }
// console.log(menu);
// console.log('count:', count);
// // document.writeln('Имена ключей: ' + Object.keys(menu));
// // document.writeln('<br>Всего ключей: ' + Object.keys(menu).length);

// // Object.keys(menu).forEach(function(key){
// //     document.writeln('<br>' + key + ': ' + menu[key]);
// // });
// Object.keys(menu).forEach((key) => document.writeln('<br>' + key + ': ' + menu[key]));


// let car = {
//     name: 'Volvo',
//     year: 2019
// };
// console.log(car);


// let obj = {
//     name: 'Гомер',
//     colors: {
//         first: 'green',
//         second: "blue"
//     },
//     color: [
//         'black',
//         'white',
//         'red',
//         'blue'
//     ],
//     hello: function(){
//         document.writeln('Привет');
//     }
// }
// let mas2 = Object.keys(obj.colors).map(function(elem){
//     return elem + ': ' + obj.colors[elem] + '<br>';
// });
// document.writeln('<br>' + mas2 + '<br>');
// console.log(mas2);

// let mas = obj.color.map(function(elem, index, all){
//     return "<br>" + elem + ' ' + index + ' массив: ' + all;
// });
// document.writeln('<br>' + mas + '<br>')

// let mas1 =obj.color.map(elem => elem.toUpperCase());
// document.writeln('<br>' + mas1 + '<br>')

// let fil = obj.color.filter(function(elem){
//     return elem.length < 5;
// });
// document.writeln('<br>' + fil + '<br>')

// document.writeln(obj.name + ' ' + obj.colors.first + ' ' + obj.color[1]);
// obj.hello()


// let calc = {
//     num1: 5,
//     num2: 10,
//     calculate: function(){
//         this.result = this.num1 * this.num2;
//         // calc.result = calc.num1 * calc.num2;
//     }
// }
// calc.calculate();
// document.writeln(calc.result + '<br>');
// document.writeln(calc.num1);


// let x = 15, y = 10;
// // let coords = {
// //     x: x,
// //     y: y,
// //     calcSq: function(){
// //         document.writeln(this.x * this.y);
// //     }
// // };
// let coords = {
//     x, y,
//     calcSq(){
//         document.writeln(this.x * this.y);
//     }
// };
// coords.calcSq()




// Функция конструтор
// function Car(name, year){
//     this.name = name;
//     this.year = year;
// }

// Car.prototype.getAge = function(){
//     return new Date().getFullYear() - this.year;
// }

// Car.prototype.color = 'black';

// let ford = new Car('Ford', 2019);
// console.log(ford);
// console.log(ford.getAge());
// ford.color = 'red';
// console.log(ford.color);

// let bmw = new Car('BMW', 2017);
// console.log(bmw);
// console.log(bmw.getAge());
// console.log(bmw.color);


// function User(pName, pAge){
//     this.name = pName,
//     this.age = pAge;

//     this.displayInfo = function(){
//         document.writeln('Имя: ' + this.name + '; возраст: ' + this.age + '<br>');
//     }
// }
// let tom = new User("Tom", 26);
// tom.displayInfo()













































































































