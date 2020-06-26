
const $the_board = $("#the_board");
const $Guess_Form = $('#Guess-Form');
const $score = $("#score");
const $message = $("#message");
const $game_over = $("#game_over");
let points = 0;


async function checkWord(){
    const $guess = $('#Guess');
    const unwrapped_guess = $guess.get(0).value;
    console.log(unwrapped_guess);
    const result = await axios.get('/check', {params : {Guess : unwrapped_guess }});
    console.log(result);
    if( result.data.res != 'ok'){
        $message.get(0).innerHTML = result.data.msg;
    }
    else{
        if( Number.isInteger(result.data.points)){
            points += parseInt(result.data.points);
        }
        $score.get(0).innerHTML = points;
        $message.get(0).innerHTML = result.data.msg;
    }
}

$Guess_Form.on('submit', function(e){
    e.preventDefault();
    checkWord();
})
