async function showNewProduct() {
    const res = await fetch('/api/products/newest&limit=10', { method: 'POST' });
    const items = await res.json();

    console.log(items)

    for (let { __data__: item } of items) {
        const template = document.querySelector("#new-arrivals-item-template");
        const clone = document.importNode(template.content, true);

        clone.querySelector(".item").dataset.id = item.id;
        // clone.querySelector(".item-img > img").src = item.cover_image;
        clone.querySelector(".price > p").textContent = item.price;
        clone.querySelector(".title > a").textContent = item.name;
        clone.querySelector(".detail").href = `/products/${item.id}`;
        clone.querySelector(".title > a").href = `/products/${item.id}`;
        document.querySelector(".new-arrivals.item-list").appendChild(clone);
    }
}


showNewProduct()