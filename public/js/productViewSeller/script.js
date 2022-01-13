// /*
// I want to thank Paul Rudnitskiy for his idea.
// If you need full work version you can download it here  https://github.com/BlackStar1991/CardProduct
// */



// window.onload = function () {

//     //// SLIDER
//     var slider = document.getElementsByClassName("sliderBlock_items");
//     var slides = document.getElementsByClassName("sliderBlock_items__itemPhoto");
//     var next = document.getElementsByClassName("sliderBlock_controls__arrowForward")[0];
//     var previous = document.getElementsByClassName("sliderBlock_controls__arrowBackward")[0];
//     var items = document.getElementsByClassName("sliderBlock_positionControls")[0];
//     var currentSlideItem = document.getElementsByClassName("sliderBlock_positionControls__paginatorItem");

//     var currentSlide = 0;
//     var slideInterval = setInterval(nextSlide, 5000);  /// Delay time of slides

//     function nextSlide() {
//         goToSlide(currentSlide + 1);
//     }

//     function previousSlide() {
//         goToSlide(currentSlide - 1);
//     }


//     function goToSlide(n) {
//         slides[currentSlide].className = 'sliderBlock_items__itemPhoto';
//         items.children[currentSlide].className = 'sliderBlock_positionControls__paginatorItem';
//         currentSlide = (n + slides.length) % slides.length;
//         slides[currentSlide].className = 'sliderBlock_items__itemPhoto sliderBlock_items__showing';
//         items.children[currentSlide].className = 'sliderBlock_positionControls__paginatorItem sliderBlock_positionControls__active';
//     }


//     next.onclick = function () {
//         nextSlide();
//     };
//     previous.onclick = function () {
//         previousSlide();
//     };


//     function goToSlideAfterPushTheMiniBlock() {
//         for (var i = 0; i < currentSlideItem.length; i++) {
//             currentSlideItem[i].onclick = function (i) {
//                 var index = Array.prototype.indexOf.call(currentSlideItem, this);
//                 goToSlide(index);
//             }
//         }
//     }

//     goToSlideAfterPushTheMiniBlock();


// /////////////////////////////////////////////////////////

// ///// Specification Field


//     var buttonFullSpecification = document.getElementsByClassName("block_specification")[0];
//     var buttonSpecification = document.getElementsByClassName("block_specification__specificationShow")[0];
//     var buttonInformation = document.getElementsByClassName("block_specification__informationShow")[0];

//     var blockCharacteristiic = document.querySelector(".block_descriptionCharacteristic");
//     var activeCharacteristic = document.querySelector(".block_descriptionCharacteristic__active");


//     buttonFullSpecification.onclick = function () {

//         console.log("OK");


//         buttonSpecification.classList.toggle("hide");
//         buttonInformation.classList.toggle("hide");


//         blockCharacteristiic.classList.toggle("block_descriptionCharacteristic__active");


//     };


// /////  QUANTITY ITEMS

//     var up = document.getElementsByClassName('block_quantity__up')[0],
//         down = document.getElementsByClassName('block_quantity__down')[0],
//         input = document.getElementsByClassName('block_quantity__number')[0];

//     function getValue() {
//         return parseInt(input.value);
//     }

//     up.onclick = function (event) {
//         input.value = getValue() + 1;
//     };
//     down.onclick = function (event) {
//         if (input.value <= 1) {
//             return 1;
//         } else {
//             input.value = getValue() - 1;
//         }

//     }


// };

url = window.location.href;
id = url.substring(url.lastIndexOf('/') + ('/').length)

async function check_valid_user(store_id, product_id) {
    const options = {
        method: "GET",
        headers: {
            "content-type": "text/plain;charset=UTF-8"
        }
    }

    const res = await fetch('/api/mystore', options);
    if (res.status != 200) {
        alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        return; 
    }
    const data = await res.json();
    if (data.__data__.id == store_id)
    {
        return;
    }
    window.location.href = `/products/${product_id}`;
}

async function show_product(id) {
    const options = {
        method: "GET",
        headers: {
            "content-type": "text/plain;charset=UTF-8"
        }
    }

    const res = await fetch(`/api/products/${id}`, options);
    if (res.status != 200) {
        alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        window.location.href = '/mystore';
        return; 
    }
    const data = await res.json();
    if (data.error == 404)
    {
        alert("Sản phẩm không tồn tại");
        return;
    }
    check_valid_user(data.store_id.id, data.id);
    console.log(data);
    document.getElementById("product-name").innerHTML = data.name;
    document.getElementById("category-name").innerHTML = data.cate_id.name;
    document.getElementById("author").innerHTML = data.author;
    document.getElementById("number-of-page").innerHTML = data.number_of_pages;
    document.getElementById("publishing-year").innerHTML = data.publishing_year;
    document.getElementById("publisher").innerHTML = data.publisher;
    document.getElementById("quantity").innerHTML = data.quantity;
    document.getElementById("description").innerHTML = data.description;
    document.getElementById("price").innerHTML = data.price;
    document.getElementById("details").innerHTML = data.detail;
    document.getElementById("edit-product").setAttribute("onclick", `window.location.href = '/products/edit-product/${id}'`);
    document.getElementById("delete-product").setAttribute("onclick", `delete_product(${id})`);
}

async function delete_product(id) {
    const isSubmit = confirm('Bạn chắc chắn muốn xóa sản phẩm này?');
    if (isSubmit == false) {
        return;
    }
  
    const options = {
        headers: {
            'Content-Type': 'text/plain;charset=UTF-8'
        },
        method: 'DELETE',
    }
  
    const res = await fetch(`/api/products/${id}`, options);
    const data = await res.json();
    console.log(res);
    if (res.status != 200) {
        if (res.status == 404) {
            alert("Xóa sản phẩm thất bại");
        }
        else if (res.status == 403)
        {
            alert("Bạn không có quyền xóa sản phẩm này");
        }
        else {
            alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        }
        return;
    }
    alert("Xóa sản phẩm thành công, bạn sẽ được đưa về trang cửa hàng của bạn");
    window.location.href = '/mystore';
}

show_product(id);