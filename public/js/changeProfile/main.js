var changeProfileForm = document.getElementById('edit-profile-form');

var inputFullname = document.getElementById('name');
var inputDateofbirth = document.getElementById('dob');
var inputEmail = document.getElementById('email');
var inputPhonenumber = document.getElementById('phone');
var avt = document.getElementById("avt");
var oldDob
var oldAvt
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
  avt.src = data.avt_link;
  oldAvt = data.avt_link;
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})

var loadFile = async function(event) {
  avt.src = "https://media0.giphy.com/media/6036p0cTnjUrNFpAlr/giphy.gif";
  var formData = new FormData();
  formData.append("file", event.target.files[0]);

  const options = {
    method: "POST",
    body: formData
  }

  const res = await fetch("/api/images/upload", options);
  const data = await res.json();

  avt.src = data.url;
};

async function onFormsubmit(e) {
    e.preventDefault();
    var name = inputFullname.value.trim();
    var dob = inputDateofbirth.value;
    var email = inputEmail.value;
    var phone = inputPhonenumber.value;
    var avt_link = avt.src; 

    if (name == '' && dob == oldDob && email == '' && phone == '' && avt_link == oldAvt) {
      alert('Bạn chưa nhập bất kì thông tin nào cần thay đổi');
      return;
    }
    else if(!letters.test(name) && name != '')
    {
      alert('Họ và tên không bao gồm ký tự đặc biệt và số');
      return;
    }
    else if (phone && (isNaN(Number(phone)) || phone.length != 10))
    {
      alert('Số điện thoại không hợp lệ');
      return;
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
            email: email,
            avt_link: avt_link
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


