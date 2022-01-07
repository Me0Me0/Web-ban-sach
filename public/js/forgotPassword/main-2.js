var passwordInput = document.getElementById('pass');
var repasswordInput = document.getElementById('repass')
var formForgotPassword = document.getElementById('forgot_password');
var token = window.location.href;
var expression = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])/;

if (formForgotPassword.attachEvent) {
    formForgotPassword.attachEvent('submit', onFormsubmit);
} else {
    formForgotPassword.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
    e.preventDefault();
    var password = passwordInput.value;
    var repassword = repasswordInput.value;

    if (password.length < 8) {
        alert('Mật khẩu phải có ít nhất 8 ký tự');
    }
    else if(!expression.test(password)){
        alert('Mật khẩu phải chứa ít nhất 1 chữ hoa, 1 chữ thường, 1 số và không có ký tự đặc biệt')
    }
    else if(repassword==''){
        alert('Vui lòng xác nhận lại mật khẩu');
    }
    else if(repassword!==password){
        alert('Mật khẩu xác nhận không trùng khớp');
    }
    else
    {
        const options = {
            method: "POST",
            headers: {
                "content-type": "application/json"
            },
            body: JSON.stringify({
                password: password
            })
        }   
        
        token = token.substring(token.lastIndexOf('/') + 1)
        console.log(`/users/reset-password/${token}`)
        const res = await fetch(`/users/reset-password/${token}`, options);
        const data = await res.json();

        //Có gì sửa lại dòng này giúp em
        if (data.error) {
            alert('Đặt lại mật khẩu thất bại');
        } else if (data.data.success) {
            alert('Đặt lại mật khẩu thành công, đăng nhập để tiếp tục sử dụng');
            location.href = "/users/signin"
        } else {
            alert('Đã xảy ra lỗi, vui lòng thử lại sau');
        }
    }
}
