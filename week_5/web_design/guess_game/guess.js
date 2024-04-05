const randomnumber=math.floor(math.random() * 100) +1;
console.log(randomNumber)
let attempt=0;

function checkGuess(){
    const guess =parseInt(document.getElementById("guessField").value)
    attempt++;
    if(isNaN(guess) || guess<1|| guess>100)
    setmessage("Please enter a valid number between 1 and 100")
    return;
}
if(guess === randomnumber){
    setmessage("Congratulations!You have won")
    document.getElementById("guessField").disabled= true;
}elseif(guess < randomnumber);
    setmessage("Too low try again")
elseif(Guess > randomnumber);
    setmessages("Too high try again")

    