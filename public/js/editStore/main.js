var changeDetailForm = document.getElementById('edit-detail-form');

var inputStoreName = document.getElementById('name');
var inputEmail = document.getElementById('email');
var inputPhonenumber = document.getElementById('phone');
var inputDescription = document.getElementById('description');


if (changeDetailForm.attachEvent) {
  changeDetailForm.attachEvent('submit', onFormsubmit);
} else {
  changeDetailForm.addEventListener('submit', onFormsubmit);
}

const options = {
  method: "GET", 
  headers: {
      "content-type": "text/plain;charset=UTF-8"
  }
}

fetch("/api/mystore", options)
.then(data => data.json())
.then(data =>  { 
  data = data.__data__
  inputStoreName.setAttribute("placeholder", data.name);
  inputPhonenumber.setAttribute("placeholder", "0" + data.phone);
  inputEmail.setAttribute("placeholder", data.email);
  inputDescription.setAttribute("placeholder", data.description);
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})

async function onFormsubmit(e) {
    e.preventDefault();
    var name = inputStoreName.value;
    var email = inputEmail.value;
    var phone = inputPhonenumber.value;
    var description = inputDescription.value;

    if (name == '' && email == '' && phone == '' && description == ''){
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
            description: description
        })
      }
      console.log(name, phone, email, description)
      fetch("/api/mystore/details", options)
      .then(data => data.json())
      .then(data =>  {
        console.log(data)
        if (data.error) {
          alert("Thay đổi thông tin cửa hàng thất bại");
        } else if (data.data.success) {
          alert("Thay đổi thông tin cửa hàng thành công"); 
          location.href = "/mystore/view-details";
        }
      })
      .catch((err) => {
        alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
        console.error(err);
      })
    }
}
