/*!
* Start Bootstrap - Shop Homepage v5.0.4 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

async function showOrders() {
    const res = await fetch('/api/mystore/orders');
    console.log(res)
    if (res.status != 200) {
        alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        return;
    }

    const orders = await res.json();
    const template = document.querySelector('#order-template')
    
    for (const order of orders) {
        const clone = template.content.cloneNode(true);

        clone.querySelector('tr').id = order.id;
        clone.querySelector('.order-id').textContent = order.id;
        clone.querySelector('.view-detail').href += order.id;
        switch(order.status) {
            case 1:
                clone.querySelector('.status').textContent = "Đang xử lý";
                break;
            case 2:
                clone.querySelector('.status').textContent = "Đang giao";
                break;
            case 3:
                clone.querySelector('.status').textContent = "Đã hoàn thành";
                break;
            case 4:
                clone.querySelector('.status').textContent = "Đã hủy";
                break;
            default:
                clone.querySelector('.status').textContent = "Không xác định";
        }
        clone.querySelector('.subtotal').textContent = order.total_cost;
        document.querySelector('#order-list').appendChild(clone);
    }
}

showOrders()