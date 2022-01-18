/*!
* Start Bootstrap - Shop Homepage v5.0.4 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
// Error
const err = {
    "Invalid product": "Một sản phẩm trong giỏ hàng của bạn không \
tồn tại hoặc đã bị xóa, vui lòng kiểm tra hoặc reload lại trang.",

    "Invalid quantity": "Số lượng sản phẩm trong giỏ hàng của bạn không được vượt quá số lượng sản phẩm trong kho, \
vui lòng kiểm tra hoặc reload lại trang.",
}

// Function declaration
async function showCartItems() {
    const res = await fetch('/api/cart');
    if (res.status != 200) {
        alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        return;
    }

    const products = await res.json();
    const template = document.querySelector('#item-template')
    
    for (const item of products) {
        const clone = template.content.cloneNode(true);

        clone.querySelector('tr').id = item.product_id;
        clone.querySelector('.product-name').textContent = item.name;
        clone.querySelector('.store-name').textContent = item.store_name;
        clone.querySelector('.view-detail').href += item.product_id;
        clone.querySelector('.price').textContent = item.price;
        clone.querySelector('.quantity').value = item.quantity;
        clone.querySelector('.quantity').dataset.prev = item.quantity;
        clone.querySelector('.quantity').max = item.product_quantity;
        clone.querySelector('.subtotal').textContent = item.price * item.quantity;
        clone.querySelector('.product-image > img').src = item.cover_image;
        document.querySelector('#cart-items').appendChild(clone);
    }

    document.querySelector('#total').textContent = 0; 
    selectItemEvent();
    deleteItemEvent();
    updateQuantityEvent();
}

function updateTotalPrice() {
    const total = document.querySelector('#total');
    const productNodes = document.querySelectorAll('#cart-items > tr');

    let totalPrice = 0;
    for (const productNode of productNodes) {
        const price = productNode.querySelector('.price').textContent;
        const quantity = productNode.querySelector('.quantity').value;
        const checkBox = productNode.querySelector('input[type="checkbox"]');

        if (checkBox.checked) {
            totalPrice += price * quantity;
        }
    }

    total.textContent = totalPrice;
}

function selectItemEvent() {
    const productNodes = document.querySelectorAll('#cart-items > tr');

    for (const productNode of productNodes) {
        const checkbox = productNode.querySelector("input[type='checkbox']");
        checkbox.addEventListener('change', () => {
            updateTotalPrice()
        });
    }
}

function deleteItemEvent() {
    const productNodes = document.querySelectorAll('#cart-items > tr');

    for (const productNode of productNodes) {
        const deleteButton = productNode.querySelector('.delete');
        deleteButton.addEventListener('click', async () => {
            const res = await fetch(`/api/cart/${productNode.id}`, {
                method: 'DELETE'
            });
            if (res.status != 200) {
                alert("Đã xảy ra lỗi, vui lòng thử lại sau");
                return;
            }

            productNode.remove();
            updateTotalPrice();
        });
    }
}

function updateQuantityEvent() {
    const productNodes = document.querySelectorAll('#cart-items > tr');

    for (const productNode of productNodes) {
        const quantity = productNode.querySelector('.quantity');
        const price = productNode.querySelector('.price');

        quantity.addEventListener('change', async () => {
            const options = {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    quantity: quantity.value
                })
            }
            const res = await fetch(`/api/cart/${productNode.id}/quantity`, options);
            const data = await res.json();

            if (res.status != 200) {
                if (res.status == 422) {
                    alert(err[data.error]);
                } 
                else {
                    alert("Đã xảy ra lỗi, vui lòng thử lại sau");
                }

                quantity.value = quantity.dataset.prev;
                return;
            }

            quantity.dataset.prev = quantity.value;
            console.log(price, quantity);
            productNode.querySelector('.subtotal').textContent = price.textContent * quantity.value;
            updateTotalPrice();
        });
    }
}

// order infomations
async function showProvices() {
    const res = await fetch('/api/address/provinces');
    const provinces = await res.json();
    provinces.sort((a, b) => {
        if (a._name <  b._name) return -1;
        return 1;
    });

    const select = document.querySelector('#province');
    for (const province of provinces) {
        const option = document.createElement('option');
        option.value = province.id;
        option.textContent = province._name;
        select.appendChild(option);
    }
}

async function showDistrict(provinceId) {
    const res = await fetch(`/api/address/districts?province_id=${provinceId}`);
    const districts = await res.json();
    districts.sort((a, b) => {
        if (a._prefix + a._name < b._prefix + b._name) return -1;
        return 1;
    });

    const select = document.querySelector('#district');
    for (const district of districts) {
        const option = document.createElement('option');
        option.value = district.id;
        option.textContent = district._prefix + ' ' + district._name;
        select.appendChild(option);
    }
}

async function showWard(districtId) {
    const res = await fetch(`/api/address/wards?district_id=${districtId}`);
    const wards = await res.json();
    wards.sort((a, b) => {
        if (a._prefix + a._name < b._prefix + b._name) return -1;
        return 1;
    });

    const select = document.querySelector('#ward');
    for (const ward of wards) {
        const option = document.createElement('option');
        option.value = ward.id;
        option.textContent = ward._prefix + ' ' + ward._name;
        select.appendChild(option);
    }
}

async function orderSubmit(e) {
    e.preventDefault();
    const products = [];
    
    const productNodes = document.querySelectorAll('#cart-items > tr');
    for (const productNode of productNodes) {
        if (productNode.querySelector("input[type='checkbox']").checked) {
            products.push({
                product_id: Number(productNode.id),
                quantity: Number(productNode.querySelector('.quantity').value)
            });
        }
    }

    if (products.length == 0) {
        alert('Bạn chưa chọn sản phẩm nào');
        return;
    }

    
    const phone = document.querySelector('#phone').value;
    if (isNaN(Number(phone)) || phone.length != 10) {
        alert('Số điện thoại không hợp lệ');
        return;
    }

    const payload = {
        recipient_name: document.querySelector('#name').value.trim(),
        recipient_phone: Number(phone),
        recipient_address: document.querySelector('#address').value.trim(),
        province_id: Number(document.querySelector('#province').value),
        district_id: Number(document.querySelector('#district').value),
        ward_id: Number(document.querySelector('#ward').value),
        products: products
    }
    
    const isSubmit = confirm('Bạn có chắc muốn đặt hàng?');
    if (isSubmit == false) {
        return;
    }

    const options = {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(payload)
    }

    const res = await fetch('/api/orders', options);
    const data = await res.json();
    if (res.status != 200) {
        if (res.status == 422) {
            alert(err[data.error]);
        } 
        else {
            alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        }
        return;
    }
    alert("Đặt hàng thành công");
    window.location.reload();
}

// Event listener
document.querySelector("#province").addEventListener('change', async (e) => {
    const provinceId = e.target.value;
    document.querySelector('#district').innerHTML = '<option value="" disabled selected>Select your option</option>';
    showDistrict(provinceId);
})

document.querySelector("#district").addEventListener('change', async (e) => {
    const districtId = e.target.value;
    document.querySelector('#ward').innerHTML = '<option value="" disabled selected>Select your option</option>';
    showWard(districtId);
})

document.querySelector("#order-details-form").addEventListener('submit', orderSubmit);

// Execute
showCartItems()
showProvices()
