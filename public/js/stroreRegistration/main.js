var inputName = document.getElementById('name');
var inputEmail = document.getElementById('email');
var inputPhonenumber = document.getElementById('phone');
var inputDes = document.getElementById('des');

var signUpForm = document.getElementById('signupform');



if (signUpForm.attachEvent) {
  signUpForm.attachEvent('submit', onFormsubmit);
} else {
  signUpForm.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
  e.preventDefault();
  var name = inputName.value;
  var email = inputEmail.value;
  var phone = inputPhonenumber.value;
  var des = inputDes.value;

  if(name==''){
    alert('Vui lòng nhập tên cửa hàng');
  }
  else if(email==''){
    alert('Vui lòng nhập email');
  }
  else if(phone==''){
    alert('Vui lòng nhập số điện thoại');
  }
  else if(des==''){
    alert('Vui lòng nhập mô tả cửa hàng');
  }
  else
  {
    const options = {
      method: "POST",
      headers: {
          "content-type": "application/json"
      },
      body: JSON.stringify({
          name: name,
          phone: phone,
          email: email,
          des: des
      })
    }
    fetch("/api/mystore/register", options)
    .then(data => data.json())
    .then(data =>  { 
      console.log(data);
      if(data.data&&data.data.id)
      {
        alert("Đăng ký shop thành công"); 
        location.href = "/mystore"
      } 
      // else
      // {
      //   alert("Tên tài khoản đã tồn tại, vui lòng thử lại với tên khác");
      // }
    })
    .catch((err) => {
      alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
      console.error(err);
    })
  }
}