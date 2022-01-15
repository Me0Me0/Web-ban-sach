/*!
* Start Bootstrap - Shop Homepage v5.0.4 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
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
    const params = new URLSearchParams(window.location.search);
    const keyword = params.get("q");

    params.set("limit", limit * 5);
    params.set("skip", skip);
    params.set("keyword", keyword);
    params.delete("page");
    params.delete("q");

    const res = await fetch(`/api/products/search?${params.toString()}`);
    const data = await res.json();
    return data
}


async function showProducts() {
    let data = await getProducts();

    if (data.length == 0 && currentPage != 1) {
        urlSearchParams.set("page", 1);
        window.location.search = urlSearchParams;
    }
    
    if (data.length == 0) {
        searchNotFoundView();
        pageNext.remove();
        pagePrev.remove();
        pageItems.forEach(page => page.remove());

        return;
    }

    let remain = data.splice(limit, data.length - limit);

    showPagination(remain.length);

    for (const { __data__: product } of data) {
        const template = document.querySelector("#product-template").content;
        const clone = template.cloneNode(true);

        clone.querySelector("div").id = product.id;
        clone.querySelector(".product-name").textContent = product.name;
        clone.querySelector(".product-image").src = product.cover_image;
        clone.querySelector(".product-price").textContent = product.price + " VND";
        clone.querySelector("#product-detail").href = '/products/' + product.id;

        document.querySelector("#product-list").appendChild(clone);
    }
}


function sortEvent() {
    const sortSelect = document.querySelector("#sort-option");
    const sortBy = urlSearchParams.get("sortBy");
    const ascending = urlSearchParams.get("ascending") || "true";
    if (sortBy) {
        sortSelect.value = `${sortBy}-${ascending}`;
    }

    sortSelect.addEventListener("change", function (e) {
        const option = e.target.value.split("-");

        urlSearchParams.set("sortBy", option[0]);
        urlSearchParams.set("ascending", option[1]);
        window.location.search = urlSearchParams;
    })
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
            urlSearchParams.set("page", e.target.textContent);
            window.location.search = urlSearchParams;
        })
    });
    // prev click
    pagePrev.addEventListener("click", function (e) {
        urlSearchParams.set("page", currentPage - 1);
        window.location.search = urlSearchParams;
    });
    // next click
    pageNext.addEventListener("click", function (e) {
        urlSearchParams.set("page", currentPage + 1);
        window.location.search = urlSearchParams;
    });
}

sortEvent();
showProducts();


