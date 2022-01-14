const userID = location.pathname.split('/')[3];

const options = {
  method: "GET", 
  headers: {
      "content-type": "text/plain;charset=UTF-8" // for a string body, depends on body
  }
}

fetch("/api/admin/users/" + userID, options)
.then(data => data.json())
.then(data =>  { 
  console.log(data);
  document.getElementById("name").innerHTML = data.name;
  document.getElementById("dob").innerHTML = data.dob;
  document.getElementById("phone").innerHTML = "0" + data.phone;
  document.getElementById("email").innerHTML = data.email;
  document.getElementById("username").innerHTML = data.username;
  document.getElementById("avt").src = data.avt_link;
  document.getElementById("status").innerHTML = data.deleted_at == null ? "Đang hoạt động" : "Đã xóa";

  if (data.deleted_at == null) {
    document.getElementById("btn-delete").style.display = "block";
  }
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})


async function delete_account() {
  const isSubmit = confirm('Bạn chắc chắn muốn xóa tài khoản?\
  Nếu xóa tài khoản, mọi thứ liên quan đến tài khoản này đều bị xóa');
  if (isSubmit == false) {
      return;
  }

  const options = {
      headers: {
          'Content-Type': 'text/plain;charset=UTF-8'
      },
      method: 'DELETE',
  }

  const res = await fetch('/api/admin/users/' + userID, options);
  const data = await res.json();
  if (res.status != 200) {
      if (res.status == 404) {
          alert("Xóa tài khoản thất bại");
      } 
      else {
          alert("Đã xảy ra lỗi, vui lòng thử lại sau");
      }
      return;
  }
  alert("Xóa tài khoản thành công");
  window.location.reload();
}