document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('toggle-password').addEventListener('click', function () {
        const passwordField = document.getElementById('password');
        const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordField.setAttribute('type', type);

        // Cambiar el ícono
        this.classList.toggle('fa-eye');
        this.classList.toggle('fa-eye-slash');
    });

    const formulario = document.getElementById('register-form');

    // Validar campos al cambiar o enviar el formulario
    formulario.addEventListener('submit', () => validateForm());
    formulario.querySelectorAll('.form-control').forEach(input => {
        input.addEventListener('input', () => validateForm()); // Valida mientras el usuario escribe
    });
});



function validateForm() {
    let isValid = true;

    // Limpiar errores y estilos previos
    document.querySelectorAll('.error-message').forEach(el => el.remove());
    document.querySelectorAll('.form-control').forEach(el => resetStyle(el));

    // Validar nombre
    const nombre = document.getElementById('nombre');
    if (!/^[a-zA-Z]{3,}$/.test(nombre.value)) {
        showError(nombre, 'El nombre debe tener al menos 3 letras y solo letras.');
        isValid = false;
    }

    // Validar apellido
    const apellido = document.getElementById('apellido');
    if (!/^[a-zA-Z]{3,}$/.test(apellido.value)) {
        showError(apellido, 'El apellido debe tener al menos 3 letras y solo letras.');
        isValid = false;
    }

    // Validar email
    const email = document.getElementById('email');
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) { 
        showError(email, 'Ingresa un correo electrónico válido.');
        isValid = false;
    }

    // Validar contraseña de de tamaño
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm-password');
    if (!/(?=.*[A-Za-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{6,}/.test(password.value)) {
        showError(password, 'La contraseña debe tener al menos 6 caracteres, incluir al menos 1 letra, 1 número y 1 carácter especial.');
        isValid = false;
    }

    // Validar confirmación de contraseña
    if (password.value !== confirmPassword.value) {
        showError(confirmPassword, 'Las contraseñas no coinciden.');
        isValid = false;
    }
    const adminPassword = document.getElementById('adminPassword');
    if (adminPassword.value.trim() !== '' && adminPassword.value !== "clavemaestra123") {
        showError(adminPassword, 'Contraseña maestra incorrecta');
        isValid = false;
    }

    return isValid;
}

// Función para mostrar errores y cambiar diseño dinámicamente
function showError(input, message) {
    // Cambiar estilos en línea del campo
    input.style.border = '2px solid #d9534f'; // Rojo para errores
    input.style.backgroundColor = '#f8d7da';
    input.style.color = '#721c24';

    // Mostrar mensaje de error debajo del campo
    const error = document.createElement('div');
    error.className = 'error-message';
    error.style.fontSize = '12px';
    error.style.color = '#d9534f';
    error.style.marginTop = '5px';
    error.textContent = message;
    input.parentNode.appendChild(error);
}

// Función para resetear estilos
function resetStyle(input) {
    input.style.border = '';
    input.style.backgroundColor = '';
    input.style.color = '';
}