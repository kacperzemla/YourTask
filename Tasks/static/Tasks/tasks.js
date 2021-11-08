const buttonAdd = document.querySelector(".tasks__add")
const formWrap = document.querySelector(".bg-modal")
const cancelButton = document.querySelector(".goals-add__button")
const form = document.querySelector(".goals-add")
const dateDay = document.querySelector(".tasks__header")
const fullDate = document.querySelector(".tasks__date")

const date = new Date();

Date.prototype.myDate = function(){
    let  weekdays = new Array(7);
    weekdays[0] = "Sunday";
    weekdays[1] = "Monday";
    weekdays[2] = "Tuesday";
    weekdays[3] = "Wednesday";
    weekdays[4] = "Thursday";
    weekdays[5] = "Friday";
    weekdays[6] = "Saturday";
    let day = weekdays[this.getDay()] ;
    return day;
};

dateDay.innerHTML = date.myDate();
fullDate.innerHTML = date.toLocaleDateString('de-DE')

buttonAdd.addEventListener("click", () => {
    formWrap.style.display = "flex";
})

cancelButton.addEventListener("click", () => {
    formWrap.style.display = "none";
})

formWrap.addEventListener('mouseup', function (e) {
    if (!form.contains(e.target)) {
        formWrap.style.display = 'none'
    }
})