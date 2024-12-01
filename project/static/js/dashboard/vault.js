document.addEventListener('DOMContentLoaded', function () {
    const alertClose = document.querySelector('.alert-close');
    const alertSucess = document.querySelector('.alert-success');

    alertClose.addEventListener('click', function () {
        alertSucess.style.display = 'none';
    });

    setTimeout(function () {
        alertSucess.style.display = 'none';
    }, 3000);
});

