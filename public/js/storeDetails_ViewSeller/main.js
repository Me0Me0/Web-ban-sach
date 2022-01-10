const options = {
  method: "GET", 
  headers: {
      "content-type": "text/plain;charset=UTF-8" // for a string body, depends on body
  }
}

fetch("/api/mystore", options)
.then(data => data.json())
.then(data =>  { 
  data = data.__data__
  document.getElementById("store-name").innerHTML = data.name;
  document.getElementById("phone").innerHTML = "0" + data.phone;
  document.getElementById("email").innerHTML = data.email;
  document.getElementById("description").innerHTML = data.description;
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})
