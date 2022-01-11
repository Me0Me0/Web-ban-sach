var changeProfileForm = document.getElementById('edit-profile-form');

var inputFullname = document.getElementById('name');
var inputDateofbirth = document.getElementById('dob');
var inputEmail = document.getElementById('email');
var inputPhonenumber = document.getElementById('phone');
var oldDob
var letters = /^[A-Za-zàáâãèéêìíòóôõùúýỳỹỷỵựửữừứưụủũợởỡờớơộổỗồốọỏịỉĩệểễềếẹẻẽặẳẵằắăậẩẫầấạảđÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝỲỸỶỴỰỬỮỪỨƯỤỦŨỢỞỠỜỚƠỘỔỖỒỐỌỎỊỈĨỆỂỄỀẾẸẺẼẶẲẴẰẮĂẬẨẪẦẤẠẢĐ\s]+$/;

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

fetch("/api/users/details", options)
.then(data => data.json())
.then(data =>  { 
  inputFullname.placeholder = data.name;
  inputDateofbirth.value = data.dob;
  oldDob = inputDateofbirth.value
  inputPhonenumber.placeholder = "0" + data.phone;
  inputEmail.placeholder = data.email;
  document.getElementById("avt").src = data.avt_link;
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})

var loadFile = function(event) {
  var reader = new FileReader();
  reader.onload = function(){
    var output = document.getElementById('avt');
    output.src = reader.result;
    console.log(output.src)
  };
  reader.readAsDataURL(event.target.files[0]);
};

async function onFormsubmit(e) {
    e.preventDefault();
    var name = inputFullname.value || inputFullname.placeholder;
    var dob = inputDateofbirth.value;
    var email = inputEmail.value || inputEmail.placeholder;
    var phone = inputPhonenumber.value || inputPhonenumber.placeholder;

    console.log(name, dob, email, phone)
    if (name == '' && dob == oldDob && email == '' && phone == ''){
      alert('Bạn chưa nhập bất kì thông tin nào cần thay đổi')
    }
    else if(!letters.test(name) && name != '')
    {
      alert('Họ và tên không bao gồm ký tự đặc biệt và số');
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
            dob: dob,
            phone: phone,
            email: email
        })
      }
      fetch("/api/users/details", options)
      .then(data => data.json())
      .then(data =>  { 
        alert("Thay đổi thông tin thành công"); 
        location.href = "/users/view-profile";
      })
      .catch((err) => {
        alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
        console.error(err);
      })
    }
}
