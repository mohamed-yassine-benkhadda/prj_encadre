
const nav = document.querySelector('nav');
const body = document.querySelector('body');
const main = document.querySelector('.main');
const sbuttons = document.querySelectorAll('.modalwin');
const settings_pan = document.querySelector('.settings_pan');
const close_img = document.querySelector('.close_img');
console.log(sbuttons);

for(let i = 0; i <sbuttons.length;i++) {
    sbuttons[i].addEventListener("click",function(){
        settings_pan.classList.remove("hidden");
    })
}

close_img.addEventListener("click",function(){
    settings_pan.classList.add("hidden");
})