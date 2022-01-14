// api get category
async function showCategory() {
    const res = await fetch("/api/products/categories");
    const data = await res.json();

    for (const { __data__: cate} of data) {
        const template = document.querySelector("#category-template").content;
        const clone = template.cloneNode(true);

        clone.querySelector("li").dataset.id = cate.id;
        clone.querySelector(".category-name").textContent = cate.name;
        clone.querySelector(".category-link").href = "/products/category/" + cate.id;

        document.querySelector(".categories-ul").appendChild(clone);
    }
}
showCategory();

async function showTopCategory() {
    var res = await fetch("api/products/top-cate?limit=5");
    var categories = await res.json();

    console.log(categories);
    
    let i = 1
    for (let { __data__: category } of categories) {
        content = document.querySelector(`#cate-${i}`);
        content.textContent = category.name;
        content.href += category.id;
        i += 1;
    }

    res = await fetch("/api/products/categories");
    totalCategories = await res.json();

    for (let { __data__: category } of totalCategories) {
        if (i > 5) break;

        const found = categories.find(cate => cate.__data__.id == category.id);
        if (!found) {
            content = document.querySelector(`#cate-${i}`);
            content.textContent = category.name;
            content.href += category.id;
            i += 1;
        }
    }
}

async function showNewProduct() {
    const res = await fetch('/api/products/newest?limit=5');
    const items = await res.json();

    console.log(items)

    for (let { __data__: item } of items) {
        const template = document.querySelector("#new-arrivals-item-template");
        const clone = document.importNode(template.content, true);

        clone.querySelector(".item").dataset.id = item.id;
        // clone.querySelector(".item-img > img").src = "https://i.pinimg.com/736x/53/38/f8/5338f8f34d04e94e076d1d2e6d2350a0.jpg";
        clone.querySelector(".price > p").textContent = item.price;
        clone.querySelector(".title > a").textContent = item.name;
        clone.querySelector(".detail").href = `/products/${item.id}`;
        clone.querySelector(".title > a").href = `/products/${item.id}`;
        document.querySelector(".new-arrivals.item-list").appendChild(clone);
    }
}

async function showBestSeller() {
    const res = await fetch('/api/products/top-product?limit=5');
    const items = await res.json();

    console.log(items)

    if (items.length == 0)
    {
        document.querySelector(".best-seller").style.display = "none";
        return;
    }

    for (let { __data__: item } of items) {
        const template = document.querySelector("#best-seller-item-template");
        const clone = document.importNode(template.content, true);

        clone.querySelector(".item").dataset.id = item.id;
        // clone.querySelector(".item-img > img").src = "https://i.pinimg.com/736x/53/38/f8/5338f8f34d04e94e076d1d2e6d2350a0.jpg";
        clone.querySelector(".price > p").textContent = item.price;
        clone.querySelector(".title > a").textContent = item.name;
        clone.querySelector(".detail").href = `/products/${item.id}`;
        clone.querySelector(".title > a").href = `/products/${item.id}`;
        document.querySelector(".best-seller.item-list").appendChild(clone);
    }
}

showTopCategory()
showBestSeller()
showNewProduct()