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
  oldDob = inputDateofbirth.value;
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
    var name = inputFullname.value;
    var dob = inputDateofbirth.value;
    var email = inputEmail.value;
    var phone = inputPhonenumber.value;

    if (name == '' && dob == oldDob && email == '' && phone == ''){
      alert('Bạn chưa nhập bất kì thông tin nào cần thay đổi')
    }
    else if(!letters.test(name) && name != '')
    {
      alert('Họ và tên không bao gồm ký tự đặc biệt và số');
    }
    else
    {
      if (name == '')
      {
        name = inputFullname.placeholder;
      }
      if (email == '')
      {
        email = inputEmail.placeholder;
      }
      if (phone == '')
      {
        phone = inputPhonenumber.placeholder;
      }
      if (dob == '')
      {
        dob = oldDob;
      }
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
      // const res = await fetch("/api/users/details", options);
      // const data = await res.json();

      // if (data.error == "Duplicated email") {
      //     alert('Email này đã được sử dụng, vui lòng chọn email khác');
      //     console.log(data)
      //     return;
      // } else if (data.data.success) {
      //     alert('Thay đổi thông tin thành công');
      //     console.log(data);
      //     location.href = "/users/view-profile";
      //     return;
      // } else {
      //     alert('Đã xảy ra lỗi, vui lòng thử lại sau');
      //     console.log(data);
      //     return;
      // }
      fetch("/api/users/details", options)
      .then(data => data.json())
      .then(data =>  {
        console.log(data)
        if (data.error == "Duplicated email") {
          alert('Email này đã được sử dụng, vui lòng chọn email khác');
          console.log(data)
        } else if (data.data.success) {
          alert("Thay đổi thông tin thành công"); 
          location.href = "/users/view-profile";
          console.log(data)
        } else {
          alert("Thay đổi thông tin thất bại");
        }
      })
      .catch((err) => {
        alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
        console.error(err);
      })
    }
}
