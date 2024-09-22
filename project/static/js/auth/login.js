document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('password');
    const toggleIcon = document.querySelector('.input-container .icon');

    toggleIcon.addEventListener('click', function () {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);

        const iconSrc = type === 'password' ? '/static/icons/eye-off.svg' : '/static/icons/eye.svg';
        toggleIcon.setAttribute('src', iconSrc);
    });

    const alertClose = document.querySelector('.alert-close');
    const alertError = document.querySelector('.alert-error');

    alertClose.addEventListener('click', function () {
        alertError.style.display = 'none';
    });

    setTimeout(function () {
        alertError.style.display = 'none';
    }, 5000);
});

