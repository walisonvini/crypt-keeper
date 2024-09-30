document.addEventListener('DOMContentLoaded', function() {
    var menuToggles = document.querySelectorAll('.menu-toggle');

    menuToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function(event) {
            event.preventDefault();

            var submenu = toggle.nextElementSibling;

            document.querySelectorAll('.submenu').forEach(function(menu) {
                if (menu !== submenu) {
                    menu.style.display = 'none';
                }
            });

            if (submenu.style.display === 'block') {
                submenu.style.display = 'none';
                toggle.classList.remove('active');

            } else {
                submenu.style.display = 'block';
                toggle.classList.add('active');
            }
        });
    });
});
