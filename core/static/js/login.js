document.addEventListener("DOMContentLoaded", function() {
    const username = document.getElementById('mail');
    const password = document.getElementById('pass');
    const icon = document.querySelector(".bi");
    const form = document.querySelector("form");

    // Mostrar/ocultar contraseña
    if (icon) {
        icon.addEventListener("click", () => {
            password.type = password.type === "password" ? "text" : "password";
            icon.classList.toggle('bi-eye-slash');
        });
    }

    if (form) {
        form.addEventListener("submit", (evento) => {
            let isValid = true;

            // Resetear errores
            username.classList.remove("errorField");
            password.classList.remove("errorField");

            // Validar email
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(username.value)) {
                username.classList.add("errorField");
                username.placeholder = "Correo inválido";
                isValid = false;
                evento.preventDefault();
            }

            // Validar contraseña
            if (password.value.length < 8) {
                password.classList.add("errorField");
                password.placeholder = "Contraseña inválida";
                isValid = false;
                evento.preventDefault();
            }

        });
    }

    username.addEventListener("input", () => {
        username.classList.remove("errorField");
        username.placeholder = "Correo electrónico";
    });

    password.addEventListener("input", () => {
        password.classList.remove("errorField");
        password.placeholder = "Contraseña";
    });
});