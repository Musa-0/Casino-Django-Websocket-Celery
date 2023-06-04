var error = document.querySelector('#error_form');
var statesStavka = document.querySelector('#states_stavka');


var socket_notification = new WebSocket('ws://' + window.location.host + '/ws/notification_connection/');
socket_notification.onmessage = function(e)
{
    var data = JSON.parse(e.data);
    console.log(data)
    if(data.event=="Send_notification"){
        if(data.message=="succses"){
            statesStavka.innerHTML = "Ставка успешно сделана"
            statesStavka.style.color = "green"
        }
        if(data.message=="stavka_alredy_create"){
            statesStavka.innerHTML = "Ставка уже сделана"
            statesStavka.style.color = "white"
        }
        if(data.message=="you_havent_money"){
            error.innerHTML = "У вас недостаточно средств"
            error.style.color = "red"
        }


    }
}

document.querySelector('#btn').onclick = function(e) {
    var summ_input = document.querySelector('#input').value;
    var color = document.getElementsByName('color');
    error.innerHTML = ''
    statesStavka.innerHTML = ''
    if(color[0].checked || color[1].checked){

        if (color[0].checked) {color = color[0].value}
        else{color = color[1].value}
        if(summ_input!=""){
            if(Number(summ_input)>=25){
                socket_notification.send(JSON.stringify({
                    'quantity': summ_input,
                    'color': color}));}
            else{
                error.innerHTML = "вы ввели сумму меньше 25р"
                error.style.color = "red"}
        }
        else{
        error.innerHTML = "вы не ввели сумму"
        error.style.color = "red"}
    }
    else{
        error.innerHTML = "вы не выбрали кнопку"
        error.style.color = "red"}
    }


