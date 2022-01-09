/*!
* Start Bootstrap - Shop Homepage v5.0.4 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

async function getCartItems() {
    const res = await fetch('/api/cart');
    if (res.status != 200) {
        console.log("Đã xảy ra lỗi, vui lòng thử lại sau");
        return;
    }

    const items = await res.json();
    return items;
}


async function showCartItems() {
    const items = await getCartItems();
    const template = document.querySelector('#item-template')
    
    for (const item of items.products) {
        const clone = template.content.cloneNode(true);

        clone.querySelector('.product-name').textContent = item.name;
        clone.querySelector('.store-name').textContent = item.store_name;
        clone.querySelector('.view-detail').href += item.product_id;
        clone.querySelector('.price').textContent = item.price;
        clone.querySelector('.quantity').value = item.quantity;
        clone.querySelector('.subtotal').textContent = item.price * item.quantity;
        document.querySelector('#cart-items').appendChild(clone);
    }

    document.querySelector('#total').textContent = items.reduce((total, item) => total + item.price * item.quantity, 0); 
}

showCartItems()