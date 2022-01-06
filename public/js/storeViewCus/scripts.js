const options = {
    method: "GET", 
    headers: {
        "content-type": "text/plain;charset=UTF-8" // for a string body, depends on body
    }
  }
  
  fetch("/mystore", options)
  .then(data => data.json())
  .then(data =>  { 
    console.log(data);
    document.title = data.name;
    document.getElementById("storename").innerHTML = data.name;
  })
  .catch((err) => {
    alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
    console.error(err);
  })