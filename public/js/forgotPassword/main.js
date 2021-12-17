const submit_btn = document.querySelector("#submit_btn");
const container = document.querySelector(".container");

var emailInput = document.getElementById('email');

var formLogin = document.getElementById('forgot_password');

if (formLogin.attachEvent) {
    formLogin.attachEvent('submit', onFormsubmit);
} else {
    formLogin.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
    e.preventDefault();
    var email = emailInput.value;

     const options = {
        method: "POST",
        headers: {
            "content-type": "application/json"
        },
        body: JSON.stringify({
            email:email
        })
    }

    const res = await fetch("/users/forgetPass", options);
    const data = await res.json();

    //Có gì sửa lại dòng này giúp e
    if (data.error) {
        alert('Email không tồn tại');
    } else if (data.data.success) {
        alert('Đã gửi link reset mật khẩu');
    } else {
        alert('Đã xảy ra lỗi, vui lòng thử lại sau');
    }
}
