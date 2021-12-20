const container = document.querySelector(".container");

var inputFullname = document.getElementById('name');
var inputDateofbirth = document.getElementById('dob');
var inputEmail = document.getElementById('email');
var inputPhonenumber = document.getElementById('phone');

var editProfileForm = document.getElementById('eidt_profile_form');

if (editProfileForm.attachEvent) {
  editProfileForm.attachEvent('submit', onFormsubmit);
} else {
  editProfileForm.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
  e.preventDefault();

  var name = inputFullname.value;
  var dob = inputDateofbirth.value;
  var email = inputEmail.value;
  var phone = inputPhonenumber.value;

  const options = {
    method: "POST",
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
  fetch("/users/edit_profile", options)
  .then(data => data.json())
  .then(data =>  { 
    console.log(data);
    alert("Sửa thông tin thành công"); 
    window.location.href = "signin.html";
  })
  .catch((err) => {
    alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
    console.error(err);
  })
  
}
