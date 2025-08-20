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

    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const sidebar = document.querySelector('.container-sidebar');
    
    if (mobileMenuToggle && sidebar) {
        mobileMenuToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            sidebar.classList.toggle('active');
        });
    }

    document.addEventListener('click', function(event) {
        if (window.innerWidth <= 768) {
            if (!sidebar.contains(event.target) && !mobileMenuToggle.contains(event.target)) {
                mobileMenuToggle.classList.remove('active');
                sidebar.classList.remove('active');
            }
        }
    });

    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            mobileMenuToggle.classList.remove('active');
            sidebar.classList.remove('active');
        }
    });
});
