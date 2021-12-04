var inputUsername = document.getElementById('loginusername');
var inputPassword = document.getElementById('loginpassword');

var formLogin = document.getElementById('signinform');

if (formLogin.attachEvent) {
    formLogin.attachEvent('submit', onFormsubmit);
} else {
    formLogin.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
    e.preventDefault();
    var user = inputUsername.value;
    var pass = inputPassword.value;

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

    const res = await fetch("/users/signin", options);
    const data = await res.json();

    if (data.error) {
        alert('Tài khoản hoặc mật khẩu không đúng');
    } else if (data.data.success) {
        alert('Đăng nhập thành công');
        window.location.href = "/";
    } else {
        alert('Đã xảy ra lỗi, vui lòng thử lại sau');
    }
}