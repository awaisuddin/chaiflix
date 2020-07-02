var intervalo1;
var intervalo2;
var intervalo3;

function scrollDireita(){
  intervalo1 = setInterval(function(){ document.getElementById('scroller1').scrollLeft += 1 }  , 1);
  intervalo2 = setInterval(function(){ document.getElementById('scroller2').scrollLeft += 1 }  , 1);
  intervalo3 = setInterval(function(){ document.getElementById('scroller3').scrollLeft += 1 }  , 1);
};
function scrollEsquerda(){
  intervalo1 = setInterval(function(){ document.getElementById('scroller1').scrollLeft -= 1 }  , 1);
  intervalo2 = setInterval(function(){ document.getElementById('scroller2').scrollLeft -= 1 }  , 1);
  intervalo3 = setInterval(function(){ document.getElementById('scroller3').scrollLeft -= 1 }  , 1);
};

function clearScroll(){
  clearInterval(intervalo1);
  clearInterval(intervalo2);
  clearInterval(intervalo3);
  
};
