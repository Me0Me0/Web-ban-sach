var usernameInput = document.getElementById('username');

var formForgotPassword = document.getElementById('forgot_password');

if (formForgotPassword.attachEvent) {
    formForgotPassword.attachEvent('submit', onFormsubmit);
} else {
    formForgotPassword.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
    e.preventDefault();
    var username = usernameInput.value;

    if (username.length < 5) {
        alert('Tên đăng nhập phải có ít nhất 5 ký tự')
    }
    else
    {
        const options = {
            method: "POST",
            headers: {
                "content-type": "application/json"
            },
            body: JSON.stringify({
                username: username
            })
        }        

        const res = await fetch("/api/users/forgot-password", options);
        const data = await res.json();

        //Có gì sửa lại dòng này giúp e
        if (data.error) {
            alert('Tên đăng nhập không tồn tại');
        } else if (data.data.status_code == 202) {
            alert('Liên kết dẫn đến trang đặt lại mật khẩu đã gửi tới email đăng ký tài khoản này');
        } else {
            alert('Đã xảy ra lỗi, vui lòng thử lại sau');
        }
    }
}
