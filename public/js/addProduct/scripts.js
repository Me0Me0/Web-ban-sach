// const actualPrice = document.querySelector('#actual-price');
// const discountPercentage = document.querySelector('#discount');
// const sellingPrice = document.querySelector('#sell-price');
// const productName = document.querySelector('#product-name');
// const shortLine = document.querySelector('#short-des');
// const des = document.querySelector('#des');
// const author = document.querySelector('#author');
// const pagenumber = document.querySelector('#apagenumber');
// const publisher = document.querySelector('#publisher');
// const publishyear = document.querySelector('#publishyear');
// const stock = document.querySelector('#stock');

// let cate = []; // will store all the cate

// buttons
const addProductBtn = document.querySelector('#add-btn');
const backBtn = document.querySelector('#back');

// discountPercentage.addEventListener('input', () => {
//     if(discountPercentage.value > 100){
//         discountPercentage.value = 99;
//     } else{
//         let discount = actualPrice.value * discountPercentage.value / 100;
//         sellingPrice.value = actualPrice.value - discount;
//     }
// })

// sellingPrice.addEventListener('input', () => {
//     let discount = (sellingPrice.value / actualPrice.value) * 100;
//     discountPercentage.value = discount;
// })

let uploadImages = document.querySelectorAll('.fileupload');
let labels = document.querySelectorAll('.upload-image');
let imagePaths = {};


async function uploadImage(file) {
    const formData = new FormData();
    formData.append('file', file);

    const options = {
        method: 'POST',
        body: formData
    }
    const res = await fetch('/api/images/upload', options);
    const data = await res.json();
    
    return data.url
}

async function uploadImageHandler() {    
    uploadImages.forEach((fileupload, index) => {
        fileupload.addEventListener('change', async () => {
            const file = fileupload.files[0];
            
            if(file.type.includes('image')){
                // means user uploaded an image
                const imageUrl = await uploadImage(file);
                labels[index].style.backgroundImage = `url(${imageUrl})`;
                imagePaths[index] = imageUrl;
            } else{
                showAlert('upload image only');
            }
        })
    })
}

uploadImageHandler()


// show category
async function showCategory() {
    const res = await fetch("/api/products/categories");
    const data = await res.json();
    
    for (const { __data__: cate} of data) {
      const template = document.querySelector("#category-template").content;
      const clone = template.cloneNode(true);
  
      clone.querySelector("option").value = cate.id;
      clone.querySelector("option").textContent = cate.name;

      document.querySelector("#category").appendChild(clone);
    }
  }
  
  showCategory();


function checkNumberInput(field) {
    if (isNaN(field) || field < 0) {
        alert(`Trường ${field} không hợp lệ`);
        return false;
    }

    return true;
}


// create product
document.querySelector("#product-form").addEventListener('submit', async (e) => {
    e.preventDefault();
    // Kiem tra nam
    const publishing_year = Number(document.querySelector('#publishing-year').value);
    const number_of_pages = Number(document.querySelector('#page-number').value);
    const quantity = Number(document.querySelector('#quantity').value);
    const price = Number(document.querySelector('#price').value);

    if (
        !checkNumberInput(publishing_year) ||
        !checkNumberInput(number_of_pages) ||
        !checkNumberInput(quantity) ||
        !checkNumberInput(price)) {
        return;
    }

    const product = {
        name: document.querySelector('#product-name').value,
        cate_id: document.querySelector('#category').value,
        description: document.querySelector('#description').value,
        detail: document.querySelector('#detail').value,
        author: document.querySelector('#author').value,
        number_of_pages: document.querySelector('#page-number').value,
        publishing_year: document.querySelector('#publishing-year').value,
        publisher: document.querySelector('#publisher').value,
        quantity: document.querySelector('#quantity').value,
        price: document.querySelector('#price').value,
        cover_image: "http://smartmobilestudio.com/wp-content/uploads/2012/06/leather-book-preview.png",
        image_links: Object.values(imagePaths)
    }

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(product)
    }
    const res = await fetch('/api/mystore/products/new', options)

    if (res.status != 200) {
        alert("Có lỗi xảy ra, vui lòng thử lại");
        return;
    }

    alert("Thêm sản phẩm thành công");
    location.href = "/mystore";

});