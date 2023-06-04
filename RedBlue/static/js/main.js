var error = document.querySelector('#error_form');
var statesStavka = document.querySelector('#states_stavka');
var radio_blue = document.getElementById("color_blue");
var radio_red = document.getElementById("color_red");

//таймер
var timeMinuts = document.getElementById("minuts"); // Берём блок для показа времени
var timeSeconds = document.getElementById("seconds");
var timeMinut = 0;//document.getElementById("times").innerHTML;
time_get();
setInterval(function () {
    seconds = timeMinut%60 // Получаем секунды
    minutes = timeMinut/60%60 // Получаем минуты
    // Условие если время закончилось то...
    if (timeMinut > 0) {
        // Таймер удаляется
        //clearInterval(timer);
        --timeMinut; // Уменьшаем таймер

    }
    if(seconds<0){
        seconds=0
    }
    // Создаём строку с выводом времени
    timeMinuts.innerHTML = `0${Math.trunc(minutes)}`;
    if (seconds < 10){
        timeSeconds.innerHTML = `0${seconds}`;
    }
    else{
        timeSeconds.innerHTML = `${seconds}`;
    }
}, 1000)


function time_get(){
//загрузка времени
var xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", "http://"+ window.location.host + "/time/", true );
xmlHttp.responseType = 'json';
xmlHttp.send();

xmlHttp.onload = function() {
  if (xmlHttp.status != 200) {
    alert('Ошибка');}
  else {
    timeMinut = xmlHttp.response['time'];

  }
}
}

//websocket
var blue_button = document.getElementById("things__first");
var red_button = document.getElementById("things__second");
var wait = document.getElementById("for_ends_auction");

var socket = new WebSocket('ws://'+ window.location.host + '/ws/connection/');
socket.onmessage = function(e){
    var graph_data = JSON.parse(e.data);
    if(graph_data.event=="Send_winner_color"){
        if(graph_data.color=='r'){
            red_button.style.boxShadow = "0px 0px 24px 0px white";
            red_button.style.background = "red";
        }
        if(graph_data.color=='b'){
            blue_button.style.boxShadow = "0px 0px 24px 0px white";
            blue_button.style.background = "blue";
        }
    }
    if(graph_data.event=="State_auction"){
        if(graph_data.state=="start"){
            wait.innerHTML = 'ДО КОНЦА АУКЦИОНА'
            wait.style.padding = "0px 0px"

            error.innerHTML = ''
            statesStavka.innerHTML = ''
            red_button.style.boxShadow = "0px 0px 24px 0px red";
            red_button.style.background = "#b30000";
            blue_button.style.boxShadow = "0px 0px 24px 0px blue";
            blue_button.style.background = "#0000ad";
            radio_blue.checked = false
            radio_red.checked = false
            time_get();
        }
        if(graph_data.state=="wait"){
            wait.innerHTML = 'ОЖИДАЕМ...'
            wait.style.padding = "0px 66px"





        }

    }
}


