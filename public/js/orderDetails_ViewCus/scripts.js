const url = window.location.href;
const order_id = url.substring(url.lastIndexOf('/') + ('/').length);

async function get_order_details(order_id) {
    const options = {
        method: "GET",
        headers: {
            "content-type": "text/plain;charset=UTF-8"
        }
    }

    const res = await fetch(`/api/orders/${order_id}`, options);
    if (res.status != 200) {
        alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        return;
    }
    const data = await res.json();
    console.log(data);
    document.getElementById("order-id").innerHTML = data.id;
    switch(data.status) {
        case 1:
            document.getElementById("status").innerHTML = "Đang xử lý";
            break;
        case 2:
            document.getElementById("status").innerHTML = "Đang giao";
            break;
        case 3:
            document.getElementById("status").innerHTML = "Đã hoàn thành";
            break;
        case 4:
            document.getElementById("status").innerHTML = "Đã hủy";
            break;
        default:
            document.getElementById("status").innerHTML = "Không xác định";
    }
    document.getElementById("recipient-name").innerHTML = data.recipient_name;
    document.getElementById("recipient-phone").innerHTML = data.recipient_phone;
    document.getElementById("recipient-address").innerHTML = get_address(data);
    document.getElementById("total").innerHTML = data.total_cost;
    document.getElementById("cancel-order").setAttribute("onclick", `cancel_order(${order_id})`);

    const products = data.order_products;
    console.log(products);
    const template = document.querySelector("#item-template");

    for (const product of products) {
        const clone = template.content.cloneNode(true);
        
        clone.querySelector("tr").id = product.product_id.id;
        clone.querySelector(".product-name").textContent = product.product_id.name;
        clone.querySelector(".view-detail").href += product.product_id.id;
        clone.querySelector(".price").textContent = product.product_id.price + " VND";
        clone.querySelector(".quantity").textContent = product.quantity;
        document.querySelector("#order-items").appendChild(clone);
    }
}

function get_address(data) {
    var address = data.recipient_address;
    address = address + ", " + data.ward_id._prefix + ' ' + data.ward_id._name;
    address = address + ", " + data.district_id._prefix + ' ' + data.district_id._name;
    address = address + ", " + data.province_id._name;
    return address;
}

async function cancel_order(order_id) {
    const isSubmit = confirm('Bạn có chắc chắn muốn hủy đơn hàng?');
    if (isSubmit == false) {
        return;
    }

    const options = {
        method: "DELETE",
        headers: {
            "content-type": "text/plain;charset=UTF-8"
        }
    }

    const res = await fetch(`/api/orders/${order_id}`, options);
    if (res.status != 200) {
        alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        return;
    }
    const data = await res.json();

    console.log(data);
    if (data.data.success) {
        alert("Hủy đơn hàng thành công");
        location.href = "history.back()";
    } else {
        alert("Hủy đơn hàng thất bại");
    }
}

get_order_details(order_id);