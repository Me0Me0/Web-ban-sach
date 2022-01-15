async function show_total_income() {
    const res = await fetch('/api/mystore/business/total-income');
    //console.log(res);
    if (res.status != 200) {
        alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        return;
    }
    const data = await res.json();
    //console.log(data);
    document.getElementById("turnover").innerHTML = data.data.total_income + " VND";
}

async function show_best_sell_categories() {
    const res = await fetch('/api/mystore/business/best-sell-categories');
    //console.log(res);
    if (res.status != 200) {
        alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        return;
    }
    const data = await res.json();
    best_categories = data.slice(0, 3);

    console.log(best_categories);
    best_categories_content = document.getElementById("most-bought-category");
    for (let category of best_categories) {
        best_categories_content.innerHTML = best_categories_content.innerHTML + category.cate_id.name + ", ";
    }
}

async function show_best_sell_products() {
    const res = await fetch('/api/mystore/business/best-sell-products');
    //console.log(res);
    if (res.status != 200) {
        alert("Đã xảy ra lỗi, vui lòng thử lại sau");
        return;
    }
    const data = await res.json();
    best_products = data.slice(0, 3);

    const template = document.querySelector("#product-template");

    let i = 1;
    for (const product of best_products) {
        const clone = template.content.cloneNode(true);

        clone.querySelector("tr").id = product.id;
        clone.querySelector(".rank").textContent = i;
        clone.querySelector(".product-name").textContent = product.name;
        clone.querySelector(".price").innerHTML = product.price + " VND";
        clone.querySelector(".view-detail").href += product.id;
        clone.querySelector(".quantity").textContent = product.sum;
        i += 1;
        document.querySelector("#product-list").appendChild(clone);
    }
}

show_total_income()
show_best_sell_categories()
show_best_sell_products()