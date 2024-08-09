document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('password');
    const toggleIcon = document.querySelectorAll('.input-container .icon');

    toggleIcon[0].addEventListener('click', function () {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);

        const iconSrc = type === 'password' ? '/static/icons/eye-off.svg' : '/static/icons/eye.svg';
        toggleIcon[0].setAttribute('src', iconSrc);
    });

    const confirmPasswordInput = document.getElementById('password2');

    toggleIcon[1].addEventListener('click', function () {
        const type = confirmPasswordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        confirmPasswordInput.setAttribute('type', type);

        const iconSrc = type === 'password' ? '/static/icons/eye-off.svg' : '/static/icons/eye.svg';
        toggleIcon[1].setAttribute('src', iconSrc);
    });
});