$(document).ready(function() {
    $('#createCredential').on('click', function(event) {
        event.preventDefault();

        $('#name').removeClass('input-error');
        $('#username').removeClass('input-error');
        $('#password').removeClass('input-error');
        $('#url').removeClass('input-error');

        $('#nameError').text('');
        $('#usernameError').text('');
        $('#passwordError').text('');
        $('#urlError').text('');

        var urlPath = window.location.pathname;
        var vaultId = urlPath.match(/\/vault\/(\d+)/)[1];

        var formData = new FormData($('#form-create-credential')[0]);

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
                
                $('#credential-table tbody').prepend(`
                    <tr id="credential-${data.credential.id}">
                        <td>
                            <div class="flex">
                                <img src="${data.credential.icon}"">
                                <div>
                                    <p class="nameTable" onclick="openModalViewCredential(
                                        ${data.credential.id},
                                        '${data.credential.name}',
                                        '${data.credential.username}',
                                        '${data.credential.password}',
                                        '${data.credential.url || ''}',
                                        '${data.credential.description || ''}'
                                    )">${data.credential.name}</p>
                                    <p class="usernameTable">${data.credential.username}</p>
                                </div>
                            </div>
                        </td>
                        <td>Me</td>
                        <td>
                            <div class="options-toggle">⋮</div>
                            <div class="options-menu">
                                <ul>
                                    <li><a onclick="copyText('${data.credential.username}')">Copy username</a></li>
                                    <li><a onclick="copyText('${data.credential.password}')">Copy password</a></li>
                                    ${data.credential.url ? `<li><a onclick="launchUrl('${data.credential.url}')">Launch</a></li>` : ''}
                                    <li><a onclick="deleteCredential(${data.credential.id})">Delete</a></li>
                                </ul>
                            </div>
                        </td>
                    </tr>
                `);                

                $('#form-create-credential').trigger('reset');

                closeModal('modal-create-credential');

                $('.alert-success').show();
                $('.alert-title').text(data.message);

                setTimeout(function () {
                    $('.alert-title').text('');
                    $('.alert-success').hide();
                }, 3000);
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

    // update credential
    $('#updateCredential').on('click', function(event) {
        event.preventDefault();

        $('#name-view').removeClass('input-error');
        $('#username-view').removeClass('input-error');
        $('#password-view').removeClass('input-error');
        $('#url-view').removeClass('input-error');

        $('#nameError-view').text('');
        $('#usernameError-view').text('');
        $('#passwordError-view').text('');
        $('#urlError-view').text('');


        var formData = new FormData($('#form-view-credential')[0]);

        var urlPath = window.location.pathname;
        var vaultId = urlPath.match(/\/vault\/(\d+)/)[1];

        var data = {};

        formData.forEach(function(value, key){
            data[key] = value;
        });

        data['vault'] = vaultId;

        id = $('#credentialId').val();

        $.ajax({
            url: '/vaults/credential/' + id,
            type: 'PUT',
            data: JSON.stringify(data),
            processData: false,
            contentType: false,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            success: function(data) {
                const updatedCredentialRow = `
                    <td>
                        <div class="flex">
                            <img src="${data.credential.icon}">
                            <div>
                                <p class="nameTable" onclick="openModalViewCredential(
                                    '${id}',
                                    '${data.credential.name}',
                                    '${data.credential.username}',
                                    '${data.credential.password}',
                                    '${data.credential.url || ''}',
                                    '${data.credential.description || ''}'
                                )">${formData.get('name')}</p>
                                <p class="usernameTable">${formData.get('username')}</p>
                            </div>
                        </div>
                    </td>
                    <td>Me</td>
                    <td>
                        <div class="options-toggle">⋮</div>
                        <div class="options-menu">
                            <ul>
                                <li><a onclick="copyText('${data.credential.username}')">Copy username</a></li>
                                <li><a onclick="copyText('${data.credential.password}')">Copy password</a></li>
                                ${data.credential.url ? `<li><a onclick="launchUrl('${data.credential.url}')">Launch</a></li>` : ''}
                                <li><a onclick="deleteCredential(${data.credential.id})">Delete</a></li>
                            </ul>
                        </div>
                    </td>
                `;
                $('#credential-' + id).html(updatedCredentialRow);

                $('#form-view-credential').trigger('reset');

                closeModal('modal-view-credential');

                $('.alert-success').show();
                $('.alert-title').text(data.message);

                setTimeout(function () {
                    $('.alert-title').text('');
                    $('.alert-success').hide();
                }, 3000);
            },
            error: function(xhr, status, error) {
                var response = JSON.parse(xhr.responseText);
                if (response.errors) {
                    if (response.errors.name) {
                        $('#nameError-view').text(response.errors.name);
                        $('#name-view').addClass('input-error');
                    }
                    if (response.errors.username) {
                        $('#usernameError-view').text(response.errors.username);
                        $('#username-view').addClass('input-error');
                    }
                    if (response.errors.password) {
                        $('#passwordError-view').text(response.errors.password);
                        $('#password-view').addClass('input-error');
                    }
                    if (response.errors.url) {
                        $('#urlError-view').text(response.errors.url);
                        $('#url-view').addClass('input-error');
                    }
                }
            
            }
        });
    });

    // delete credential
    $('#deleteCredential').on('click', function(event) {
        event.preventDefault();

        var id = $('#credentialId').val();

        deleteCredential(id);
    });

    $('#credential-table').on('click', '.options-toggle', function(event) {
        event.stopPropagation();
    
        var $menu = $(this).next('.options-menu');
        $menu.toggle();
    });

    $(document).on('click', function() {
        $('.options-menu').hide();
    });
});

function openModalViewCredential(id, name, username, password, url, description) {
    openModal('modal-view-credential');

    $('#credentialId').val(id);
    $('#name-view').val(name);
    $('#username-view').val(username);
    $('#password-view').val(password);
    $('#url-view').val(url);
    $('#description-view').val(description);
}

function randomPassword(size, idInputPassword) {
    const inputPassword = document.getElementById(idInputPassword);

    if (inputPassword.value) {
        Swal.fire({
            title: "Are you sure?",
            text: "Are you sure you want to overwrite the current password?",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "Yes"
        }).then((result) => {
            if (result.isConfirmed) {
                generatePassword(size, inputPassword);
            }
        });
    } else {
        generatePassword(size, inputPassword);
    }
}

function generatePassword(size, inputPassword) {
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

    inputPassword.value = password;
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

    if(!inputText) {
        return;
    }

    navigator.clipboard.writeText(inputText).then(() => {
        showAlert(text);
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

function copyText(text) {
    navigator.clipboard.writeText(text).then(() => {
        showAlert('Copied to clipboard');
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

function launch(input) {
    const url = document.getElementById(input).value;

    if(!url) {
        return;
    }

    if (!url.startsWith('http://') && !url.startsWith('https://')) {
        window
            .open('http://' + url, '_blank')
            .focus();
    }

    window.open(url, '_blank');
}

function launchUrl(url) {
    if(!url) {
        return;
    }

    if (!url.startsWith('http://') && !url.startsWith('https://')) {
        window
            .open('http://' + url, '_blank')
            .focus();
    }

    window.open(url, '_blank');
}

function deleteCredential(id) {
    Swal.fire({
        title: "Are you sure?",
        text: "Are you sure you want to delete this credential? This action cannot be undone.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes"
    }).then((result) => {
        if (result.isConfirmed) {

            $.ajax({
                url: '/vaults/credential/' + id,
                type: 'DELETE',
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                success: function(data) {
                    $('#credential-' + id).remove();
    
                    closeModal('modal-view-credential');
    
                    $('.alert-success').show();
                    $('.alert-title').text(data.message);
    
                    setTimeout(function () {
                        $('.alert-title').text('');
                        $('.alert-success').hide();
                    }, 3000);
                },
                error: function(xhr, status, error) {
                    var response = JSON.parse(xhr.responseText);
    
                    $('.alert-success').show();
                    $('.alert-title').text(response.message);
    
                    setTimeout(function () {
                        $('.alert-title').text('');
                        $('.alert-success').hide();
                    }, 3000);
                }
            });
        }
    });
}