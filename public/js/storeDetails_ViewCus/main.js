url = window.location.href;
id = url.substring(url.lastIndexOf('/stores/') + ('/stores/').length)
id = id.substring(0, id.lastIndexOf('/'))

const options = {
  method: "GET", 
  headers: {
      "content-type": "text/plain;charset=UTF-8" // for a string body, depends on body
  }
}

fetch(`/api/stores/${id}/details`, options)
.then(data => data.json())
.then(data =>  { 
  console.log(data);
  document.getElementById("name").innerHTML = data.name;
  document.getElementById("phone").innerHTML = "0" + data.phone;
  document.getElementById("email").innerHTML = data.email;
  document.getElementById("description").innerHTML = data.description;
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})
