var changeProfileForm = document.getElementById('edit-profile-form');

var inputFullname = document.getElementById('name');
var inputEmail = document.getElementById('email');
var inputPhonenumber = document.getElementById('phone');
var inputDes = document.getElementById('des');


if (changeProfileForm.attachEvent) {
  changeProfileForm.attachEvent('submit', onFormsubmit);
} else {
  changeProfileForm.addEventListener('submit', onFormsubmit);
}

const options = {
  method: "GET", 
  headers: {
      "content-type": "text/plain;charset=UTF-8"
  }
}

fetch("/mystore/edit", options)
.then(data => data.json())
.then(data =>  { 
  inputFullname.value = data.name;
  inputPhonenumber.value = "0" + data.phone;
  inputEmail.value = data.email;
  inputDes.value = data.des;
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})

// var loadFile = function(event) {
//   var reader = new FileReader();
//   reader.onload = function(){
//     var output = document.getElementById('avt');
//     output.src = reader.result;
//     console.log(output.src)
//   };
//   reader.readAsDataURL(event.target.files[0]);
// };

async function onFormsubmit(e) {
    e.preventDefault();
    var name = inputFullname.value;
    var email = inputEmail.value;
    var phone = inputPhonenumber.value;
    var des = inputDes.value;

    console.log(name, dob, email, phone)
    if (name == '' && dob == oldDob && email == '' && phone == ''){
      alert('Bạn chưa nhập bất kì thông tin nào cần thay đổi')
    }
    else
    {
      const options = {
        method: "PUT",
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
      fetch("/mystore/edit", options)
      .then(data => data.json())
      .then(data =>  { 
        alert("Thay đổi thông tin cửa hàng thành công"); 
        location.href = "/users/view-profile";
      })
      .catch((err) => {
        alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
        console.error(err);
      })
    }
}
