document.getElementById('registrationForm').addEventListener('submit', function(e) {
            e.preventDefault();
            let isValid = true;
            
            // Проверка имени
            const name = document.getElementById('name');
            const nameError = document.getElementById('nameError');
            if (name.value.trim() === '') {
                nameError.style.display = 'block';
                isValid = false;
            } else {
                nameError.style.display = 'none';
            }
            
            // Проверка email
            const email = document.getElementById('email');
            const emailError = document.getElementById('emailError');
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email.value)) {
                emailError.style.display = 'block';
                isValid = false;
            } else {
                emailError.style.display = 'none';
            }
            
            // Проверка пароля
            const password = document.getElementById('password');
            const passwordError = document.getElementById('passwordError');
            if (password.value.length < 6) {
                passwordError.style.display = 'block';
                isValid = false;
            } else {
                passwordError.style.display = 'none';
            }
            
            // Проверка подтверждения пароля
            const confirmPassword = document.getElementById('confirmPassword');
            const confirmError = document.getElementById('confirmError');
            if (password.value !== confirmPassword.value) {
                confirmError.style.display = 'block';
                isValid = false;
            } else {
                confirmError.style.display = 'none';
            }
            
            if (isValid) {
                alert('Регистрация прошла успешно!');
                // Здесь обычно отправка данных на сервер
                this.reset();
            }
        });