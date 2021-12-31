// const sign_in_btn = document.querySelector("#sign-in-btn");
// const sign_up_btn = document.querySelector("#sign-up-btn");
// const container = document.querySelector(".container");

var inputUsername = document.getElementById('username');
var inputPassword = document.getElementById('password');
var inputRePassword = document.getElementById('repassword');
var inputFullname = document.getElementById('fullname');
var inputDateofbirth = document.getElementById('dob');
var inputEmail = document.getElementById('email');
var inputPhonenumber = document.getElementById('phone');

var signUpForm = document.getElementById('signupform');

var letters = /^[A-Za-zàáâãèéêìíòóôõùúýỳỹỷỵựửữừứưụủũợởỡờớơộổỗồốọỏịỉĩệểễềếẹẻẽặẳẵằắăậẩẫầấạảđÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝỲỸỶỴỰỬỮỪỨƯỤỦŨỢỞỠỜỚƠỘỔỖỒỐỌỎỊỈĨỆỂỄỀẾẸẺẼẶẲẴẰẮĂẬẨẪẦẤẠẢĐ\s]+$/;
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
    alert('Tên đăng nhập phải có ít nhất 5 ký tự');
  }
  else if (pass.length < 8) {
    alert('Mật khẩu phải có ít nhất 8 ký tự');
  }
  else if(!expression.test(pass))
  {
    alert('Mật khẩu phải chứa ít nhất 1 chữ hoa, 1 chữ thường, 1 số và không có ký tự đặc biệt')
  }
  else if(repass==''){
    alert('Vui lòng xác nhận lại mật khẩu');
  }
  else if(repass!==pass){
    alert('Mật khẩu xác nhận không trùng khớp');
  }
  else if(name==''){
    alert('Vui lòng nhập họ tên');
  }
  else if(!letters.test(name))
	{
		alert('Họ và tên không bao gồm ký tự đặc biệt và số');
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
}

// sign_up_btn.addEventListener("click", () => {
//   container.classList.add("sign-up-mode");
// });

// sign_in_btn.addEventListener("click", () => {
//   container.classList.remove("sign-up-mode");
// });