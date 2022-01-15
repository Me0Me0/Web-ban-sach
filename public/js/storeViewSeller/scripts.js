const options = {
  method: "GET", 
  headers: {
      "content-type": "text/plain;charset=UTF-8" // for a string body, depends on body
  }
}

fetch("/api/mystore", options)
.then(data => data.json())
.then(data =>  {
  data = data.__data__
  console.log(data);
  document.getElementById("storename").innerHTML = data.name;
})
.catch((err) => {
  alert ("Đã xảy ra lỗi, vui lòng thử lại sau");
  console.error(err);
})
  

// --------- danh sach san pham -----------

const pageItems = document.querySelectorAll(".page-item");
const pagePrev = document.querySelector(".page-prev");
const pageNext = document.querySelector(".page-next");

const urlSearchParams = new URLSearchParams(window.location.search);
const currentPage = Number(urlSearchParams.get("page")) || 1;

const limit = 20;
const skip = (currentPage - 1) * limit;

function searchNotFoundView() {
    const template = document.querySelector("#search-not-found-template").content;
    const clone = template.cloneNode(true);

    document.querySelector("#product-list").appendChild(clone);
}

async function getProducts() {
    const res = await fetch(`/api/mystore/products?limit=${limit * 5}&skip=${skip}`);
    const data = await res.json();
    return data
}


async function showProducts() {
    let data = await getProducts();

    if (data.length == 0 && currentPage != 1) {
        const query = new URLSearchParams();
    
        query.set("page", "1");
        window.location.search = query.toString();
    }
    
    if (data.length == 0) {
        searchNotFoundView();
        pageNext.remove();
        pagePrev.remove();
        pageItems.forEach(page => page.remove());

        return;
    }

    let remain = data.splice(limit, data.length - limit);

    // let store = currentPage;
    // currentPage = 3;
    showPagination(remain.length);

    for (const { __data__: product } of data) {
        const template = document.querySelector("#product-template").content;
        const clone = template.cloneNode(true);

        clone.querySelector("div").id = product.id;
        clone.querySelector(".product-name").textContent = product.name;
        clone.querySelector(".product-image").src = product.cover_image;
        clone.querySelector(".product-price").textContent = product.price + " VND";
        clone.querySelector("#product-detail").href = '/products/view-seller/' + product.id;
        document.querySelector("#product-list").appendChild(clone);
    }
}

function showPagination(remainLen) {
    if (remainLen === 0) {
        pageNext.remove();
    }
    if (currentPage === 1) {
        pagePrev.remove();
    }

    if (currentPage <= 4) {
        pageItems[currentPage - 1].querySelector("a").classList.add("active");
        let extraPage = Math.ceil(remainLen / limit);
        
        if (currentPage + extraPage > 5) {
            extraPage = 5 - currentPage;
        }

        for (let i = currentPage + extraPage + 1; i <= 5; i++) {
            pageItems[i - 1].remove();
        }
    } 
    else {
        pageItems[pageItems.length - 1].querySelector("a").classList.add("active");
        let temp = currentPage;
        for (let i = pageItems.length - 1; i >= 0; i--) {
            pageItems[i].querySelector("a").textContent = temp;
            temp--;
        }
    }

    // page click
    [...pageItems].forEach(page => {
        page.addEventListener("click", function (e) {
            const query = new URLSearchParams();
    
            query.set("page", e.target.textContent);
            window.location.search = query.toString();
        })
    });
    // prev click
    pagePrev.addEventListener("click", function (e) {
        const query = new URLSearchParams();

        query.set("page", currentPage - 1);
        window.location.search = query.toString();
    });
    // next click
    pageNext.addEventListener("click", function (e) {
        const query = new URLSearchParams();

        query.set("page", currentPage + 1);
        window.location.search = query.toString();
    });
}

showProducts();




