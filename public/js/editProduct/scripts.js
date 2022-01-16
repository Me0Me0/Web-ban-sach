const productID = location.pathname.split('/')[3];
document.getElementById("back-btn").setAttribute("onclick", `window.location.href = '/products/view-seller/${productID}'`);
// buttons
const addProductBtn = document.querySelector('#add-btn');
const backBtn = document.querySelector('#back');
const imagePaths = {};

let uploadImages = document.querySelectorAll('.fileupload');
let labels = document.querySelectorAll('.upload-image');

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
            const acceptedTypes = ['image/png', 'image/jpeg', 'image/jpg', 'image/gif'];

            if(acceptedTypes.includes(file.type)) {
                // means user uploaded an image
                // loading
                labels[index].style.backgroundImage = `url(https://gocchiase.net/wp-content/uploads/2021/10/tai-anh-dang-loading-messenger-trinh-duyet-anh-dong-gif-4.gif)`;

                const imageUrl = await uploadImage(file);
                labels[index].style.backgroundImage = `url(${imageUrl})`;

                if (index == 0) {
                    imagePaths[0] = {
                        image_link: imageUrl
                    }
                    console.log('yoyo: ', imagePaths[0])
                }
                else if (imagePaths[index]) {
                    imagePaths[index] = {
                        id: imagePaths[index].id,
                        image_link: imageUrl,
                    };
                }
                else {
                    imagePaths[index] = {
                        id: -1, // id = -1 means this image is new
                        image_link: imageUrl,
                    };
                }

                document.getElementById("cover-image").style.backgroundImage = `url(${imagePaths[0]})`;
                document.getElementById("text_img").innerHTML ="";
            } else{
                alert('Vui lòng tải ảnh có định dạng: png, jpg, jpeg, gif');
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
        const template = document.querySelector("#category-template-select").content;
        const clone = template.cloneNode(true);

        clone.querySelector("option").value = cate.id;
        clone.querySelector("option").textContent = cate.name;

        document.querySelector("#category").appendChild(clone);
    }
}
showCategory();

// Get product info
async function getProductInfo() {
    const res = await fetch('/api/products/' + productID);
    const data = await res.json();
    console.log(data)
    document.querySelector('#product-name').value = data.name;
    document.querySelector('#category').value = data.cate_id.id;
    document.querySelector('#description').value = data.description;
    document.querySelector('#detail').value = data.detail.replace(/<br>/g, '\n');
    document.querySelector('#author').value = data.author;
    document.querySelector('#page-number').value = data.number_of_pages;
    document.querySelector('#publishing-year').value = data.publishing_year;
    document.querySelector('#publisher').value = data.publisher;
    document.querySelector('#quantity').value = data.quantity;
    document.querySelector('#price').value = data.price;

    // cover
    imagePaths[0] = {
        image_link: data.cover_image
    }
    labels[0].style.backgroundImage = `url(${data.cover_image})`;

    // product images
    let i = 1;
    for (let {__data__: productImage} of data.product_images) {
        imagePaths[i] = {
            id: productImage.id,
            image_link: productImage.image_link
        }
        labels[i].style.backgroundImage = `url(${productImage.image_link})`;
        i++;
    }
}
getProductInfo();


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

    // Xử lý ảnh cover
    const cover_image = imagePaths[0].image_link;
    console.log(imagePaths[0])
    if (!cover_image) {
        alert("Vui lòng tải lên ảnh bìa.");
        return;
    }

    const product = {
        name: document.querySelector('#product-name').value,
        cate_id: document.querySelector('#category').value,
        description: document.querySelector('#description').value,
        detail: document.querySelector('#detail').value.replace(/\n/g, '<br>'),
        author: document.querySelector('#author').value,
        number_of_pages: document.querySelector('#page-number').value,
        publishing_year: document.querySelector('#publishing-year').value,
        publisher: document.querySelector('#publisher').value,
        quantity: document.querySelector('#quantity').value,
        price: document.querySelector('#price').value,
        cover_image: cover_image,
    }

    let options = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(product)
    }
    let res = await fetch(`/api/mystore/products/${productID}`, options);
    if (res.status != 200) {
        alert("Có lỗi xảy ra, vui lòng thử lại");
        return;
    }


    // update images
    let images = Object.values(imagePaths).slice(1);
    options = {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            list_image_link: images
        })
    }
    res = await fetch(`/api/mystore/products/${productID}/images`, options);
    if (res.status != 200) {
        alert("Có lỗi xảy ra, vui lòng thử lại");
        return;
    }

    alert("Cập nhật sản phẩm thành công");
    location.href = "/mystore";
});
