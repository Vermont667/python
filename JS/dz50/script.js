document.writeln('<div id="demonstration"></div>');
let div = document.querySelector('#demonstration');
div.innerHTML = 'Термоста́т — прибор для поддержания постоянной температуры. Поддержание температуры обеспечивается либо за счёт использования терморегуляторов, либо осуществлением фазового перехода (например, таяние льда). Для уменьшения потерь тепла или холода термостаты, как правило, теплоизолируют. Но не всегда. Широко известны автомобильные моторы, где летом нет никакой теплоизоляции и за счёт действия восковых термостатов поддерживается постоянная температура. Другим примером термостата, широко используемого в быту, является холодильник.'
div.style.backgroundColor = 'yellow';
div.style.color = 'black';
div.style.width = '256px';
div.style.height = '256px';
div.style.overflow = 'scroll';
div.style.outline = '1px dashed red';

div.className = 'resetFont';

let res = document.querySelector('.resetFont');
res.style.fontSize = '20px';
res.style.fontWeight = '400px';
res.style.textDecoration = 'underline';