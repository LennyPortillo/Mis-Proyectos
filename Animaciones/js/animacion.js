document.getElementById('btn_girar').onclick = girar;
document.getElementById('btn_parar').onclick = parar;

function girar(){
    document.getElementById('cubo').style.animationPlayState='running';


}

function parar(){
    document.getElementById('cubo').style.animationPlayState='paused'
}