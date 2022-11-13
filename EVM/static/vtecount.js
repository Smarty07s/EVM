x=y=0

function disa(){
    document.getElementById('vote').disabled =true;
}
function ddusa() {
    document.getElementById('vote').disabled =false;   
}

function vte(){

    x = x+1
    document.getElementById('vtec').innerHTML = x;
    const disset = setTimeout(disa,5000);
    clearTimeout(disset);
    ddusa();


}