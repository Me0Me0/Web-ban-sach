var formProfile = document.getElementById('profile_form');

if (formProfile.attachEvent) {
    formProfile.attachEvent('submit', onFormsubmit);
} else {
    formProfile.addEventListener('submit', onFormsubmit);
}

async function onFormsubmit(e) {
    e.preventDefault();

    fetch("/users/details", {
        method: "GET", 
        headers: {
            "Content-Type": "text/plain;charset=UTF-8" // for a string body, depends on body
        },
        body: JSON.stringify(data),
      })
    .then(data => data.json())
    .then(data =>  { 
      console.log(data);
        document.getElementById("name").innerHTML = data.data.name;
        document.getElementById("dob").innerHTML = data.data.dob;
        document.getElementById("phone").innerHTML = data.data.phone;
        document.getElementById("email").innerHTML = data.data.email;
    })
    .catch((err) => {
      alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
      console.error(err);
    })
}

