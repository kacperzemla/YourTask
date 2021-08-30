const form = document.querySelector('.register__form')
const email = document.querySelector('#id_username');
const password = document.querySelector('#id_password1')
const password2 = document.querySelector('#id_password2')
email.required = false;
password.required = false;
password2.required = false;
// const email = document.querySelector('.email')
// email.style.border = '2px solid red'

form.addEventListener('submit', (e) => {

     if(!checkInputs()){
          e.preventDefault();
     };

})

function checkInputs(){
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();
    let a = 0;
    if(emailValue === ''){
         setError(email, 'Email cannot be blank');
    } else if(!isEmail(emailValue)){
        setError(email, 'Email is not valid');
    } else{
         setSuccess(email)
         a++;
    }

    if(passwordValue.length < 8){
         setError(password, 'Password must be 8 characters long');
    } else {
         setSuccess(password);
         a++;
    }

    if(passwordValue !== password2Value){
         setError(password2, 'Passwords don`t match');

    } else {
         setSuccess(password2);
         a++
    }
    if(a === 3){
         return true
    } else {
         return false
    }
}

function setError(input, message){
     const error = input.nextElementSibling;
     const label = error.parentElement;
     label.style.marginBottom = '0'
     const errorText = error.querySelector('.error')
     errorText.innerText = message;
     error.style.display = 'flex';

}

function setSuccess(input){
     const success = input.nextElementSibling;
     success.style.display = 'none';
     const label = success.parentElement;
     label.style.marginBottom = '0.5rem'
}

function isEmail(email){
     return /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/.test(email)
}
