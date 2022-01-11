// var CORRECT_USER = 'user';
// var CORRECT_PASS = 'pass';
// var check = true;

var inputUsername = document.getElementById('loginusername');
var inputPassword = document.getElementById('loginpassword');

var formLogin = document.getElementById('loginform');

if (formLogin.attachEvent) {
    formLogin.attachEvent('submit', onFormsubmit);
} else {
    formLogin.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
    e.preventDefault();
    var user = inputUsername.value;
    var pass = inputPassword.value;

    if (pass.length < 8) {
        alert('Mật khẩu phải có ít nhất 8 kí tự');
    }

    // if (user == CORRECT_USER && pass == CORRECT_PASS) {
    //     alert('Đăng nhập thành công');
    // } else {
    //     alert('Tài khoản hoặc mật khẩu không đúng');
    // }
    const options = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            username: user,
            password: pass
        })
    }

    const res = await fetch("/api/users/signin", options);
    const data = await res.json();

    if (data.error) {
        alert('Tài khoản hoặc mật khẩu không đúng');
    } else if (data.data.success) {
        //alert('Đăng nhập thành công');
        localStorage.setItem('user', user);
        window.location.href = "/admin/list-users";
    } else {
        alert('Đã xảy ra lỗi, vui lòng thử lại sau');
    }
}