$(document).ready(function() {
    $('#createCredential').on('click', function(event) {
        event.preventDefault();

        var urlPath = window.location.pathname;
        var vaultId = urlPath.match(/\/vault\/(\d+)/)[1];

        var formData = new FormData($('#createCredentialForm')[0]);

        formData.append('vault', vaultId);

        $.ajax({
            url: '/vaults/credential',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            success: function(data) {
                $('#createCredentialForm').trigger('reset');

                closeModal('modal-create-credential');

                $('.alert-success').show();
                $('.alert-success').text(data.message);

                setTimeout(function () {
                    $('.alert-success').text('');
                    $('.alert-success').hide();
                }, 2000);
            },
            error: function(xhr, status, error) {
                var response = JSON.parse(xhr.responseText);
                if (response.errors) {
                    if (response.errors.name) {
                        $('#nameError').text(response.errors.name);
                        $('#name').addClass('input-error');
                    }
                    if (response.errors.username) {
                        $('#usernameError').text(response.errors.username);
                        $('#username').addClass('input-error');
                    }
                    if (response.errors.password) {
                        $('#passwordError').text(response.errors.password);
                        $('#password').addClass('input-error');
                    }
                    if (response.errors.url) {
                        $('#urlError').text(response.errors.url);
                        $('#url').addClass('input-error');
                    }
                }
            
            }
        });
    });
});