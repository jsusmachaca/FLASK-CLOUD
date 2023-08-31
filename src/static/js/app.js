const password = document.getElementById('password')
const inpPass = document.getElementById('show-passwd')
const inpName = document.getElementById('name')


password.addEventListener('focus', ()=> {
    inpPass.style.display = 'block'
    password.style.marginBottom = '-10px'
})

inpPass.addEventListener('click', ()=> {
    if (password.type == 'password')
    {
        password.type = 'text'
    }else 
    {
        password.type = 'password'
    }
})

/*
password.addEventListener('focusout', ()=> {
    inpPass.style.display = 'none'
})
*/
inpName.addEventListener('focus', ()=> {
    const message = document.getElementById('message')
    message.style.display = 'none'
})