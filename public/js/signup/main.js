const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

var inputUsername = document.getElementById('username');
var inputPassword = document.getElementById('password');
var inputRePassword = document.getElementById('repassword');
var inputFullname = document.getElementById('fullname');
var inputDateofbirth = document.getElementById('dob');
var inputEmail = document.getElementById('email');
var inputPhonenumber = document.getElementById('phone');

var signUpForm = document.getElementById('signupform');

var expression = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])/;

if (signUpForm.attachEvent) {
  signUpForm.attachEvent('submit', onFormsubmit);
} else {
  signUpForm.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
  e.preventDefault();
  var user = inputUsername.value;
  var pass = inputPassword.value;
  var repass = inputRePassword.value;
  var name = inputFullname.value;
  var dob = inputDateofbirth.value;
  var email = inputEmail.value;
  var phone = inputPhonenumber.value;

  if (user.length < 5) {
    alert('Tài khoản phải có ít nhất 5 kí tự');
  }
  else if (pass.length < 8) {
    alert('Mật khẩu phải có ít nhất 8 kí tự');
  }
  else if(!expression.test(pass))
  {
    alert('Mật khẩu phải chứa ít nhất 1 ký tự hoa, 1 ký tự thường và 1 số và không có ký tự đặc biệt')
  }
  else if(repass==''){
    alert('Vui lòng xác nhận lại mật khẩu');
  }
  else if(repass!==pass){
    alert('Xác nhận mật khẩu không trùng khớp');
  }
  else if(name==''){
    alert('Vui lòng nhập họ tên');
  }
  else if(dob==''){
    alert('Vui lòng chọn ngày tháng năm sinh');
  }
  else if(email==''){
    alert('Vui lòng nhập email');
  }
  else if(phone==''){
    alert('Vui lòng nhập số điện thoại');
  }
  else
  {
    const options = {
      method: "POST",
      headers: {
          "content-type": "application/json"
      },
      body: JSON.stringify({
          username: user,
          password: pass,
          name: name,
          dob: dob,
          phone: phone,
          email: email
      })
    }
    fetch("/users/signup", options)
    .then(data => data.json())
    .then(data =>  { 
      console.log(data);
      if(data.data&&data.data.id)
      {
        alert("Tạo tài khoản thành công"); 
      } 
      else
      {
        alert("Tên tài khoản đã tồn tại, vui lòng thử tên khác");
      }
    })
    .catch((err) => {
      alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
      console.error(err);
    })
  }
}

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});