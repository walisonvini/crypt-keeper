function randomPassword(size, idInputPassword) {
    const inputPassword = document.getElementById(idInputPassword);

    const caracteresEspeciais = '!@#$%^&*()';
    const letrasMinusculas = 'abcdefghijklmnopqrstuvwxyz';
    const letrasMaiusculas = letrasMinusculas.toUpperCase();
    const numeros = '0123456789';

    const caracteres = caracteresEspeciais + letrasMinusculas + letrasMaiusculas + numeros;

    let password = '';

    for (let i = 0; i < size; i++) {
        const randomIndex = Math.floor(Math.random() * caracteres.length);
        password += caracteres.charAt(randomIndex);
    }

    inputPassword.value = password
}

function seePassword(eyeIcon, passwordInput) {
    const togglePassword = document.getElementById(eyeIcon);
    const input = document.getElementById(passwordInput);

    const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
    input.setAttribute('type', type);

    const iconSrc = type === 'password' ? "/static/icons/eye.svg" : "/static/icons/eye-off.svg";
    togglePassword.setAttribute('src', iconSrc);
}

function copyInput(idInputText, text) {
    const inputText = document.getElementById(idInputText).value;

    navigator.clipboard.writeText(inputText).then(() => {
        showAlert(text);
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

function showAlert(message) {
    const alertBox = document.querySelector('.alert.alert-success');
    const alertTitle = alertBox.querySelector('.alert-title');
    
    alertTitle.textContent = message;
    
    alertBox.style.display = 'flex';
    
    setTimeout(() => {
        alertBox.style.display = 'none';
    }, 3000);
}