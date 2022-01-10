/*!
* Start Bootstrap - Shop Homepage v5.0.4 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
async function showOrders() {
    const res = await fetch('/api/orders');
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
        clone.querySelector('.status').textContent = order.status;
        clone.querySelector('.subtotal').textContent = order.total_cost;
        document.querySelector('#order-list').appendChild(clone);
    }
}

showOrders()