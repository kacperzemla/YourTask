const buttonAdd = document.querySelector(".tasks__add")
const formWrap = document.querySelector(".bg-modal")
const cancelButton = document.querySelector(".goals-add__button")
const form = document.querySelector(".goals-add")
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