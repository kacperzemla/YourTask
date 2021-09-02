const user = document.querySelector('.profile__header__icon')
const menu = document.querySelector('.menu')
const arrow = document.querySelector('.arrow-img')

user.addEventListener('click', () => {
    menu.classList.toggle('active');
    arrow.style.transform = "rotate(180deg)";
    if(!menu.classList.contains('active')){
        arrow.style.transform = "rotate(0deg)";
    }
})