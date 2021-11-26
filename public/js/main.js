var CORRECT_USER = 'user';
var CORRECT_PASS = 'pass';
var check = true;

var inputUsername = document.getElementById('username');
var inputPassword = document.getElementById('password');

var formLogin = document.getElementById('loginform');

if (formLogin.attachEvent) {
    formLogin.attachEvent('submit', onFormsubmit);
} else {
    formLogin.addEventListener('submit', onFormsubmit);
}

function onFormsubmit(e) {
    var user = inputUsername.value;
    var pass = inputPassword.value;

    if (user == CORRECT_USER && pass == CORRECT_PASS) {
        alert('Đăng nhập thành công');
    } else {
        alert('Tài khoản hoặc mật khẩu không đúng');
    }
}

function showHidden() {
    if (check) {
        inputPassword.type = 'text';
        check = false;
    } else {
        inputPassword.type = 'password';
        check = true
    }

}