/*const navSlide = () =>  {
    const burger =document.querySelector('.burger'); //.burgerdeki ilk elemanı alıp const tipindeki değişkene atıyor
    const nav=document.querySelector('.navbar-nav');
    const navLinks = document.querySelectorAll('.navbar-nav li');

    burger.addEventListener('click', ()=>{//addeventlistener birşeyler ekliyor işte mouseover veya click gibi komutlar verdikten sonra 
        //gerçekleşmesini istediğin olayın kodunu fonk için yazıyorsun
        nav.classList.toggle('active');
        navLinks.forEach((link, index )=>{
            if(link.style.animation){
                link.style.animation='';
            }
            else{
                link.style.animation =`navLinkFade 0.5s ease forwards ${index / 7+0.5}`;
            }
            
            
        
        });
    });


}

navSlide();*/
console.clear();
const navSlide= ()=> {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.navbar-nav');
    const navLinks=document.querySelectorAll('.navbar-nav li');
 //Toggle Nav
    
    burger.addEventListener('click', () =>{
        nav.classList.toggle('nav-active');

        navLinks.forEach((link,index) =>{
            if(link.style.animation) {
                link.style.animation=''
             } else {
               //Here there was a small mistake of using normal quotes '' and not back ticks ``.
               //Thats it!
                 link.style.animation=`navLinkFade 0.5s ease forwards ${index /7 + 0.5}s`;
             }
             console.log(index / 9);
         });

         burger.classList.toggle('toggle');
    });
  // Fixed an issue here from foreach to forEach.

}
navSlide();

//NOTES
/*console.log() is used to print something much the same as print function

example------------------------------------------------------------------------------------
define MY_FAV as a constant and give it the value 7
const MY_FAV = 7;

this will throw an error - Uncaught TypeError: Assignment to constant variable.
MY_FAV = 20;

// MY_FAV is 7
console.log('my favorite number is: ' + MY_FAV);

// trying to redeclare a constant throws an error
// Uncaught SyntaxError: Identifier 'MY_FAV' has already been declared
const MY_FAV = 20;

// the name MY_FAV is reserved for constant above, so this will fail too
var MY_FAV = 20;

// this throws an error too
let MY_FAV = 20;

---------------------------------------------------------------------------------------



*/