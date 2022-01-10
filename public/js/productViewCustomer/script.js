/*
I want to thank Paul Rudnitskiy for his idea.
If you need full work version you can download it here  https://github.com/BlackStar1991/CardProduct
*/
//window.onload = function () {

    //// SLIDER
    // var slider = document.getElementsByClassName("sliderBlock_items");
    // var slides = document.getElementsByClassName("sliderBlock_items__itemPhoto");
    // var next = document.getElementsByClassName("sliderBlock_controls__arrowForward")[0];
    // var previous = document.getElementsByClassName("sliderBlock_controls__arrowBackward")[0];
    // var items = document.getElementsByClassName("sliderBlock_positionControls")[0];
    // var currentSlideItem = document.getElementsByClassName("sliderBlock_positionControls__paginatorItem");

    // var currentSlide = 0;
    // var slideInterval = setInterval(nextSlide, 5000);  /// Delay time of slides

    // function nextSlide() {
    //     goToSlide(currentSlide + 1);
    // }

    // function previousSlide() {
    //     goToSlide(currentSlide - 1);
    // }


    // function goToSlide(n) {
    //     slides[currentSlide].className = 'sliderBlock_items__itemPhoto';
    //     items.children[currentSlide].className = 'sliderBlock_positionControls__paginatorItem';
    //     currentSlide = (n + slides.length) % slides.length;
    //     slides[currentSlide].className = 'sliderBlock_items__itemPhoto sliderBlock_items__showing';
    //     items.children[currentSlide].className = 'sliderBlock_positionControls__paginatorItem sliderBlock_positionControls__active';
    // }


    // next.onclick = function () {
    //     nextSlide();
    // };
    // previous.onclick = function () {
    //     previousSlide();
    // };


    // function goToSlideAfterPushTheMiniBlock() {
    //     for (var i = 0; i < currentSlideItem.length; i++) {
    //         currentSlideItem[i].onclick = function (i) {
    //             var index = Array.prototype.indexOf.call(currentSlideItem, this);
    //             goToSlide(index);
    //         }
    //     }
    // }

    // goToSlideAfterPushTheMiniBlock();


/////////////////////////////////////////////////////////

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


/////  QUANTITY ITEMS

    // var up = document.getElementsByClassName('block_quantity__up')[0],
    //     down = document.getElementsByClassName('block_quantity__down')[0],
    //     input = document.getElementsByClassName('block_quantity__number')[0];

    // function getValue() {
    //     return parseInt(input.value);
    // }

    // up.onclick = function (event) {
    //     input.value = getValue() + 1;
    // };
    // down.onclick = function (event) {
    //     if (input.value <= 1) {
    //         return 1;
    //     } else {
    //         input.value = getValue() - 1;
    //     }

    // }


//};
url = window.location.href;
id = url.substring(url.lastIndexOf('/') + ('/').length)

const options = {
    method: "GET",
    headers: {
        "content-type": "text/plain;charset=UTF-8"
    }
}

fetch(`/api/products/${id}`, options)
.then(data => data.json())
.then(data =>  { 
  console.log(data);
  document.getElementById("product-name").innerHTML = data.name;
  var store = document.getElementById("store-name");
  store.innerHTML = data.store_id.name;
  store.onclick = `href='/stores/${id}'`
  document.getElementById("category-name").innerHTML = data.cate_id.name;
  document.getElementById("author").innerHTML = data.author;
  document.getElementById("number-of-page").innerHTML = data.number_of_pages;
  document.getElementById("publishing-year").innerHTML = data.publishing_year;
  document.getElementById("publisher").innerHTML = data.publisher;
  document.getElementById("quantity").innerHTML = data.quantity;
  document.getElementById("description").innerHTML = data.description;
  document.getElementById("price").innerHTML = data.price;
  
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})

async function add_to_cart() {
  var quantity = document.getElementById("quantity-added").value
  const options = {
    method: "POST",
    headers: {
        "content-type": "text/plain;charset=UTF-8"
    }
  }
  const res = await fetch(`/api/products/${id}/add-to-cart?quantity=${quantity}`, options)
  const data = await res.json();

  if (data.error) {
    alert("Thêm sản phẩm vào giỏ hàng thất bại")
    console.log(data)
  } else if (data.data.success) {
    console.log(data);
    alert ("Sản phẩm đã được thêm vào giỏ hàng")
  } else {
    alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
    console.log(data);
  }
}