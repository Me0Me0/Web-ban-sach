const actualPrice = document.querySelector('#actual-price');
const discountPercentage = document.querySelector('#discount');
const sellingPrice = document.querySelector('#sell-price');
const productName = document.querySelector('#product-name');
const shortLine = document.querySelector('#short-des');
const des = document.querySelector('#des');
const author = document.querySelector('#author');
const pagenumber = document.querySelector('#apagenumber');
const publisher = document.querySelector('#publisher');
const publishyear = document.querySelector('#publishyear');
const stock = document.querySelector('#stock');

let cate = []; // will store all the cate

// buttons
const addProductBtn = document.querySelector('#add-btn');
const backBtn = document.querySelector('#back');

discountPercentage.addEventListener('input', () => {
    if(discountPercentage.value > 100){
        discountPercentage.value = 99;
    } else{
        let discount = actualPrice.value * discountPercentage.value / 100;
        sellingPrice.value = actualPrice.value - discount;
    }
})

sellingPrice.addEventListener('input', () => {
    let discount = (sellingPrice.value / actualPrice.value) * 100;
    discountPercentage.value = discount;
})

let uploadImages = document.querySelectorAll('.fileupload');
let imagePaths = [];

uploadImages.forEach((fileupload, index) => {
    fileupload.addEventListener('change', () => {
        const file = fileupload.files[0];
        let imageUrl;

        if(file.type.includes('image')){
            // means user uploaded an image
            label.style.backgroundImage = `url(${imageUrl})`;

        } else{
            showAlert('upload image only');
        }
    })
})