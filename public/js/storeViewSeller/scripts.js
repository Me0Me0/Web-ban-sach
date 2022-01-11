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
  console.log(data);
  document.getElementById("store-name").innerHTML = data.name;
  document.getElementById("go-to-order-list").href += data.id;
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})