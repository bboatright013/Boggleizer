
const $Timer = $("#Timer");
count = 0;



$(document).ready(function(){
    console.log("timer on");
    let intervalID = setInterval(function(){
        count += 1;
        console.log(count);
        $Timer.get(0).innerHTML = count;
    }, 1000)
    setTimeout( async function(){
        console.log("timer over");
        clearInterval(intervalID);
        $Guess_Form.css("display", "none");
        $game_over.css("display", "block");
        await postScore();
    }, 60000)
});
 



async function postScore(){
    let resp = await axios.get('/post-score')
    console.log(resp);
    
}