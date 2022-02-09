// Show Password function for login.html, Show Password function for login modal is in base.html
function showPasswordPage() {
  var passwordEl = document.getElementById("password-pg");
  if (passwordEl.type === "password") {
    passwordEl.type = "text";
  } else {
    passwordEl.type = "password";
  }
}