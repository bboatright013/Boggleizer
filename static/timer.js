
const $Timer = $("#Timer");



$(document).ready(function(){
    count = 0;
    console.log("timer on");
    let intervalID = setInterval(function(){
        count += 1;
        console.log(count);
        $Timer.get(0).innerHTML = count;
    }, 1000)
    setTimeout(function(){
        console.log("timer over");
        clearInterval(intervalID);
        $Guess_Form.css("display", "none");
        $game_over.css("display", "block")
    }, 60000)

});