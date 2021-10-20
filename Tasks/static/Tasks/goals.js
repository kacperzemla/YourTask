const buttonAdd = document.querySelector("#mygoals__header__button")
const formWrap = document.querySelector(".bg-modal")
const cancelButton = document.querySelector(".goals-add__button")
const form = document.querySelector(".goals-add")
const goalsList = document.querySelectorAll(".goals-list li")
const checkedList  = document.querySelectorAll(".checkbox svg")

const goalsNumber = goalsList.length;
const finishedGoalsNumber = checkedList.length;

const total = document.querySelector(".total__text p")
total.innerHTML = finishedGoalsNumber + "/" + goalsNumber;

buttonAdd.addEventListener("click", () => {
    formWrap.style.display = "flex";
})

cancelButton.addEventListener("click", () => {
    formWrap.style.display = "none";
})

formWrap.addEventListener('mouseup', function(e){
    if(!form.contains(e.target)){
        formWrap.style.display = 'none'
    }
})