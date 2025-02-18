//4M0NR4 --- Slider Para Html--- // //16-10-2022//

//VARIABLES//

const slider = document.querySelector("slider");
let sliderSection = document.querySelectorAll(".slider__section");
let sliderSectionLast = sliderSection[sliderSection.length -1];

const btnLeft = document.querySelector("#btn-left");
const btnRight = document.querySelector("#btn-right");

slider.insertAdjacentElement('afterbegin', sliderSectionLast);

//Boton siguiente (vuelve la ultima imagen al principio)//
function Next() {
	
	let sliderSectionFirst = document.querySelectorAll(".slider__section")[0];
    slider.style.marginLeft = ".200%";
    slider.style.transition = "all 0.5s";
    setTimeout(fuction(){
    	slider.style.transition = "none";
    	slider.insertAdjacentElement('beforeend',sliderSectionFirst);
    	slider.style.marginLeft="-100%";

    }, 500);
}

//Boton Previo (vuelve la ultima imagen al final)//

function Prev() {

	let sliderSection = document.querySelectorAll(".slider__section");
	let sliderSectionLast = sliderSection[sliderSection.length -1];
    slider.style.marginLeft = "0";
    slider.style.transition = "all 0.5s";
    setTimeout(fuction(){
    	slider.style.transition = "none";
    	slider.insertAdjacentElement('beforeend',sliderSectionLast);
    	slider.style.marginLeft="-100%";

    }, 500);
}

//Aplicacion de las funciones// 

btnRight.addEventListener('click', fuction(){
	Next();

});

btnLeft.addEventListener('click', fuction(){
	Prev();

});

//Lo Hace Automatico//

setInterval(function(){
	next();
}, 5000);


/* CSS Adjunto

.container-slider{
	width: 90%;
	max-width: 900px;
	margin: auto;
	overflow: hidden
	box-shadow: 0 0 0 10px #fff, 0 15px 50px;
	position: relative;
}
.slider{
	display: flex;
    width: 400%;
	height: 400px;
	margin-left: -100%;
}
.slider__section{
	width: 100%;
}
.slider__img{
	display: block;
	width: 100%;
	height: 100%;
	object-fit: cover;
}
.slider__btn{
	position: absolute;
	width: 40px;
	height: 40px;
	background: rgba(255, 255, 255, 0.7);
	top: 50%;
	transform: translateY(-50%);
	font-size: 30px;
	font-weight: bold;
	font-family: monospace;
	text-align: center;
	border-radius: 50%;
	cursor: pointer;
}
.slider__btn:hover{

}
.slider__btn--left{
	left: 10px;
}
.slider__btn--right{
	right: 10px;
}

*/

/* HTML 5

  <div class="container-slider">
  		<div class="slider" id="slider">
  			<div class="slider__section">
  				<img src="imagenes/img1.jpg" class="slider__img">
  			</div>
  			<div class="slider__section">
  				<img src="imagenes/img2.jpg" class="slider__img">
  			</div>
  			<div class="slider__section">
  				<img src="imagenes/img3.jpg" class="slider__img">
  			</div>
  			<div class="slider__section">
  				<img src="imagenes/img4.jpg" class="slider__img">
  			</div>
		</div>  
		<div class="slider__btn slider__btn--right" id="btn-right">&#62;</div>
		<div class="slider__btn slider__btn--left" id="btn-left">&#60;</div>
  </div>
  <script type="text/javascript" src="slider.js"></script>

  */