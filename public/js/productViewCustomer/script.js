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

function show_product_image(cover_image, product_images) {
  const template = document.querySelector("#product-image-template");

  let i = 1;
  if (cover_image != '') {
      const clone = template.content.cloneNode(true);

      clone.querySelector(".product-image").id += i;
      clone.querySelector(".product-image").src = cover_image;
      clone.querySelector(".product-image").style.display = "none";
      document.querySelector("#product-images").appendChild(clone);
      i += 1;
  }

  for (const { __data__: image } of product_images) {
      const clone = template.content.cloneNode(true);

      clone.querySelector("li").id = image.id;
      clone.querySelector(".product-image").id += i;
      clone.querySelector(".product-image").src = image.image_link;
      clone.querySelector(".product-image").style.display = "none";
      document.querySelector("#product-images").appendChild(clone);
      i += 1;
  }
  return i - 1;
}

fetch(`/api/products/${id}`, options)
.then(data => data.json())
.then(data =>  { 
  console.log(data);
  var number_of_image = show_product_image(data.cover_image, data.product_images);
  document.getElementById("product-name").innerHTML = data.name;
  var store = document.getElementById("store-name");
  store.innerHTML = data.store_id.name;
  store.setAttribute("onclick", `href='/stores/${data.store_id.id}'`)
  document.getElementById("category-name").innerHTML = data.cate_id.name;
  document.getElementById("author").innerHTML = data.author;
  document.getElementById("number-of-page").innerHTML = data.number_of_pages;
  document.getElementById("publishing-year").innerHTML = data.publishing_year;
  document.getElementById("publisher").innerHTML = data.publisher;
  document.getElementById("quantity").innerHTML = data.quantity;
  document.getElementById("description").innerHTML = data.description;
  document.getElementById("price").innerHTML = data.price;
  document.getElementById("details").innerHTML = data.detail;
  return number_of_image;
})
.then(number_of_image => {
  if (number_of_image != 0) {
      document.getElementById("image-1").style.display = "unset";
      document.getElementById("image-1").setAttribute("class", "show");
  }
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})

async function add_to_cart() {
  var quantity = document.getElementById("quantity-added").value
  if (quantity < 1)
  {
    alert("Số lượng sản phẩm thêm vào giỏ hàng phải lớn hơn 0");
    return;
  }
  const options = {
    method: "POST",
    headers: {
        "content-type": "text/plain;charset=UTF-8"
    }
  }
  const res = await fetch(`/api/products/${id}/add-to-cart?quantity=${quantity}`, options)
  const data = await res.json();

  console.log(data);
  if (data.error == "Unprocessable Entity") {
    alert("Số lượng sản phẩm bạn chọn vượt quá số lượng còn lại trong kho");
  } else if (data.error == "Unauthorized") {
    alert("Đăng nhập để có thể thêm sản phẩm vào giỏ hàng của bạn")
  } else if (data.data.success) {
    console.log(data);
    alert ("Sản phẩm đã được thêm vào giỏ hàng");
  } else {
    alert ("Thêm sản phẩm vào giỏ hàng thất bại");
    console.log(data);
  }
}

function showPreviousImage() {
  current_image = document.querySelector(".show");
  displayed_image_id = Number(current_image.id.substring(current_image.id.lastIndexOf('-') + ('-').length)) - 1;
  if (displayed_image_id < 1)
  {
      return;
  }
  current_image.setAttribute("class", "hide");
  current_image.style.display = "none";
  document.getElementById(`image-${displayed_image_id}`).style.display = "unset";
  document.getElementById(`image-${displayed_image_id}`).setAttribute("class", "show");
}
function showNextImage() {
  number_of_image = document.querySelectorAll("#product-images img").length;
  console.log(number_of_image);
  current_image = document.querySelector(".show");
  displayed_image_id = Number(current_image.id.substring(current_image.id.lastIndexOf('-') + ('-').length)) + 1;
  if (displayed_image_id > number_of_image)
  {
      return;
  }
  current_image.setAttribute("class", "hide");
  current_image.style.display = "none";
  document.getElementById(`image-${displayed_image_id}`).style.display = "unset";
  document.getElementById(`image-${displayed_image_id}`).setAttribute("class", "show");
}