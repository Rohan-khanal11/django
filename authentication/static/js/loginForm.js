// login_form.js
document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  const usernameInput = document.getElementById('username');
  const passwordInput = document.getElementById('password');
  const usernameError = document.getElementById('username-error');
  const passwordError = document.getElementById('password-error');

  form.addEventListener('submit', (e) => {
    let valid = true;

    // Validate username
    if (usernameInput.value.trim().length < 3) {
      usernameError.style.display = 'block';
      usernameInput.classList.add('error-input');
      valid = false;
    } else {
      usernameError.style.display = 'none';
      usernameInput.classList.remove('error-input');
    }

    // Validate password
    if (passwordInput.value.length < 6) {
      passwordError.style.display = 'block';
      passwordInput.classList.add('error-input');
      valid = false;
    } else {
      passwordError.style.display = 'none';
      passwordInput.classList.remove('error-input');
    }

    if (!valid) {
      e.preventDefault();
    }
  });

  // Clear error on input
  usernameInput.addEventListener('input', () => {
    usernameError.style.display = 'none';
    usernameInput.classList.remove('error-input');
  });

  passwordInput.addEventListener('input', () => {
    passwordError.style.display = 'none';
    passwordInput.classList.remove('error-input');
  });
});
