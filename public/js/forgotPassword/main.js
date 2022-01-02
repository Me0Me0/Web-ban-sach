var usernameInput = document.getElementById('username');

var formLogin = document.getElementById('forgot_password');

if (formLogin.attachEvent) {
    formLogin.attachEvent('submit', onFormsubmit);
} else {
    formLogin.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
    e.preventDefault();
    var username = usernameInput.value;

    const options = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            username:username
        })
    }

    const res = await fetch("/users/forgot-password", options);
    const data = await res.json();

    //Có gì sửa lại dòng này giúp e
    if (data.error) {
        alert('Tên đăng nhập không tồn tại');
    } else if (data.data.success) {
        alert('Liên kết dẫn đến trang đặt lại mật khẩu đã gửi tới email đăng ký tài khoản này');
    } else {
        alert('Đã xảy ra lỗi, vui lòng thử lại sau');
    }
}
